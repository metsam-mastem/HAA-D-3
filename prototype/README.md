# HAA-D-3 Knowledge Graph Vertical Slice
Standard-library Python prototype: validate a typed concept graph, render SVG deterministically, and emit SHA-256 provenance receipt.

## Run from repo root
```bash
PYTHONPATH=prototype/src python -m haa_d3.cli prototype/data/knowledge-graph.json --out out
PYTHONPATH=prototype/src python -m unittest discover -s prototype/tests -v
```
Outputs: `out/graph.json`, `out/graph.svg`, `out/receipt.json`.
No neural model is trained or evaluated here. Measurements remain NOT RUN until execution results are inspected.
