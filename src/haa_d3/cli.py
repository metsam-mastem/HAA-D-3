"""Command-line tools for HAA-D-3 portable contracts and research prototypes."""
from __future__ import annotations
import argparse, csv, io, json, sys
from pathlib import Path
from .contracts import validate_finding, validate_scene
from .schema_validation import validate_json_schema
from .render_svg import render_scene_frames
from .release import build_release_bundle
from .kuramoto import simulate_kuramoto
from .scene_mappings import kuramoto_to_scene
from .knowledge_graph import create_receipt, render_svg, validate_graph


def _unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def _reject_json_constant(value: str):
    raise ValueError(f"non-standard JSON numeric constant: {value}")


def _read_json(path: Path) -> dict:
    try:
        payload = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
            parse_constant=_reject_json_constant,
        )
    except FileNotFoundError:
        raise ValueError(f"file not found: {path}") from None
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"invalid JSON: {exc}") from None
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(prog="haa-d3", description="HAA-D-3 portable tools")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate-scene", help="validate a SceneSpec JSON file"); validate.add_argument("path", type=Path)
    finding = sub.add_parser("validate-finding", help="validate a Finding JSON file"); finding.add_argument("path", type=Path)
    render = sub.add_parser("render-scene", help="render a SceneSpec as deterministic SVG frames"); render.add_argument("path", type=Path); render.add_argument("--out", type=Path, default=Path("artifacts/frames")); render.add_argument("--frame-rate", type=float, default=None)
    release = sub.add_parser("build-release", help="build simulation, SceneSpec, SVG and MIDI release bundle")
    release.add_argument("--video", action="store_true", help="render MP4 preview; requires ffmpeg and haa-d3[media]")
    release.add_argument("--nodes", type=int, default=24); release.add_argument("--coupling", type=float, default=1.5); release.add_argument("--dt", type=float, default=0.05); release.add_argument("--steps", type=int, default=100); release.add_argument("--seed", type=int, default=7); release.add_argument("--frame-rate", type=float, default=24.0); release.add_argument("--output", type=Path, default=Path("artifacts/haa-d3-release.zip"))
    graph = sub.add_parser("render-knowledge-graph", help="validate graph JSON and generate SVG plus provenance receipt")
    graph.add_argument("path", type=Path); graph.add_argument("--out", type=Path, default=Path("artifacts/knowledge-graph"))
    simulation = sub.add_parser("simulate-kuramoto", help="run a seeded coupled-oscillator simulation")
    for command in (simulation,):
        command.add_argument("--nodes", type=int, default=64); command.add_argument("--coupling", type=float, default=1.5)
        command.add_argument("--dt", type=float, default=0.02); command.add_argument("--steps", type=int, default=500)
        command.add_argument("--seed", type=int, default=7); command.add_argument("--omega-mean", type=float, default=1.0)
        command.add_argument("--omega-std", type=float, default=0.25); command.add_argument("--format", choices=("json", "csv"), default="json")
        command.add_argument("--output", type=Path, default=None)
    scene = sub.add_parser("kuramoto-scene", help="run Kuramoto and compile an analytical SceneSpec")
    scene.add_argument("--nodes", type=int, default=64); scene.add_argument("--coupling", type=float, default=1.5)
    scene.add_argument("--dt", type=float, default=0.02); scene.add_argument("--steps", type=int, default=250)
    scene.add_argument("--seed", type=int, default=7); scene.add_argument("--omega-mean", type=float, default=1.0)
    scene.add_argument("--omega-std", type=float, default=0.25); scene.add_argument("--frame-rate", type=float, default=24.0)
    scene.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    if args.command == "render-scene":
        try:
            payload = _read_json(args.path)
            errors = validate_json_schema(payload, "scene-spec.schema.json") + validate_scene(payload)
            if errors:
                for error in errors: print(f"FAIL: {error}")
                return 1
            frames = render_scene_frames(payload, args.out, frame_rate=args.frame_rate)
        except (ValueError, OSError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr); return 2
        print(json.dumps({"status":"PASS","frame_count":len(frames),"output":str(args.out)}, indent=2))
        return 0

    if args.command == "build-release":
        try:
            simulation = simulate_kuramoto(nodes=args.nodes, coupling=args.coupling, dt=args.dt, steps=args.steps, seed=args.seed)
            scene_payload = kuramoto_to_scene(simulation, frame_rate=args.frame_rate)
            errors = validate_json_schema(scene_payload, "scene-spec.schema.json") + validate_scene(scene_payload)
            if errors:
                for error in errors: print(f"FAIL: {error}")
                return 1
            archive = build_release_bundle(simulation, scene_payload, args.output, include_video=args.video)
        except (ValueError, OSError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr); return 2
        print(json.dumps({"status":"GENERATED_NOT_REVIEWED","release_bundle":str(archive)}, indent=2))
        return 0

    if args.command == "render-knowledge-graph":
        try:
            payload = _read_json(args.path); errors = validate_graph(payload)
            if errors:
                for error in errors: print(f"FAIL: {error}")
                return 1
            svg = render_svg(payload); receipt = create_receipt(payload, svg)
        except (ValueError, OSError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr); return 2
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "graph.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (args.out / "graph.svg").write_text(svg, encoding="utf-8")
        (args.out / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status":"PASS","output":str(args.out),"receipt":receipt}, ensure_ascii=False, indent=2))
        return 0

    if args.command in ("simulate-kuramoto", "kuramoto-scene"):
        try:
            result = simulate_kuramoto(nodes=args.nodes, coupling=args.coupling, dt=args.dt, steps=args.steps, seed=args.seed, omega_mean=args.omega_mean, omega_std=args.omega_std)
            if args.command == "kuramoto-scene": result = kuramoto_to_scene(result, frame_rate=args.frame_rate)
        except ValueError as exc:
            print(f"ERROR: {exc}", file=sys.stderr); return 2
        output_kind = "SCENE" if args.command == "kuramoto-scene" else args.format.upper()
        if args.command == "kuramoto-scene" or args.format == "json":
            rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        else:
            buffer = io.StringIO(); writer = csv.DictWriter(buffer, fieldnames=("step", "time_seconds", "order_parameter")); writer.writeheader()
            for sample in result["samples"]: writer.writerow({key: sample[key] for key in writer.fieldnames})
            rendered = buffer.getvalue()
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(rendered, encoding="utf-8")
            print(f"PASS: wrote {output_kind} output to {args.output}")
        else: sys.stdout.write(rendered)
        return 0

    try: payload = _read_json(args.path)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr); return 2
    schema_name = "scene-spec.schema.json" if args.command == "validate-scene" else "finding.schema.json"
    errors = validate_json_schema(payload, schema_name)
    errors += validate_scene(payload) if args.command == "validate-scene" else validate_finding(payload)
    if errors:
        for error in errors: print(f"FAIL: {error}")
        return 1
    print("PASS: contract semantic checks"); return 0


if __name__ == "__main__":
    raise SystemExit(main())
