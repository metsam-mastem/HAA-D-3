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
        scene["objects"] = [dict(obj, id=f"safe-{index}") for index, obj in enumerate(self.scene["objects"] * 201)]
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


    def test_blender_clear_scene_removes_only_tagged_objects(self):
        import importlib.util
        import sys
        from types import SimpleNamespace
        from unittest.mock import patch

        class FakeID(dict):
            def __init__(self, *args, users=0, **kwargs):
                super().__init__(*args, **kwargs)
                self.users = users

        class FakeCollection(list):
            def remove(self, item, **kwargs):
                super().remove(item)

        owned = FakeID(haa_d3_generated=True)
        user_object = FakeID(name="user-object")
        generated_camera = FakeID(haa_d3_generated=True)
        user_mesh = FakeID(name="user-mesh", users=0)
        generated_mesh = FakeID(haa_d3_generated=True, users=0)
        fake_bpy = SimpleNamespace(
            context=SimpleNamespace(scene=SimpleNamespace(camera=generated_camera)),
            data=SimpleNamespace(
                objects=FakeCollection([owned, user_object, generated_camera]),
                meshes=FakeCollection([user_mesh, generated_mesh]),
                curves=FakeCollection(), materials=FakeCollection(),
                cameras=FakeCollection(), lights=FakeCollection(),
            ),
        )
        adapter_path = Path(__file__).resolve().parents[1] / "adapters" / "blender" / "render_scene.py"
        spec = importlib.util.spec_from_file_location("haa_d3_blender_adapter_test", adapter_path)
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"bpy": fake_bpy}):
            spec.loader.exec_module(module)
            module.clear_scene()
        self.assertEqual(fake_bpy.data.objects, [user_object])
        self.assertEqual(fake_bpy.data.meshes, [user_mesh])
        self.assertIsNone(fake_bpy.context.scene.camera)

    def test_blender_preflight_rejects_bad_fps_before_scene_mutation(self):
        import importlib.util
        import sys
        from types import SimpleNamespace
        from unittest.mock import patch

        fake_bpy = SimpleNamespace()
        adapter_path = Path(__file__).resolve().parents[1] / "adapters" / "blender" / "render_scene.py"
        spec = importlib.util.spec_from_file_location("haa_d3_blender_preflight_test", adapter_path)
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"bpy": fake_bpy}):
            spec.loader.exec_module(module)
            with self.assertRaisesRegex(ValueError, "frame_rate"):
                module.build_scene({"scene_id":"bad","frame_rate":True,"duration_seconds":1,"objects":[]}, Path("/tmp/unused"))


    def test_blender_adapter_refuses_to_overwrite_existing_outputs_by_default(self):
        import importlib.util
        import sys
        import tempfile
        from types import SimpleNamespace
        from unittest.mock import patch

        adapter_path = Path(__file__).resolve().parents[1] / "adapters" / "blender" / "render_scene.py"
        spec = importlib.util.spec_from_file_location("haa_d3_blender_overwrite_test", adapter_path)
        module = importlib.util.module_from_spec(spec)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "render"
            output.mkdir()
            (output / "scene.blend").write_bytes(b"preserve")
            with patch.dict(sys.modules, {"bpy": SimpleNamespace()}):
                spec.loader.exec_module(module)
                with self.assertRaisesRegex(FileExistsError, "already contains HAA-D-3 outputs"):
                    module.build_scene({"scene_id":"demo","frame_rate":24,"duration_seconds":1,"objects":[]}, output)
            self.assertEqual((output / "scene.blend").read_bytes(), b"preserve")


    def test_blender_adapter_selects_available_eevee_engine(self):
        import importlib.util
        import sys
        from types import SimpleNamespace
        from unittest.mock import patch

        adapter_path = Path(__file__).resolve().parents[1] / "adapters" / "blender" / "render_scene.py"
        spec = importlib.util.spec_from_file_location("haa_d3_blender_engine_test", adapter_path)
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"bpy": SimpleNamespace()}):
            spec.loader.exec_module(module)
        self.assertEqual(module.eevee_engine_for_version((4, 0, 0)), "BLENDER_EEVEE")
        self.assertEqual(module.eevee_engine_for_version((4, 2, 0)), "BLENDER_EEVEE_NEXT")


if __name__ == "__main__":
    unittest.main()
