"""Explicit, renderer-neutral mappings from research outputs to SceneSpec."""
from __future__ import annotations

from typing import Any
import math


def kuramoto_to_scene(
    simulation: dict[str, Any],
    *,
    scene_id: str | None = None,
    frame_rate: float = 24.0,
    orbit_radius: float = 1.0,
) -> dict[str, Any]:
    """Map Kuramoto phases to a circular analytical scene.

    x = R*cos(theta), y = R*sin(theta). The order parameter is mapped to a
    global coherence metric. This is an analytical visualization, not anatomy.
    """
    if simulation.get("model") != "kuramoto_mean_field":
        raise ValueError("simulation model must be kuramoto_mean_field")
    params = simulation.get("parameters", {})
    samples = simulation.get("samples", [])
    nodes = params.get("nodes")
    if not isinstance(nodes, int) or nodes < 2 or not samples:
        raise ValueError("simulation must contain at least two nodes and one sample")
    if isinstance(frame_rate, bool) or not isinstance(frame_rate, (int, float)) or frame_rate <= 0:
        raise ValueError("frame_rate must be a positive number")
    if isinstance(orbit_radius, bool) or not isinstance(orbit_radius, (int, float)) or orbit_radius <= 0:
        raise ValueError("orbit_radius must be a positive number")
    for sample in samples:
        phases = sample.get("phases_radians", [])
        if len(phases) != nodes:
            raise ValueError("each sample must contain one phase per oscillator")

    objects: list[dict[str, Any]] = []
    for index in range(nodes):
        keyframes = []
        for sample in samples:
            theta = sample["phases_radians"][index]
            keyframes.append({
                "time_seconds": sample["time_seconds"],
                "value": [
                    round(orbit_radius * math.cos(theta), 9),
                    round(orbit_radius * math.sin(theta), 9),
                    0.0,
                ],
            })
        first = keyframes[0]["value"]
        objects.append({
            "id": f"oscillator-{index:04d}",
            "type": "oscillator",
            "transform": {"position": first, "scale": [1.0, 1.0, 1.0]},
            "geometry": {"primitive": "point"},
            "animation": [{"property": "transform.position", "keyframes": keyframes}],
            "data_binding": {
                "source_model": simulation["model"],
                "source_field": f"samples[*].phases_radians[{index}]",
                "evidence_class": "MODEL_OUTPUT",
                "mapping": "polar_phase_to_cartesian_position",
                "orbit_radius": orbit_radius,
            },
        })

    coherence_keys = [
        {"time_seconds": sample["time_seconds"], "value": sample["order_parameter"]}
        for sample in samples
    ]
    objects.append({
        "id": "global-coherence",
        "type": "metric",
        "transform": {"position": [0.0, 0.0, 0.0]},
        "animation": [{"property": "material.emission_intensity", "keyframes": coherence_keys}],
        "data_binding": {
            "source_model": simulation["model"],
            "source_field": "samples[*].order_parameter",
            "evidence_class": "MODEL_OUTPUT",
            "mapping": "order_parameter_to_normalized_emission_intensity",
        },
        "annotations": [{"label": "Kuramoto order parameter r(t)", "evidence_class": "MODEL_OUTPUT"}],
    })

    duration = float(samples[-1]["time_seconds"])
    seed = params.get("seed", "unknown")
    return {
        "schema_version": "0.1.0",
        "scene_id": scene_id or f"kuramoto-seed-{seed}",
        "title": "Coupled Oscillators — Phase Synchronization",
        "duration_seconds": max(duration, 1.0 / float(frame_rate)),
        "frame_rate": float(frame_rate),
        "interpretation_mode": "ANALYTICAL",
        "evidence_refs": [f"simulation:kuramoto-seed-{seed}"],
        "coordinate_system": "2D_CARTESIAN",
        "units": "normalized_scene_units",
        "objects": objects,
        "audio_cues": [],
        "metadata": {
            "source_model": simulation["model"],
            "source_model_version": simulation.get("model_version"),
            "evidence_class": "MODEL_OUTPUT",
            "scientific_scope": simulation.get("scientific_scope"),
            "mapping": "x=R*cos(theta); y=R*sin(theta); coherence=r(t)",
            "simulation_parameters": params,
            "limitations": ["Analytical visualization of a generic oscillator model; not biological anatomy."],
        },
    }
