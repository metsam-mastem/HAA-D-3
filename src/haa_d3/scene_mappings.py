"""Explicit, renderer-neutral mappings from research outputs to SceneSpec."""
from __future__ import annotations

import hashlib
import json
import math
from typing import Any


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
    if not isinstance(nodes, int) or isinstance(nodes, bool) or nodes < 2:
        raise ValueError("simulation must contain at least two nodes")
    if not isinstance(samples, list) or not samples:
        raise ValueError("simulation must contain at least one sample")
    for name, value in (("frame_rate", frame_rate), ("orbit_radius", orbit_radius)):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be a finite positive number")
    for index, sample in enumerate(samples):
        if not isinstance(sample, dict):
            raise ValueError(f"samples[{index}] must be an object")
        phases = sample.get("phases_radians")
        if not isinstance(phases, list) or len(phases) != nodes:
            raise ValueError(f"samples[{index}] must contain one phase per oscillator")
        if "time_seconds" not in sample or "order_parameter" not in sample:
            raise ValueError(f"samples[{index}] is missing time_seconds or order_parameter")

    run_payload = json.dumps(params, sort_keys=True, separators=(",", ":"))
    run_id = hashlib.sha256(run_payload.encode("utf-8")).hexdigest()[:16]

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
        objects.append({
            "id": f"oscillator-{index:04d}",
            "type": "oscillator",
            "transform": {"position": keyframes[0]["value"], "scale": [1.0, 1.0, 1.0]},
            "geometry": {"primitive": "point"},
            "animation": [{"property": "transform.position", "keyframes": keyframes}],
            "data_binding": {
                "source_model": simulation["model"],
                "source_run_id": run_id,
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
            "source_run_id": run_id,
            "source_field": "samples[*].order_parameter",
            "evidence_class": "MODEL_OUTPUT",
            "mapping": "order_parameter_to_normalized_emission_intensity",
        },
        "annotations": [{"label": "Kuramoto order parameter r(t)", "evidence_class": "MODEL_OUTPUT"}],
    })

    duration = float(samples[-1]["time_seconds"])
    return {
        "schema_version": "0.1.0",
        "scene_id": scene_id or f"kuramoto-{run_id}",
        "title": "Coupled Oscillators — Phase Synchronization",
        "duration_seconds": max(duration, 1.0 / float(frame_rate)),
        "frame_rate": float(frame_rate),
        "interpretation_mode": "ANALYTICAL",
        "evidence_refs": [f"simulation:kuramoto:{run_id}"],
        "coordinate_system": "2D_CARTESIAN",
        "units": "normalized_scene_units",
        "objects": objects,
        "audio_cues": [],
        "metadata": {
            "source_model": simulation["model"],
            "source_model_version": simulation.get("model_version"),
            "source_run_id": run_id,
            "evidence_class": "MODEL_OUTPUT",
            "scientific_scope": simulation.get("scientific_scope"),
            "mapping": "x=R*cos(theta); y=R*sin(theta); coherence=r(t)",
            "simulation_parameters": params,
            "limitations": ["Analytical visualization of a generic oscillator model; not biological anatomy."],
        },
    }
