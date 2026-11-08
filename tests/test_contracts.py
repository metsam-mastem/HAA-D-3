import unittest
from haa_d3.contracts import validate_finding, validate_scene
from haa_d3.capabilities import AdapterDescriptor, RuntimeProfile, select_adapters

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


if __name__ == "__main__":
    unittest.main()
