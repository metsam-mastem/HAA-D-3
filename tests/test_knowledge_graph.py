import json
import unittest
from pathlib import Path
from haa_d3.knowledge_graph import create_receipt, render_svg, validate_graph

FIXTURE = Path(__file__).parents[1] / "examples" / "knowledge" / "seed-graph.json"


class KnowledgeGraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_seed_graph_is_valid(self):
        self.assertEqual(validate_graph(self.graph), [])

    def test_rejects_duplicate_node_ids(self):
        graph = dict(self.graph)
        graph["concepts"] = self.graph["concepts"] + [dict(self.graph["concepts"][0])]
        self.assertTrue(any("duplicate" in error for error in validate_graph(graph)))

    def test_rejects_dangling_relations(self):
        graph = dict(self.graph)
        graph["relations"] = self.graph["relations"] + [{"source":"missing","target":"math.graph","type":"invalid"}]
        self.assertTrue(any("unknown" in error for error in validate_graph(graph)))

    def test_rejects_non_finite_coordinates(self):
        graph = dict(self.graph)
        graph["concepts"] = [dict(node) for node in self.graph["concepts"]]
        graph["concepts"][0]["x"] = float("nan")
        self.assertTrue(any("finite numeric" in error for error in validate_graph(graph)))

    def test_svg_is_deterministic_and_escapes_labels(self):
        graph = dict(self.graph); graph["title"] = "HAA-D-3 <Graph>"
        first = render_svg(graph)
        self.assertEqual(first, render_svg(graph))
        self.assertIn("HAA-D-3 &lt;Graph&gt;", first)

    def test_receipt_binds_input_and_output_hashes(self):
        svg = render_svg(self.graph); receipt = create_receipt(self.graph, svg)
        self.assertEqual(len(receipt["input_sha256"]), 64)
        self.assertEqual(len(receipt["output_svg_sha256"]), 64)
        self.assertEqual(receipt["concept_count"], len(self.graph["concepts"]))
        self.assertEqual(receipt["relation_count"], len(self.graph["relations"]))
        self.assertEqual(receipt["scientific_validation"], "NOT_RUN")


    def test_rejects_non_string_relation_endpoints_without_crashing(self):
        for endpoint in (["math.graph"], {"id": "math.graph"}, 7):
            with self.subTest(endpoint=endpoint):
                graph = dict(self.graph)
                graph["relations"] = [dict(self.graph["relations"][0], source=endpoint)]
                errors = validate_graph(graph)
                self.assertTrue(any("source" in error and "string" in error for error in errors))

    def test_rejects_non_string_relation_targets_without_crashing(self):
        for endpoint in (["math.graph"], {"id": "math.graph"}, 7):
            with self.subTest(endpoint=endpoint):
                graph = dict(self.graph)
                graph["relations"] = [dict(self.graph["relations"][0], target=endpoint)]
                errors = validate_graph(graph)
                self.assertTrue(any("target" in error and "string" in error for error in errors))


    def test_rejects_graphs_over_resource_limits(self):
        graph = dict(self.graph)
        graph["concepts"] = [{"id": f"n{i}", "label": f"Node {i}"} for i in range(10001)]
        self.assertTrue(any("concept limit" in error for error in validate_graph(graph)))

    def test_rejects_relation_count_over_resource_limit(self):
        graph = dict(self.graph)
        graph["relations"] = [{"source": "math.graph", "target": "math.graph", "type": "related"}] * 50001
        self.assertTrue(any("relation limit" in error for error in validate_graph(graph)))


if __name__ == "__main__":
    unittest.main()
