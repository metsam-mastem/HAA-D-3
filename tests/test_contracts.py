import unittest
from haa_d3.contracts import validate_finding, validate_scene
from haa_d3.capabilities import AdapterDescriptor, RuntimeProfile, select_adapters
from haa_d3.kuramoto import simulate_kuramoto, order_parameter
from haa_d3.scene_mappings import kuramoto_to_scene

class ContractTests(unittest.TestCase):
    def scene(self):
        return {"schema_version":"0.1.0","scene_id":"demo-001","title":"Synthetic emergence","duration_seconds":12,"frame_rate":24,"interpretation_mode":"METAPHORICAL","evidence_refs":["finding-demo"],"objects":[{"id":"node-1","type":"point"}]}
    def test_valid_scene(self):
        self.assertEqual(validate_scene(self.scene()), [])
    def test_duplicate_scene_object_ids(self):
        s=self.scene(); s["objects"].append({"id":"node-1","type":"point"})
        self.assertTrue(any("duplicate object id" in e for e in validate_scene(s)))
    def test_invalid_duration(self):
        s=self.scene(); s["duration_seconds"]=0
        self.assertTrue(any("duration_seconds" in e for e in validate_scene(s)))
    def test_missing_scene_field(self):
        s=self.scene(); del s["evidence_refs"]
        self.assertTrue(any("evidence_refs" in e for e in validate_scene(s)))
    def test_valid_finding(self):
        f={"id":"f-1","statement":"Synthetic demo generated.","evidence_class":"METAPHOR","source_ids":[],"limitations":["Not empirical data."]}
        self.assertEqual(validate_finding(f), [])
    def test_invalid_evidence_class(self):
        f={"id":"f-1","statement":"Claim","evidence_class":"PROVEN","source_ids":[],"limitations":[]}
        self.assertTrue(any("evidence_class" in e for e in validate_finding(f)))

class AdapterSelectionTests(unittest.TestCase):
    def test_selects_offline_platform_compatible_adapter(self):
        items = [
            AdapterDescriptor("cloud-renderer", "1", ("render",), platforms=("any",), offline=False),
            AdapterDescriptor("local-renderer", "1", ("render",), platforms=("linux",), offline=True),
            AdapterDescriptor("windows-only", "1", ("render",), platforms=("windows",), offline=True),
        ]
        selected = select_adapters(items, "render", RuntimeProfile("linux", offline_required=True))
        self.assertEqual([item.adapter_id for item in selected], ["local-renderer"])

    def test_gpu_requirement_is_respected(self):
        item = AdapterDescriptor("gpu-adapter", "1", ("simulate",), requires_gpu=True)
        self.assertEqual(select_adapters([item], "simulate", RuntimeProfile("linux")), [])

    def test_selection_order_is_deterministic(self):
        items = [AdapterDescriptor("z-adapter", "1", ("render",)), AdapterDescriptor("a-adapter", "1", ("render",))]
        selected = select_adapters(items, "render", RuntimeProfile("linux"))
        self.assertEqual([item.adapter_id for item in selected], ["a-adapter", "z-adapter"])



class KuramotoSimulationTests(unittest.TestCase):
    def test_fixed_seed_is_deterministic(self):
        a = simulate_kuramoto(nodes=8, steps=5, seed=19)
        b = simulate_kuramoto(nodes=8, steps=5, seed=19)
        self.assertEqual(a, b)

    def test_sample_count_and_order_parameter_bounds(self):
        result = simulate_kuramoto(nodes=12, steps=7, seed=3)
        self.assertEqual(len(result["samples"]), 8)
        for sample in result["samples"]:
            self.assertGreaterEqual(sample["order_parameter"], 0.0)
            self.assertLessEqual(sample["order_parameter"], 1.0 + 1e-12)

    def test_invalid_inputs_are_rejected(self):
        for kwargs in ({"nodes": 1}, {"steps": 0}, {"dt": 0}, {"omega_std": -1}):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    simulate_kuramoto(**kwargs)

    def test_order_parameter_for_identical_phases_is_one(self):
        self.assertAlmostEqual(order_parameter([0.3, 0.3, 0.3]), 1.0, places=12)

    def test_kuramoto_scene_mapping_preserves_provenance_and_shape(self):
        simulation = simulate_kuramoto(nodes=5, steps=3, seed=4)
        scene = kuramoto_to_scene(simulation)
        self.assertEqual(scene["interpretation_mode"], "ANALYTICAL")
        self.assertEqual(scene["metadata"]["evidence_class"], "MODEL_OUTPUT")
        self.assertEqual(len(scene["objects"]), 6)
        self.assertEqual(len(scene["objects"][0]["animation"][0]["keyframes"]), 4)
        self.assertTrue(any(obj["id"] == "global-coherence" for obj in scene["objects"]))
        self.assertTrue(scene["metadata"]["source_run_id"])
        self.assertEqual(scene["evidence_refs"][0], "simulation:kuramoto:" + scene["metadata"]["source_run_id"])

    def test_different_parameters_produce_different_scene_identity(self):
        a = kuramoto_to_scene(simulate_kuramoto(nodes=4, steps=2, seed=2, coupling=1.0))
        b = kuramoto_to_scene(simulate_kuramoto(nodes=4, steps=2, seed=2, coupling=2.0))
        self.assertNotEqual(a["scene_id"], b["scene_id"])


    def test_rejects_non_finite_scene_numbers_and_booleans(self):
        for value in (float("nan"), float("inf"), True):
            with self.subTest(value=value):
                scene = {"schema_version":"0.1.0","scene_id":"demo","title":"Demo","duration_seconds":value,"frame_rate":24,"interpretation_mode":"METAPHORICAL","evidence_refs":[],"objects":[]}
                self.assertTrue(any("duration_seconds" in error for error in validate_scene(scene)))


if __name__ == "__main__":
    unittest.main()
