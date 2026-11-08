"""JSON Schema validation for portable HAA-D-3 contracts."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def _schema_path(name: str) -> Path:
    if Path(name).name != name:
        raise ValueError("schema name must be a filename, not a path")
    candidates = [
        Path(__file__).resolve().parents[2] / "schemas" / name,
        Path(sys.prefix) / "share" / "haa-d3" / "schemas" / name,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"JSON Schema not found: {name}")


def validate_json_schema(payload: dict[str, Any], schema_name: str) -> list[str]:
    """Return deterministic, path-qualified JSON Schema validation errors."""
    schema = json.loads(_schema_path(schema_name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(payload), key=lambda item: (list(map(str, item.absolute_path)), item.message)):
        location = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        errors.append(f"{location}: {error.message}")
    return errors
