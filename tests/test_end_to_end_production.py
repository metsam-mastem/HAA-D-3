import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from haa_d3.kuramoto import simulate_kuramoto
from haa_d3.scene_mappings import kuramoto_to_scene
from haa_d3.schema_validation import validate_json_schema
from haa_d3.render_svg import render_scene_frames
from haa_d3.sonification import write_sonification_midi
from haa_d3.release import build_release_bundle


class EndToEndProductionTests(unittest.TestCase):
    def setUp(self):
        self.simulation = simulate_kuramoto(nodes=4, coupling=1.2, dt=0.5, steps=2, seed=9)
        self.scene = kuramoto_to_scene(self.simulation, frame_rate=2.0)

    def test_scene_spec_is_validated_against_json_schema(self):
        self.assertEqual(validate_json_schema(self.scene, "scene-spec.schema.json"), [])
        invalid = dict(self.scene)
        invalid["unexpected"] = True
        self.assertTrue(validate_json_schema(invalid, "scene-spec.schema.json"))

    def test_svg_renderer_emits_deterministic_frame_sequence(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first"
            second = Path(directory) / "second"
            paths_a = render_scene_frames(self.scene, first, frame_rate=2)
            paths_b = render_scene_frames(self.scene, second, frame_rate=2)
            self.assertEqual(len(paths_a), 3)
            self.assertEqual([p.read_bytes() for p in paths_a], [p.read_bytes() for p in paths_b])
            self.assertIn(b"<svg", paths_a[0].read_bytes())

    def test_sonification_writes_valid_standard_midi_container(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "coherence.mid"
            metadata = write_sonification_midi(self.simulation, target)
            payload = target.read_bytes()
            self.assertEqual(payload[:4], b"MThd")
            self.assertEqual(payload[14:18], b"MTrk")
            self.assertEqual(payload[22:29], b"\x00\xff\x51\x03\x07\xa1\x20")
            self.assertGreater(metadata["event_count"], 0)
            self.assertEqual(metadata["evidence_class"], "MODEL_OUTPUT")

    def test_sonification_rejects_non_monotonic_sample_times(self):
        invalid = dict(self.simulation)
        invalid["samples"] = list(reversed(self.simulation["samples"]))
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                write_sonification_midi(invalid, Path(directory) / "invalid.mid")

    def test_release_bundle_is_byte_for_byte_reproducible(self):
        with tempfile.TemporaryDirectory() as directory:
            first = build_release_bundle(self.simulation, self.scene, Path(directory) / "first.zip")
            second = build_release_bundle(self.simulation, self.scene, Path(directory) / "second.zip")
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_blender_adapter_source_is_valid_python(self):
        adapter = Path(__file__).resolve().parents[1] / "adapters" / "blender" / "render_scene.py"
        compile(adapter.read_text(encoding="utf-8"), str(adapter), "exec")

    def test_release_bundle_contains_manifest_scene_frames_and_audio_cue(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = build_release_bundle(self.simulation, self.scene, Path(directory) / "release.zip")
            self.assertTrue(archive.is_file())
            with zipfile.ZipFile(archive) as bundle:
                names = set(bundle.namelist())
                self.assertIn("manifest.json", names)
                self.assertIn("scene.json", names)
                self.assertIn("sonification/coherence.mid", names)
                self.assertIn("frames/000000.svg", names)
                manifest = json.loads(bundle.read("manifest.json"))
                self.assertEqual(manifest["status"], "GENERATED_NOT_REVIEWED")
                self.assertIn("sha256", manifest["artifacts"]["scene.json"])


    def test_svg_renderer_rejects_excessive_pixel_budget(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "pixel budget"):
                render_scene_frames(self.scene, Path(directory), width=8192, height=8192)

    def test_svg_renderer_rejects_excessive_object_count(self):
        scene = dict(self.scene)
        scene["objects"] = self.scene["objects"] * 2000
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "object limit"):
                render_scene_frames(scene, Path(directory))


    def test_blender_adapter_preserves_unowned_scene_objects(self):
        adapter = Path(__file__).resolve().parents[1] / "adapters" / "blender" / "render_scene.py"
        source = adapter.read_text(encoding="utf-8")
        self.assertIn('obj.get("haa_d3_generated") is True', source)
        self.assertNotIn("bpy.ops.object.select_all", source)
        self.assertNotIn("bpy.ops.object.delete", source)

    def test_blender_adapter_has_render_budget_preflight(self):
        adapter = Path(__file__).resolve().parents[1] / "adapters" / "blender" / "render_scene.py"
        source = adapter.read_text(encoding="utf-8")
        self.assertIn("SceneSpec exceeds Blender render budget", source)
        self.assertIn("at most 1000 entries", source)


    def test_svg_renderer_rejects_boolean_and_non_numeric_timing(self):
        for value in (True, "24"):
            scene = dict(self.scene)
            scene["frame_rate"] = value
            with tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    render_scene_frames(scene, Path(directory))


if __name__ == "__main__":
    unittest.main()
