"""Command-line tools for HAA-D-3 portable contracts and research prototypes."""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

from .contracts import validate_finding, validate_scene
from .kuramoto import simulate_kuramoto


def _read_json(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"file not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {exc}") from None
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(prog="haa-d3", description="HAA-D-3 portable tools")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-scene", help="validate a SceneSpec JSON file")
    validate.add_argument("path", type=Path)
    finding = sub.add_parser("validate-finding", help="validate a Finding JSON file")
    finding.add_argument("path", type=Path)

    simulation = sub.add_parser("simulate-kuramoto", help="run a seeded coupled-oscillator simulation")
    simulation.add_argument("--nodes", type=int, default=64)
    simulation.add_argument("--coupling", type=float, default=1.5)
    simulation.add_argument("--dt", type=float, default=0.02)
    simulation.add_argument("--steps", type=int, default=500)
    simulation.add_argument("--seed", type=int, default=7)
    simulation.add_argument("--omega-mean", type=float, default=1.0)
    simulation.add_argument("--omega-std", type=float, default=0.25)
    simulation.add_argument("--format", choices=("json", "csv"), default="json")
    simulation.add_argument("--output", type=Path, default=None)

    args = parser.parse_args()

    if args.command == "simulate-kuramoto":
        try:
            result = simulate_kuramoto(
                nodes=args.nodes, coupling=args.coupling, dt=args.dt,
                steps=args.steps, seed=args.seed,
                omega_mean=args.omega_mean, omega_std=args.omega_std,
            )
        except ValueError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2

        if args.format == "json":
            rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        else:
            buffer = io.StringIO()
            writer = csv.DictWriter(buffer, fieldnames=("step", "time_seconds", "order_parameter"))
            writer.writeheader()
            for sample in result["samples"]:
                writer.writerow({key: sample[key] for key in writer.fieldnames})
            rendered = buffer.getvalue()
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
            print(f"PASS: wrote {args.format.upper()} simulation output to {args.output}")
        else:
            sys.stdout.write(rendered)
        return 0

    try:
        payload = _read_json(args.path)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
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
