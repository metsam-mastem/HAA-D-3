"""Command-line entry point for dependency-free contract checks."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .contracts import validate_finding, validate_scene


def main() -> int:
    parser = argparse.ArgumentParser(prog="haa-d3", description="HAA-D-3 portable contract tools")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate-scene", help="validate a SceneSpec JSON file")
    validate.add_argument("path", type=Path)
    finding = sub.add_parser("validate-finding", help="validate a Finding JSON file")
    finding.add_argument("path", type=Path)
    args = parser.parse_args()

    try:
        payload = json.loads(args.path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(payload, dict):
        print("ERROR: top-level JSON value must be an object", file=sys.stderr)
        return 2

    errors = validate_scene(payload) if args.command == "validate-scene" else validate_finding(payload)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: contract semantic checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
