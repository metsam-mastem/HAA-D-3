import json, unittest
from pathlib import Path
from haa_d3.graph import validate_graph, render_svg, create_receipt

FIXTURE=Path(__file__).parents[1]/"data"/"knowledge-graph.json"
class GraphSliceTests(unittest.TestCase):
    def setUp(self): self.graph=json.loads(FIXTURE.read_text(encoding="utf-8"))
    def test_fixture_valid(self): self.assertEqual(validate_graph(self.graph),[])
    def test_dangling_relation_rejected(self):
        g=dict(self.graph); g["relations"]=self.graph["relations"]+[{"source":"missing","target":"math.graph","type":"bad"}]
        self.assertTrue(any("unknown" in e for e in validate_graph(g)))
    def test_duplicate_id_rejected(self):
        g=dict(self.graph); g["concepts"]=self.graph["concepts"]+[dict(self.graph["concepts"][0])]
        self.assertTrue(any("duplicate" in e for e in validate_graph(g)))
    def test_svg_contains_labels(self):
        svg=render_svg(self.graph); self.assertIn("<title>",svg); self.assertIn("Spatial Embedding",svg); self.assertIn("Feedback Learning",svg)
    def test_receipt_hashes(self):
        r=create_receipt(self.graph,render_svg(self.graph)); self.assertEqual(len(r["input_sha256"]),64); self.assertEqual(len(r["output_svg_sha256"]),64)
    def test_deterministic(self): self.assertEqual(render_svg(self.graph),render_svg(self.graph))
if __name__=="__main__": unittest.main()
