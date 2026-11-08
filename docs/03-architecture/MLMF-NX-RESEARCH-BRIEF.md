# MLMF-NX — Core Neural Architecture Research Brief

**Project:** HAA-D-3 / The Neural Odyssey  
**Working label:** MLMF-NX (user-originated research label)  
**Status:** Research hypothesis / DRAFT — not implemented, trained, benchmarked or independently validated.  
**Purpose:** Preserve the original conversation's neural-architecture research thread as a canonical, discoverable artifact rather than letting it disappear inside broad project prose.

## 1. Concept as currently understood
The working concept explores a hybrid neural system with several candidate ingredients:
- modular, multilayer artificial-neuron computation;
- spatial or graph-embedded organization (coordinates are an optional representation, not an assumption that “3D = intelligence”);
- signal/noise filtering or denoising components;
- recurrent, hierarchical, multi-path and/or multi-temporal feedback;
- a pretrained foundation model as a replaceable high-capability baseline or integration component;
- resource-aware execution, sparse connections and modular boundaries.

The exact acronym expansion, neuron definition, canonical topology, learning rule, and whether each ingredient belongs to the same design remain **UNKNOWN / requiring owner clarification and literature-backed specification**. This document deliberately does not invent a settled model.

## 2. Research question
Can a bounded modular/spatial/feedback subsystem improve a defined task relative to an appropriate strong baseline, with an acceptable stability, memory, latency, energy and engineering-complexity cost?

Sub-questions:
1. What is the unit of computation: scalar neuron, vector-valued module, graph node, recurrent cell, or hybrid?
2. Does spatial embedding encode useful inductive bias, and what task/data regime demonstrates it?
3. What exact signal is filtered, by what objective, and how is signal/noise defined?
4. Feedback: local/interlayer/global/temporal; what carries state or error; what are the update equations and stopping rules?
5. Is the foundation model frozen, fine-tuned, distilled, or accessed through an adapter?
6. Is sparse topology static, distance-dependent, learned, or dynamically rewired?
7. What is the minimal experiment that isolates the effect of each ingredient?

## 3. Candidate system decomposition
| Component | Role hypothesis | Contract to specify | Status |
|---|---|---|---|
| Input/task adapter | encode data and task semantics | typed input/output, preprocessing | candidate |
| Foundation-model baseline | broad pretrained capability | model ID/version, license, interface, frozen/trainable | reference only |
| Modular compute graph | compose units and paths | graph schema, node/edge types, dimensions | candidate |
| Spatial embedding | encode geometric relation | coordinate system, distance, edge policy | candidate |
| Denoising/filter block | improve robustness or signal quality | noise model, objective, metrics | candidate |
| Feedback router | return state/error/context | path type, delay, gain, target | candidate |
| Learning/update controller | adjust parameters/state | rule, schedule, gradients/local updates | candidate |
| Stability monitor | bound dynamics | spectral/gain bounds, clipping, convergence/termination | required if feedback exists |
| Task head/evaluator | produce and score task output | task metrics, calibration, uncertainty | task-specific |
| Provenance/resource monitor | make runs reproducible | seed/config/hash, latency, memory, compute | required |

## 4. Candidate baseline ladder
Do not compare a hybrid against a weak or mismatched model.
- B0: task-appropriate conventional baseline (e.g., MLP/GRU/GNN; selected after task choice).
- B1: strong established model matching the task and data.
- B2: pretrained foundation-model baseline if the task benefits from it.
- C1: baseline + spatial graph only.
- C2: baseline + feedback only.
- C3: baseline + denoising only.
- C4: baseline + modular routing only.
- C5: combination of components only after isolated effects justify composition.

The comparisons must share dataset splits, data preprocessing, seeds, compute budget, training schedule and metric definitions. Report variance or confidence intervals when feasible.

## 5. Evaluation and falsification
Measure:
- task quality (accuracy/F1/MAE or justified metric), calibration and robustness;
- resource cost (parameter count, peak RAM/VRAM, latency, throughput, energy if instrumented);
- stability (bounded state, gradient behavior, convergence, oscillation/divergence, sensitivity);
- complexity (implementation burden, dependency surface, failure modes, reproducibility).

Falsification criteria include: no repeatable task gain; gain disappears under matched compute; instability or cost exceeds the declared budget; component effect is not separable; results depend on data leakage or seed selection.

## 6. Literature and code entry points
- seRNN spatial embedding precedent: https://www.nature.com/articles/s42256-023-00748-9 and https://github.com/8erberg/spatially-embedded-RNN
- feedback alignment: https://www.nature.com/articles/ncomms13276
- GLE/local spatiotemporal learning: https://www.nature.com/articles/s41467-025-66666-z
- RNN gradient stability background: https://proceedings.mlr.press/v28/pascanu13.html
- graph learning framework: https://github.com/pyg-team/pytorch_geometric
- SNN toolkits as optional adjacent models: https://github.com/norse/norse and https://github.com/jeshraghian/snntorch

These are starting references, not endorsements or proof of novelty. License and reproducibility audits are required before adoption.

## 7. Implementation gate
No custom neural training implementation should begin until:
- task and dataset are chosen and rights reviewed;
- acronym/terms and architecture graph are clarified;
- equations, dimensions, state, update rules, feedback gain and termination are specified;
- baseline and ablation plan are approved;
- resource ceiling and success/falsification thresholds are set;
- tests and reproducibility protocol are written.

## 8. Current implementation state
- Documentation: this research brief exists as a seed.
- Code: no MLMF-NX neural network module is implemented.
- Training: NOT RUN.
- Benchmarks: NOT RUN.
- Scientific review: NOT RUN.
- The current Kuramoto slice is a generic coupled-oscillator visualization and must not be described as MLMF-NX or as a brain simulation.

## 9. Decisions still needed
Record answers in an ADR or update this brief:
1. Exact acronym expansion and intended naming.
2. Task and data modality for first test.
3. Whether “neuron” means scalar, vector, or modular cell.
4. Required feedback type and learning rule.
5. Spatial topology and dimensional semantics.
6. Foundation model baseline and license/compute target.
7. measurable success and stop thresholds.
