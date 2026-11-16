# HAA-D-3 — The Neural Odyssey

> **مهندسی هنر، هنر مهندسی** — an evidence-led system that transforms interdisciplinary research and mathematical models into reproducible explanations and cinematic experiences.

**Persian identity:** اودیسهٔ هوش — از هندسهٔ ذهن تا معماری دانش  
**Baseline:** 0.2.0 consolidated foundation on main  
**Repository:** https://github.com/metsam-mastem/HAA-D-3

## 🚦 Run the Quality Gate — start here

<details>
<summary><strong>How to run checks on GitHub (no local setup)</strong></summary>

1. Open **[Actions → HAA-D-3 Quality Gate](https://github.com/metsam-mastem/HAA-D-3/actions/workflows/quality.yml)**.
2. Select **Run workflow** (top-right). GitHub requires the workflow to be present on the default branch for manual dispatch.
3. Select the branch you want to verify.
4. Choose a scope:
   - **full** — repository structure, Markdown inventory/links, full Python tests, SceneSpec validation, deterministic release bundle with MP4/WAV/MIDI/SVG, and knowledge-graph provenance outputs. Recommended for final verification.
   - **docs** — structure + Markdown inventory + local links. Fastest for documentation-only edits.
   - **python** — Python tests + SceneSpec + media/release + graph checks. Use for code changes.
5. Press **Run workflow** and open the run to follow jobs and logs.
6. To get the generated ZIP, open the completed run → **Artifacts** → download `haa-d3-e2e-release`. Artifact retention is 14 days.

**Automatic checks:** pushes to configured branches and every pull request trigger the full gate. Manual scopes only reduce work for an explicitly requested run; they do not replace full PR verification.

Useful links: [All workflow runs](https://github.com/metsam-mastem/HAA-D-3/actions) · [Workflow file](.github/workflows/quality.yml) · [Artifacts](https://github.com/metsam-mastem/HAA-D-3/actions?query=workflow%3A%22HAA-D-3+Quality+Gate%22)

</details>

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
- Runtime JSON Schema validation for SceneSpec and Finding contracts.
- Deterministic SVG frame renderer and MIDI data-sonification adapter.
- End-to-end ZIP release bundler with SHA-256 inventory and explicit review status.
- Blender 4.x background renderer adapter; Blender 4.0.2 / EEVEE runtime passed in CI with 11 verified 1920×1080 PNG frames, H.264/AAC MP4, WAV data sonification, 0.02 s stream-duration delta, saved .blend reopen and user-scene preservation.
- Knowledge-graph validation, deterministic SVG projection and SHA-256 provenance receipt, with graph-size and render-pixel budgets.
- Scene contract validation rejects non-finite values, booleans in numeric fields, malformed root types and unhashable enum values.
- Kuramoto simulation and SVG rendering enforce snapshot, frame, object, pixel and work budgets.
- Blender adapter preserves unowned scene objects and restores user render settings; Blender 4.0.2 runtime rendering and artifact verification passed (11 frames, 1920×1080), including H.264/AAC assembly and WAV data sonification.
- MP4 generation now requires FFprobe stream validation and a full FFmpeg decode pass before returning a verification PASS.
- CI audits installed third-party Python dependencies and publishes a CycloneDX SBOM artifact.
- Browser-based Neural Odyssey illustrative demo.

Graph and Kuramoto outputs remain computational/model outputs, not empirical scientific validation. The Kuramoto numerical implementation passes independent-formulation, analytical-special-case and convergence checks; external scientific review and experimental-data comparison remain pending. It is a generic coupled-oscillator system, not a biological brain model.

## Quick start
Requires Python 3.11+.

~~~bash
python -m pip install -e .
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m haa_d3.cli validate-scene examples/scenes/synthetic-emergence.scene.json
PYTHONPATH=src python -m haa_d3.cli simulate-kuramoto --nodes 64 --coupling 1.5 --dt 0.02 --steps 500 --seed 7 --output /tmp/kuramoto.json
PYTHONPATH=src python -m haa_d3.cli kuramoto-scene --nodes 64 --steps 250 --seed 7 --output /tmp/kuramoto-scene.json
PYTHONPATH=src python -m haa_d3.cli render-knowledge-graph examples/knowledge/seed-graph.json --out /tmp/haa-d3-graph
PYTHONPATH=src python -m haa_d3.cli build-release --nodes 24 --steps 100 --dt 0.05 --frame-rate 24 --output artifacts/haa-d3-release.zip
~~~

### Optional MP4 export
Install FFmpeg on the host and the media extra:
```bash
python -m pip install -e ".[media]"
PYTHONPATH=src python -m haa_d3.cli build-release --nodes 24 --steps 100 --dt 0.05 --frame-rate 24 --video --output artifacts/haa-d3-release.zip
```
The bundle then includes H.264/AAC MP4 preview, PCM WAV sonification, MIDI cue, SVG frames, source data and SHA-256 manifest. The WAV is algorithmic data sonification, not a composed soundtrack.

## Delivery plan
The compressed execution gates and acceptance criteria are in [Phased Delivery Plan](docs/17-delivery/PHASED-DELIVERY-PLAN.md).

## Creative identity
The narrative frame has three chapters: **The Genesis / پیدایش**, **The Convergence / همگرایی**, and **The Emergence / ظهور**. Original music references and creative direction remain in the series bible and creative reference map. They are inspiration only; no copyrighted audio is bundled or assumed cleared.

## Security and repository governance

- [Security reporting and vulnerability handling](SECURITY.md)
- Dependabot monitors Python and GitHub Actions dependencies weekly.
- `CODEOWNERS` routes sensitive implementation and governance paths to the repository owner; this file does not itself enforce branch protection or independent approval.
- The Quality Gate pins third-party GitHub Actions to verified commit SHAs.

## Quality and evidence
Work statuses: PASS, FAIL, NOT RUN, BLOCKED, DRAFT, IN REVIEW. Evidence classes: OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR, UNKNOWN. Green CI proves only the checks it runs. Scientific review, rights clearance and creative QC are separate release gates.

## Licensing
The repository owner has not selected a project license. Public visibility does not grant reuse rights. Do not reuse external code, data, models, fonts, images, music or video without checking applicable terms.

## Current change
Foundation consolidation [PR #4](https://github.com/metsam-mastem/HAA-D-3/pull/4) is merged. Numerical verification [PR #5](https://github.com/metsam-mastem/HAA-D-3/pull/5) is also merged. Project-state reconciliation [PR #6](https://github.com/metsam-mastem/HAA-D-3/pull/6) is merged; `main` is the authoritative current baseline.
