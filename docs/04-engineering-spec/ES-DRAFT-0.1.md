# Engineering Specification — Draft 0.1
**State:** preliminary; awaiting owner review and target task choice.

## Purpose and operating concept
Local-first research platform and thin slice to author/import concept nodes, define typed relations, render graph, export deterministic artifacts, and record provenance. Neural model integration comes later through adapters.

## Functional requirements
FR-001 concepts have stable unique IDs and labels.
FR-002 relations are typed.
FR-003 graph validator rejects duplicate IDs and dangling edges.
FR-004 renderer emits SVG from a graph snapshot.
FR-005 export retains source JSON and hashes output receipt.
FR-006 docs distinguish evidence, hypothesis, inference, creative reference.
FR-007 future model adapters expose provider/model/version/capabilities.
FR-008 feedback config declares objective, limits and stop conditions.
FR-009 evaluator compares candidate to declared baseline.
FR-010 unexecuted tests are never marked PASS.

## Nonfunctional
NFR-001 deterministic JSON/SVG for same input/config (volatile metadata excluded).
NFR-002 modular maintainability.
NFR-003 Python 3.11+ stdlib for initial slice.
NFR-004 core no network or source execution.
NFR-005 traceability with input snapshot/tool version.
NFR-006 target 500-node graph visualization to be profiled before commitment.
NFR-007 textual summary and SVG title/description.
NFR-008 dependency/assets license audit before release.

## Data model
Concept: {id,label,domain,description?,x?,y?,z?,status?}
Relation: {source,target,type,weight?}
Graph: {schema_version:"0.1",title,concepts[],relations[]}
Receipt: {input_sha256,output_sha256,tool_version,generated_at?,config}

## Interface candidates
validate_graph(graph) → errors/result.
render_svg(graph, options) → SVG.
write_artifacts(graph, directory) → graph.json, graph.svg, receipt.json.
NeuralGraph.forward(input, config) → output + diagnostics; contract deferred until task/objective chosen.

## Verification
VT-001 unique IDs; VT-002 dangling relation rejected; VT-003 valid fixture accepted; VT-004 labels and relation geometry in SVG; VT-005 hashes match bytes; VT-006 deterministic fixture; VT-007 CLI distinguishes invalid/runtime errors; VT-008 profile duration/RSS; VT-009 ablation validates architecture claim; VT-010 adapter conformance.

## Acceptance
Knowledge visualization slice accepted when fixture validates, SVG and receipt generated deterministically, and tests pass in CI. It does not establish neural performance.

## Open items
Select task/dataset rights, foundation model family, module dimensionality, objective/learning rule, target hardware, and review schema.