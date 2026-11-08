# HAA-D-3 — The Neural Odyssey

> **مهندسی هنر، هنر مهندسی** — an evidence-led system that transforms interdisciplinary research and mathematical models into reproducible explanations and cinematic experiences.

**Persian identity:** اودیسهٔ هوش — از هندسهٔ ذهن تا معماری دانش  
**Baseline:** 0.2.0 consolidated foundation on main  
**Repository:** https://github.com/metsam-mastem/HAA-D-3

## Mission
HAA-D-3 connects research, mathematics, computational engineering, knowledge representation, scientific visualization, animation, cinematography and original sound design in one governed production lifecycle. It is not a pile of disconnected tools, demos or agent-specific projects: every capability must contribute to a traceable path from a question to a validated and reviewable output.

The project does not claim a validated novel neural architecture, biological brain simulation, measured performance advantage or universal model of intelligence.

## The single project spine
~~~text
QUESTION
  → SOURCE & CLAIM LEDGER
  → FORMAL MODEL
  → REPRODUCIBLE EXPERIMENT
  → INDEPENDENT VALIDATION
  → VERSIONED SCENE SPECIFICATION
  → STORYBOARD & SHOT PLAN
  → RENDER / SOUND / EDIT
  → SCIENTIFIC + CREATIVE + RIGHTS QC
  → RELEASE PACKAGE
  → RETROSPECTIVE & NEXT QUESTION
~~~

See [End-to-End Lifecycle](docs/END-TO-END-LIFECYCLE.md) for gates, required records, evidence, failure handling and release criteria.

## Start here — mandatory reading order
1. [Repository rules for every contributor and AI agent](AGENTS.md)
2. [Project governance and anti-sprawl controls](docs/GOVERNANCE.md)
3. [Source map and ownership of every major path](docs/SOURCE-MAP.md)
4. [End-to-end lifecycle and release gates](docs/END-TO-END-LIFECYCLE.md)
5. [Documentation index](docs/README.md)
6. [Contribution workflow](CONTRIBUTING.md)

## Architecture: one owner per responsibility

| Layer | Canonical home | Responsibility |
|---|---|---|
| Research and evidence | docs/02-knowledge/, docs/06-research/, docs/10-references/, research/ | Sources, questions, claims, methods and findings |
| Portable computational core | src/haa_d3/ | Contracts, numerical models, graph tools, transformations and CLI |
| Contracts and examples | schemas/, examples/ | Versioned interchange formats and reproducible inputs |
| Scene and creative production | scenes/, creative/, adapters/ | Renderer-neutral scenes and replaceable creative backends |
| Browser demo | demo/neural-odyssey/ | Lightweight illustrative experience |
| Verification | tests/, .github/workflows/quality.yml | One test root and one quality gate |
| Generated artifacts | artifacts/, releases/ | Outputs, checksums, manifests and release evidence |
| Governance and decisions | docs/, AGENTS.md, CONTRIBUTING.md | Policies, ADRs, handoffs and project memory |

The Python package has one canonical root: src/haa_d3/. The test suite has one root: tests/. See [Source Map](docs/SOURCE-MAP.md).

## Current implemented slices
- Portable Finding and SceneSpec semantic checks.
- Capability descriptors and deterministic adapter selection.
- Seeded Kuramoto coupled-oscillator prototype and research-to-scene mapping.
- Independent numerical checks: O(N²) pairwise reference, analytical K=0 solution and Heun second-order convergence (CI run 42463415737: PASS).
- Knowledge-graph validation, deterministic SVG projection and SHA-256 provenance receipt.
- Browser-based Neural Odyssey illustrative demo.

Graph and Kuramoto outputs remain computational/model outputs, not empirical scientific validation. The Kuramoto numerical implementation passes independent-formulation, analytical-special-case and convergence checks; external scientific review and experimental-data comparison remain pending. It is a generic coupled-oscillator system, not a biological brain model.

## Quick start
Requires Python 3.11+.

~~~bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m haa_d3.cli validate-scene examples/scenes/synthetic-emergence.scene.json
PYTHONPATH=src python -m haa_d3.cli simulate-kuramoto --nodes 64 --coupling 1.5 --dt 0.02 --steps 500 --seed 7 --output /tmp/kuramoto.json
PYTHONPATH=src python -m haa_d3.cli kuramoto-scene --nodes 64 --steps 250 --seed 7 --output /tmp/kuramoto-scene.json
PYTHONPATH=src python -m haa_d3.cli render-knowledge-graph examples/knowledge/seed-graph.json --out /tmp/haa-d3-graph
~~~

## Creative identity
The narrative frame has three chapters: **The Genesis / پیدایش**, **The Convergence / همگرایی**, and **The Emergence / ظهور**. Original music references and creative direction remain in the series bible and creative reference map. They are inspiration only; no copyrighted audio is bundled or assumed cleared.

## Quality and evidence
Work statuses: PASS, FAIL, NOT RUN, BLOCKED, DRAFT, IN REVIEW. Evidence classes: OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR, UNKNOWN. Green CI proves only the checks it runs. Scientific review, rights clearance and creative QC are separate release gates.

## Licensing
The repository owner has not selected a project license. Public visibility does not grant reuse rights. Do not reuse external code, data, models, fonts, images, music or video without checking applicable terms.

## Current change
Foundation consolidation [PR #4](https://github.com/metsam-mastem/HAA-D-3/pull/4) is merged. Numerical verification [PR #5](https://github.com/metsam-mastem/HAA-D-3/pull/5) is also merged. Current main baseline: `ce4e421b630179900ccd1e18f13bae61e37e29eb`.
