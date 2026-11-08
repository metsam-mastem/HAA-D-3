"""Create a MIDI data-sonification cue from Kuramoto order-parameter samples."""
from __future__ import annotations

import math
from pathlib import Path
from typing import Any


def _variable_length(value: int) -> bytes:
    if value < 0 or value > 0x0FFFFFFF:
        raise ValueError("MIDI delta time must be between 0 and 0x0FFFFFFF ticks")
    buffer = value & 0x7F
    result = bytearray()
    while value >> 7:
        value >>= 7
        buffer <<= 8
        buffer |= ((value & 0x7F) | 0x80)
    while True:
        result.append(buffer & 0xFF)
        if buffer & 0x80:
            buffer >>= 8
        else:
            break
    return bytes(result)


def write_sonification_midi(simulation: dict[str, Any], output_path: Path) -> dict[str, Any]:
    """Map r(t) to pitch/velocity. This is sonification, not a composed score."""
    if simulation.get("model") != "kuramoto_mean_field":
        raise ValueError("simulation must be a Kuramoto mean-field output")
    samples = simulation.get("samples")
    if not isinstance(samples, list) or len(samples) < 2:
        raise ValueError("simulation must contain at least two samples")

    normalized = []
    previous_time = None
    for sample in samples:
        time_value = float(sample["time_seconds"])
        coherence = float(sample["order_parameter"])
        if not math.isfinite(time_value) or time_value < 0:
            raise ValueError("sample times must be finite and non-negative")
        if previous_time is not None and time_value <= previous_time:
            raise ValueError("sample times must be strictly increasing")
        if not math.isfinite(coherence) or not 0 <= coherence <= 1.0000001:
            raise ValueError("order_parameter must be in [0, 1]")
        normalized.append((time_value, coherence))
        previous_time = time_value

    ticks_per_second = 960  # 120 BPM, 480 ticks per quarter note
    events = []
    for index, (time_value, coherence) in enumerate(normalized):
        tick = round(time_value * ticks_per_second)
        if index + 1 < len(normalized):
            interval = normalized[index + 1][0] - time_value
        else:
            interval = time_value - normalized[index - 1][0]
        duration = max(1, round(min(0.08, interval * 0.8) * ticks_per_second))
        pitch = max(48, min(84, 48 + round(coherence * 36)))
        velocity = max(1, min(127, 32 + round(coherence * 88)))
        events.append((tick, bytes((0x90, pitch, velocity))))
        events.append((tick + duration, bytes((0x80, pitch, 0))))

    events.sort(key=lambda item: (item[0], 0 if item[1][0] == 0x80 else 1))
    track = bytearray()
    # Explicit 120 BPM tempo and 4/4 meter; do not rely on MIDI player defaults.
    track.extend(b"\x00\xff\x51\x03\x07\xa1\x20")
    track.extend(b"\x00\xff\x58\x04\x04\x02\x18\x08")
    previous_tick = 0
    for tick, message in events:
        track.extend(_variable_length(tick - previous_tick))
        track.extend(message)
        previous_tick = tick
    track.extend(b"\x00\xff\x2f\x00")
    header = (
        b"MThd" + (6).to_bytes(4, "big") + (0).to_bytes(2, "big")
        + (1).to_bytes(2, "big") + (480).to_bytes(2, "big")
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(header + b"MTrk" + len(track).to_bytes(4, "big") + track)
    return {
        "format": "Standard MIDI File Type 0",
        "tempo_bpm": 120,
        "meter": "4/4",
        "event_count": len(events),
        "mapping": "order_parameter -> pitch and velocity",
        "evidence_class": "MODEL_OUTPUT",
        "interpretation": "data sonification; not a composed soundtrack",
        "output": "sonification/coherence.mid",
    }
