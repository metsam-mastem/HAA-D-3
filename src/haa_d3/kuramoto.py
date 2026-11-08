"""Deterministic Kuramoto coupled-oscillator simulation (research prototype)."""
from __future__ import annotations

import math
import random
from typing import Any

TAU = 2.0 * math.pi


def _derivative(phases: list[float], frequencies: list[float], coupling: float) -> list[float]:
    count = len(phases)
    mean_sin = sum(math.sin(value) for value in phases) / count
    mean_cos = sum(math.cos(value) for value in phases) / count
    return [
        omega + coupling * (mean_sin * math.cos(theta) - mean_cos * math.sin(theta))
        for theta, omega in zip(phases, frequencies)
    ]


def order_parameter(phases: list[float]) -> float:
    """Return Kuramoto order parameter r in [0, 1] (up to float tolerance)."""
    if not phases:
        raise ValueError("phases must not be empty")
    real = sum(math.cos(value) for value in phases) / len(phases)
    imag = sum(math.sin(value) for value in phases) / len(phases)
    return math.hypot(real, imag)


def simulate_kuramoto(
    *,
    nodes: int = 64,
    coupling: float = 1.5,
    dt: float = 0.02,
    steps: int = 500,
    seed: int = 7,
    omega_mean: float = 1.0,
    omega_std: float = 0.25,
) -> dict[str, Any]:
    """Run a seeded Heun/RK2 simulation and return full phase snapshots.

    This is a generic coupled-oscillator model, not a biological neural model.
    """
    if isinstance(nodes, bool) or not isinstance(nodes, int) or nodes < 2:
        raise ValueError("nodes must be an integer >= 2")
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 1:
        raise ValueError("steps must be an integer >= 1")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    for name, value in (("coupling", coupling), ("dt", dt), ("omega_mean", omega_mean), ("omega_std", omega_std)):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(f"{name} must be a finite number")
    if dt <= 0:
        raise ValueError("dt must be > 0")
    if omega_std < 0:
        raise ValueError("omega_std must be >= 0")

    rng = random.Random(seed)
    phases = [rng.uniform(-math.pi, math.pi) for _ in range(nodes)]
    frequencies = [rng.gauss(omega_mean, omega_std) for _ in range(nodes)]
    samples: list[dict[str, Any]] = []

    for step in range(steps + 1):
        samples.append({
            "step": step,
            "time_seconds": round(step * dt, 10),
            "order_parameter": order_parameter(phases),
            "phases_radians": [round(value, 12) for value in phases],
        })
        if step == steps:
            break
        k1 = _derivative(phases, frequencies, float(coupling))
        predictor = [(theta + dt * slope) % TAU for theta, slope in zip(phases, k1)]
        k2 = _derivative(predictor, frequencies, float(coupling))
        phases = [
            (theta + 0.5 * dt * (slope1 + slope2)) % TAU
            for theta, slope1, slope2 in zip(phases, k1, k2)
        ]

    return {
        "model": "kuramoto_mean_field",
        "model_version": "0.1.0",
        "integration_method": "Heun_RK2",
        "evidence_class": "MODEL_OUTPUT",
        "scientific_scope": "generic coupled oscillators; not a biological brain model",
        "parameters": {
            "nodes": nodes,
            "coupling": float(coupling),
            "dt_seconds": float(dt),
            "steps": steps,
            "seed": seed,
            "omega_mean_rad_per_second": float(omega_mean),
            "omega_std_rad_per_second": float(omega_std),
        },
        "samples": samples,
    }
