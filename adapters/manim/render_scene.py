"""Manim Community adapter smoke renderer for HAA-D-3 SceneSpec.

Consumes only validated, renderer-neutral JSON data. No dynamic code or prompt
execution is performed. Set HAA_D3_SCENE_FILE to the SceneSpec path.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from manim import (
    BLUE_C, Circle, Dot, FadeIn, FadeOut, MathTex, ORIGIN, Scene,
    Text, VGroup, WHITE, YELLOW, DOWN, UP,
)


def _position_at(keyframes: list[dict], time_seconds: float) -> tuple[float, float, float]:
    if not keyframes:
        return (0.0, 0.0, 0.0)
    if time_seconds <= keyframes[0]["time_seconds"]:
        return tuple(keyframes[0]["value"])
    for left, right in zip(keyframes, keyframes[1:]):
        t0, t1 = left["time_seconds"], right["time_seconds"]
        if t0 <= time_seconds <= t1:
            alpha = 0.0 if t1 == t0 else (time_seconds - t0) / (t1 - t0)
            return tuple(a + (b - a) * alpha for a, b in zip(left["value"], right["value"]))
    return tuple(keyframes[-1]["value"])


class HaaD3SceneSpecSmoke(Scene):
    """Render a SceneSpec's oscillator tracks as a labeled 2D scientific shot."""

    def construct(self) -> None:
        source = Path(os.environ.get("HAA_D3_SCENE_FILE", ""))
        if not source.is_file():
            raise FileNotFoundError("HAA_D3_SCENE_FILE must point to a generated SceneSpec")
        scene = json.loads(source.read_text(encoding="utf-8"))
        if scene.get("schema_version") != "0.1.0" or not isinstance(scene.get("objects"), list):
            raise ValueError("unsupported or malformed SceneSpec")
        tracks = []
        for item in scene["objects"]:
            if item.get("type") != "oscillator":
                continue
            animation = item.get("animation", [])
            track = next((a for a in animation if a.get("property") == "transform.position"), None)
            if track and track.get("keyframes"):
                tracks.append((item["id"], track["keyframes"]))
        if not tracks:
            raise ValueError("SceneSpec contains no oscillator position tracks")
        if len(tracks) > 64:
            raise ValueError("Manim smoke adapter limit is 64 oscillator tracks")

        title = Text("HAA-D-3  /  COUPLED OSCILLATORS", font_size=28, color=WHITE)
        subtitle = Text("Analytical model output · not biological anatomy", font_size=16, color=BLUE_C)
        subtitle.next_to(title, down, buff=0.12)
        header = VGroup(title, subtitle).to_edge(UP, buff=0.35)
        orbit = Circle(radius=2.25, color=BLUE_C, stroke_opacity=0.35)
        center = Dot(ORIGIN, radius=0.055, color=WHITE)
        dots = VGroup(*[Dot(radius=0.075, color=YELLOW) for _ in tracks])
        labels = MathTex(r"r(t)=\left|\frac{1}{N}\sum_j e^{i\theta_j(t)}\right|", font_size=34)
        labels.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(header), FadeIn(orbit), FadeIn(center), FadeIn(labels), FadeIn(dots))
        duration = min(max(float(scene.get("duration_seconds", 1.0)), 0.5), 8.0)
        fps = min(max(float(scene.get("frame_rate", 24)), 8.0), 30.0)
        frames = max(2, round(duration * fps))
        for frame in range(frames):
            t = duration * frame / (frames - 1)
            for dot, (_, keyframes) in zip(dots, tracks):
                x, y, _z = _position_at(keyframes, t)
                dot.move_to((float(x) * 1.6, float(y) * 1.6, 0))
            self.wait(1.0 / fps)
        self.play(FadeOut(VGroup(header, orbit, center, dots, labels)))
