"""Deterministic, renderer-independent SVG frame renderer for SceneSpec."""
from __future__ import annotations

import math
from pathlib import Path
from xml.sax.saxutils import escape
from typing import Any


def _interpolate(keyframes: list[dict[str, Any]], time_seconds: float) -> Any:
    if not keyframes:
        return [0.0, 0.0, 0.0]
    ordered = sorted(keyframes, key=lambda item: float(item["time_seconds"]))
    first_value = ordered[0]["value"]
    if not isinstance(first_value, (list, tuple)):
        if time_seconds <= float(ordered[0]["time_seconds"]):
            return float(first_value)
    if time_seconds <= float(ordered[0]["time_seconds"]):
        return list(first_value)
    if time_seconds >= float(ordered[-1]["time_seconds"]):
        last_value = ordered[-1]["value"]
        return float(last_value) if not isinstance(last_value, (list, tuple)) else list(last_value)
    for left, right in zip(ordered, ordered[1:]):
        start, end = float(left["time_seconds"]), float(right["time_seconds"])
        if start <= time_seconds <= end:
            ratio = (time_seconds - start) / (end - start)
            left_value, right_value = left["value"], right["value"]
            if not isinstance(left_value, (list, tuple)):
                return float(left_value) + (float(right_value) - float(left_value)) * ratio
            return [float(a) + (float(b) - float(a)) * ratio for a, b in zip(left_value, right_value)]
    last_value = ordered[-1]["value"]
    return float(last_value) if not isinstance(last_value, (list, tuple)) else list(last_value)


def _object_position(obj: dict[str, Any], time_seconds: float) -> list[float]:
    for track in obj.get("animation", []):
        if track.get("property") == "transform.position":
            return _interpolate(track.get("keyframes", []), time_seconds)
    return list(obj.get("transform", {}).get("position", [0.0, 0.0, 0.0]))


def render_scene_frames(
    scene: dict[str, Any],
    output_dir: Path,
    *,
    frame_rate: float | None = None,
    width: int = 1280,
    height: int = 720,
) -> list[Path]:
    """Render SVG frames using only the Python standard library."""
    fps = float(frame_rate if frame_rate is not None else scene["frame_rate"])
    duration = float(scene["duration_seconds"])
    if not math.isfinite(fps) or fps <= 0:
        raise ValueError("frame_rate must be finite and positive")
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("duration_seconds must be finite and positive")
    if width < 160 or height < 120:
        raise ValueError("render dimensions are too small")
    frame_count = int(math.floor(duration * fps + 1e-9)) + 1
    if frame_count > 10000:
        raise ValueError("frame count exceeds safety limit (10000)")
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    cx, cy = width / 2, height / 2
    scale = min(width, height) * 0.32
    objects = scene.get("objects", [])
    for frame in range(frame_count):
        timestamp = min(frame / fps, duration)
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            '<rect width="100%" height="100%" fill="#07111f"/>',
            f'<text x="36" y="48" fill="#e8f2ff" font-family="sans-serif" font-size="22">{escape(str(scene.get("title", "HAA-D-3")))}</text>',
            f'<text x="36" y="{height-28}" fill="#9bb2c8" font-family="monospace" font-size="14">t={timestamp:.3f}s · {escape(str(scene.get("metadata", {}).get("evidence_class", "UNKNOWN")))}</text>',
        ]
        for obj in objects:
            position = _object_position(obj, timestamp)
            x = cx + float(position[0]) * scale
            y = cy - float(position[1]) * scale
            if obj.get("type") == "oscillator":
                parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="7" fill="#58d5df" stroke="#d8fbff" stroke-width="1.5"/>')
            elif obj.get("type") == "metric":
                value = 0.0
                for track in obj.get("animation", []):
                    if track.get("property") == "material.emission_intensity":
                        value = _interpolate(track.get("keyframes", []), timestamp)
                radius = 18 + max(0.0, min(1.0, value)) * 46
                parts.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.3f}" fill="none" stroke="#f6b85d" stroke-width="3" opacity="0.72"/>')
        parts.append("</svg>")
        path = output_dir / f"{frame:06d}.svg"
        path.write_text("\n".join(parts) + "\n", encoding="utf-8")
        paths.append(path)
    return paths
