# Concept Architecture
**Status:** candidate, not implementation truth.

## Stance
Begin with a modular monolith and typed contracts. Foundation model serves as broad baseline; custom neural core is a bounded experimental subsystem. Do not train a foundation model from scratch in the initial phase.

## Planes
1. Neural Computation: input encoder, foundation adapter, spatial graph module, recurrent/local module, task head.
2. Feedback & Learning: feedback router, objective registry, update controller, stability monitor, learning-rule adapters.
3. Control & Governance: orchestrator, resource budget, provenance registry, evaluator, human review, config/versioning.

## Data/control flow
Input/representation → pretrained model or encoder → optional spatial graph/feature module → task/output head. Configured feedback can connect module boundaries only. Evaluator runs baseline/ablation. Knowledge store links source, evidence, decisions, requirements, tests and results. Renderer projects typed graph data.

## Contracts (candidate)
ModelAdapter: load/configure/infer + provider/model/version/capabilities.
SpatialGraph: stable node IDs, coordinates, typed edges, weights, sparsity and topology version.
FeedbackController: objective, source/destination, policy, bounded steps and stopping rule.
ResourceMonitor: wall time, peak RSS/VRAM, token/operation counts, energy if instrumented.
Evaluator: task metric, baseline, repeat runs, confidence summary, export.
KnowledgeStore: source/concept/evidence/decision/artifact records.
VisualizationRenderer: graph/events to SVG/JSON with source snapshot hash.

## Feedback safeguards
Disabled by default until objective/test declared. Every loop max iterations, gain/update limit, timeout and exit criterion. Stop on divergence/NaN, budget exhaustion, unchanged state, max step or cancellation. Monitor loss/output norms and sensitivity to gain/delay.

## Alternatives
A pretrained model + tools/RAG baseline; B + small spatial graph; C task-trained recurrent/spatial module; D conditional modular experts; E local-learning/spiking branch. Compare task quality, latency, memory, reproducibility, complexity and licenses.

## Distinctions
Conv3D is not equivalent to a 3D neuron graph. Tensor axes, latent dimensions, physical coordinates and graph topology differ. Feedback alignment/GLE are not assumed plug-compatible with arbitrary transformer internals. Every addition must be ablatable.