import unittest
from haa_d3.contracts import validate_finding, validate_scene

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

if __name__ == "__main__":
    unittest.main()
