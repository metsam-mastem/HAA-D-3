# Vertical Slice Feasibility
**Recommendation:** feasible; prioritize a knowledge-to-visual slice first.

## Definition
JSON concept graph → schema validation → deterministic layout → SVG → provenance receipt → export. Outputs: graph JSON, SVG, receipt, tests. It makes architecture and knowledge visible without pretending a neural network has been trained.

## Rationale
Thin end-to-end path across data, validation, processing, rendering, export, tests, CI. Can adapt graph-first principles from user's SSG repo and provenance/pipeline patterns from VINT. Low compute, minimal dependencies; supports knowledge map and motion-design inputs.

## Feasibility assessment
Technical: HIGH for graph→SVG.
Research: MEDIUM (useful infrastructure, not neural validation).
Resources: LOW expected for small graph; measurement NOT RUN.
Integration: HIGH via JSON contracts.
Creative: HIGH, as SVG can become motion-design/scene inputs.

## Acceptance
Python 3.11+ stdlib; fixture passes; malformed graph rejected; CLI emits SVG/receipt; receipt hashes input/output; unit tests; Actions CI; generated artifact available; status only PASS after evidence.

## Neural slice (second increment)
Choose task first: synthetic sequence classification, denoising, graph node classification or temporal patterns. Baseline MLP/GRU/GNN chosen to match task. Add spatial/feedback component individually. Same split, seed, training budget, device and metrics; ablations and resource profile.

## Effort estimate
Graph visualization: ~1–3 focused days for code/tests plus review. Neural slice: ~1–3+ weeks depending task/data/hardware. Estimates only, not executed work.