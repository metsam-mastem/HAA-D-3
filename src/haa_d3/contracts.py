"""Small dependency-free semantic validators for core HAA-D-3 contracts.

JSON Schema files remain the canonical machine-readable contract. These helpers
provide useful validation without requiring a third-party package at runtime.
"""
from __future__ import annotations

from typing import Any

EVIDENCE_CLASSES = {
    "OBSERVED", "REPRODUCED", "MODEL_OUTPUT", "HYPOTHESIS",
    "INTERPRETATION", "METAPHOR", "UNKNOWN",
}
INTERPRETATION_MODES = {"LITERAL", "ANALYTICAL", "EXPLANATORY", "METAPHORICAL"}


def validate_finding(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ("id", "statement", "evidence_class", "source_ids", "limitations")
    for key in required:
        if key not in value:
            errors.append(f"missing required field: {key}")
    if not isinstance(value.get("id"), str) or not value.get("id", "").strip():
        errors.append("id must be a non-empty string")
    if not isinstance(value.get("statement"), str) or not value.get("statement", "").strip():
        errors.append("statement must be a non-empty string")
    if value.get("evidence_class") not in EVIDENCE_CLASSES:
        errors.append("evidence_class is not a supported evidence class")
    if not isinstance(value.get("source_ids"), list) or not all(isinstance(x, str) for x in value.get("source_ids", [])):
        errors.append("source_ids must be an array of strings")
    if not isinstance(value.get("limitations"), list) or not all(isinstance(x, str) for x in value.get("limitations", [])):
        errors.append("limitations must be an array of strings")
    return errors


def validate_scene(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = (
        "schema_version", "scene_id", "title", "duration_seconds",
        "frame_rate", "interpretation_mode", "evidence_refs", "objects",
    )
    for key in required:
        if key not in value:
            errors.append(f"missing required field: {key}")
    if value.get("schema_version") != "0.1.0":
        errors.append("schema_version must be 0.1.0")
    for key in ("scene_id", "title"):
        if not isinstance(value.get(key), str) or not value.get(key, "").strip():
            errors.append(f"{key} must be a non-empty string")
    for key in ("duration_seconds", "frame_rate"):
        number = value.get(key)
        if isinstance(number, bool) or not isinstance(number, (int, float)) or number <= 0:
            errors.append(f"{key} must be a positive number")
    if value.get("interpretation_mode") not in INTERPRETATION_MODES:
        errors.append("interpretation_mode is not supported")
    refs = value.get("evidence_refs")
    if not isinstance(refs, list) or not all(isinstance(x, str) for x in refs):
        errors.append("evidence_refs must be an array of strings")
    objects = value.get("objects")
    if not isinstance(objects, list):
        errors.append("objects must be an array")
    else:
        seen: set[str] = set()
        for index, obj in enumerate(objects):
            if not isinstance(obj, dict):
                errors.append(f"objects[{index}] must be an object")
                continue
            for key in ("id", "type"):
                if not isinstance(obj.get(key), str) or not obj.get(key, "").strip():
                    errors.append(f"objects[{index}].{key} must be a non-empty string")
            object_id = obj.get("id")
            if isinstance(object_id, str) and object_id in seen:
                errors.append(f"duplicate object id: {object_id}")
            elif isinstance(object_id, str):
                seen.add(object_id)
    return errors
