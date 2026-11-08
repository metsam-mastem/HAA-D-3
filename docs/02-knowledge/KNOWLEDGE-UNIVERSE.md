# Knowledge Universe — Taxonomy
**Version:** 0.1 · seed, expandable

## A Mathematics
Linear algebra (vectors/matrices/SVD/conditioning); calculus (gradient/Jacobian/Hessian); tensor algebra; probability/statistics and uncertainty; graph theory (adjacency, paths, Laplacian, spectra); geometry/metric spaces; topology (applicability to test); dynamical systems; information theory; optimization; control theory (gain, delay, stability).

## B Neural computation
Artificial neurons; MLP; CNN; RNN/LSTM/GRU; Transformers; state-space models; GNN/message passing; SNN; MoE/conditional routing; neuro-symbolic; modular/multitask; hybrid foundation adapters.

## C Spatial & multidimensional
Coordinates for neurons/modules; spatially embedded RNNs (seRNN); sparse distance-dependent connectivity; graph representations; 3D grids/tensors (not synonymous with physically positioned neurons); adaptive rewiring; hierarchical spatial modules. Open question: what computation does spatial placement encode, and what task shows benefit?

## D Learning, feedback & stability
Backprop/BPTT; feedback alignment; Hebbian/local learning; predictive coding; equilibrium/latent-equilibrium methods; online/continual learning; credit assignment; denoising objectives; spectral radius, gain limits, gradient clipping, termination. Feedback categories local/interlayer/global/temporal are this project's taxonomy, not universal nomenclature.

## E Foundation models
Model cards and licenses; open weights vs open source; adapters and feature interfaces; LoRA/QLoRA; quantization; context/cache constraints; orchestration/fallback; baseline versus added module.

## F Software/system engineering
Requirements and traceability; conceptual/logical/physical architecture; schemas/contracts; unit/integration/property/regression/acceptance tests; CI/CD; observability; versioning; security/sandbox; local/edge/server deployment; ADR/change management.

## G Compute & efficiency
CPU/GPU/NPU; RAM/VRAM and activation/optimizer memory; sparse kernels; FP16/BF16/INT8/4-bit; low-rank/pruning; batching/cache/selective compute; profiling latency/throughput/energy; distributed and neuromorphic options. Sparse representation may not be faster; benchmark.

## H Knowledge engineering
Typed concept graph/ontology; sources; evidence/hypothesis/contradiction/decision ledgers; requirements links; semantic retrieval/RAG only when justified; versioning and synthesis.

## I Visualization & creative technology
Scientific charts; 2D/3D graph layouts; SVG, Graphviz, WebGL/Three.js, Blender/Houdini/Unreal candidates; procedural motion; cinematography/compositing; UI/UX; music/BPM/meter/motif; storyboard and accessible explainers.

## J Research, evaluation & ethics
Literature/novelty review; benchmark design and splits; ablations/statistics; reproducibility; license/data audit; privacy/safety; evidence strength and claim qualification.

## Cross-domain dependency paths
Graph theory → graph Laplacian → sparse topology → GNN/message passing → prototype → topology ablation.
Control theory → gain/delay → recurrent stability → loop controller → stress test.
Foundation model → adapter contract → orchestration → baseline → compare custom addition.
Source → evidence → ADR → requirement → test → report/visual.
Formal model → simulation → verification → visualization → animation/storyboard.

## Research card schema
ID; question; objective; prerequisites; scope; primary sources; methods; findings; evidence strength; limitations; architecture link; dependencies; open questions; output; status; reviewer; date.