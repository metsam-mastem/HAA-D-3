"""Blender background renderer for HAA-D-3 SceneSpec JSON.

Usage:
  blender --background --python adapters/blender/render_scene.py -- \
    --scene examples/scenes/synthetic-emergence.scene.json --output artifacts/blender

This adapter is optional and requires Blender's bundled Python/bpy runtime.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import bpy


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args(argv)


def interpolate(keyframes, timestamp):
    ordered = sorted(keyframes, key=lambda item: float(item["time_seconds"]))
    if timestamp <= float(ordered[0]["time_seconds"]):
        return ordered[0]["value"]
    if timestamp >= float(ordered[-1]["time_seconds"]):
        return ordered[-1]["value"]
    for left, right in zip(ordered, ordered[1:]):
        a, b = float(left["time_seconds"]), float(right["time_seconds"])
        if a <= timestamp <= b:
            ratio = (timestamp - a) / (b - a)
            lv, rv = left["value"], right["value"]
            if isinstance(lv, list):
                return [float(x) + (float(y) - float(x)) * ratio for x, y in zip(lv, rv)]
            return float(lv) + (float(rv) - float(lv)) * ratio
    return ordered[-1]["value"]


def clear_scene():
    """Remove only objects created by this adapter; preserve user scene content."""
    scene = bpy.context.scene
    active_camera = scene.camera
    if active_camera is not None and active_camera.get("haa_d3_generated") is True:
        scene.camera = None
    for obj in list(bpy.data.objects):
        if obj.get("haa_d3_generated") is True:
            bpy.data.objects.remove(obj, do_unlink=True)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        for block in list(datablocks):
            if block.users == 0 and block.get("haa_d3_generated") is True:
                datablocks.remove(block)


def make_material(name, color, emission=0.0):
    material = bpy.data.materials.new(name)
    material["haa_d3_generated"] = True
    material.diffuse_color = (*color, 1.0)
    material.use_nodes = True
    principled = material.node_tree.nodes.get("Principled BSDF")
    principled.inputs["Base Color"].default_value = (*color, 1.0)
    principled.inputs["Emission Color"].default_value = (*color, 1.0)
    principled.inputs["Emission Strength"].default_value = emission
    return material


def add_camera_and_light():
    bpy.ops.object.camera_add(location=(0.0, -0.2, 8.5))
    camera = bpy.context.object
    camera.name = "HAA-D3-Camera"
    camera["haa_d3_generated"] = True
    camera.data["haa_d3_generated"] = True
    camera.data.lens = 50
    camera.rotation_euler = (0.0, 0.0, 0.0)
    bpy.context.scene.camera = camera
    bpy.ops.object.light_add(type="AREA", location=(0.0, -2.0, 5.0))
    light = bpy.context.object
    light.name = "HAA-D3-Key-Light"
    light["haa_d3_generated"] = True
    light.data["haa_d3_generated"] = True
    light.data.energy = 1200
    light.data.shape = "DISK"
    light.data.size = 8


def build_scene(spec, output_dir):
    if not isinstance(spec, dict):
        raise ValueError("SceneSpec must be a JSON object")
    required = ("scene_id", "frame_rate", "duration_seconds", "objects")
    missing = [key for key in required if key not in spec]
    if missing:
        raise ValueError("SceneSpec missing required fields: " + ", ".join(missing))
    fps = spec["frame_rate"]
    duration = spec["duration_seconds"]
    if isinstance(fps, bool) or not isinstance(fps, (int, float)) or not math.isfinite(fps) or fps <= 0:
        raise ValueError("frame_rate must be finite and positive")
    if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not math.isfinite(duration) or duration <= 0:
        raise ValueError("duration_seconds must be finite and positive")
    if fps > 120 or duration > 600 or fps * duration > 10000:
        raise ValueError("SceneSpec exceeds Blender render budget")
    if not isinstance(spec["objects"], list) or len(spec["objects"]) > 1000:
        raise ValueError("SceneSpec objects must be an array with at most 1000 entries")
    seen_ids = set()
    for index, item in enumerate(spec["objects"]):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"].strip():
            raise ValueError(f"objects[{index}] must have a non-empty string id")
        if item["id"] in seen_ids:
            raise ValueError(f"duplicate object id: {item['id']}")
        seen_ids.add(item["id"])
        if item.get("type") not in {"oscillator", "metric"}:
            raise ValueError(f"objects[{index}] has unsupported type")
    clear_scene()
    scene = bpy.context.scene
    fps = float(spec["frame_rate"])
    duration = float(spec["duration_seconds"])
    scene.render.fps = round(fps)
    scene.frame_start = 1
    scene.frame_end = max(1, round(duration * fps) + 1)
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.world.color = (0.005, 0.012, 0.025)
    cyan = make_material("HAA-D3-Cyan", (0.08, 0.72, 0.82), 1.2)
    amber = make_material("HAA-D3-Amber", (1.0, 0.52, 0.12), 0.8)
    for item in spec.get("objects", []):
        if item.get("type") == "oscillator":
            bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=0.075)
            obj = bpy.context.object
            obj.name = item["id"]
            obj["haa_d3_generated"] = True
            obj.data["haa_d3_generated"] = True
            obj.data.materials.append(cyan)
            track = next((x for x in item.get("animation", []) if x.get("property") == "transform.position"), None)
            if track:
                for key in track.get("keyframes", []):
                    frame = round(float(key["time_seconds"]) * fps) + 1
                    obj.location = tuple(key["value"])
                    obj.keyframe_insert(data_path="location", frame=frame)
            else:
                obj.location = tuple(item.get("transform", {}).get("position", [0, 0, 0]))
        elif item.get("type") == "metric":
            bpy.ops.mesh.primitive_torus_add(major_radius=0.45, minor_radius=0.012, major_segments=96, minor_segments=8)
            obj = bpy.context.object
            obj.name = item["id"]
            obj["haa_d3_generated"] = True
            obj.data["haa_d3_generated"] = True
            obj.data.materials.append(amber)
            track = next((x for x in item.get("animation", []) if x.get("property") == "material.emission_intensity"), None)
            if track:
                for key in track.get("keyframes", []):
                    frame = round(float(key["time_seconds"]) * fps) + 1
                    strength = max(0.05, min(1.0, float(key["value"])))
                    obj.scale = (0.6 + strength, 0.6 + strength, 0.6 + strength)
                    obj.keyframe_insert(data_path="scale", frame=frame)
    add_camera_and_light()
    output_dir.mkdir(parents=True, exist_ok=True)
    scene.render.filepath = str((output_dir / "frame_").resolve())
    scene.render.use_file_extension = True
    bpy.ops.wm.save_as_mainfile(filepath=str((output_dir / "scene.blend").resolve()))
    bpy.ops.render.render(animation=True)
    manifest = {
        "status": "RENDERED_NOT_REVIEWED",
        "scene_id": spec["scene_id"],
        "blender_version": bpy.app.version_string,
        "frame_start": scene.frame_start,
        "frame_end": scene.frame_end,
        "fps": scene.render.fps,
        "resolution": [scene.render.resolution_x, scene.render.resolution_y],
        "evidence_class": spec.get("metadata", {}).get("evidence_class", "UNKNOWN"),
        "scientific_scope": spec.get("metadata", {}).get("scientific_scope"),
        "limitations": ["Renderer output requires scientific, creative, accessibility and rights review."],
    }
    (output_dir / "render-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    arguments = parse_args()
    payload = json.loads(arguments.scene.read_text(encoding="utf-8"))
    build_scene(payload, arguments.output)
