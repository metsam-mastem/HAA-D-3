# HAA-D-3 — The Neural Odyssey

> An interdisciplinary scientific research, systems-engineering and creative-production platform: from evidence and mathematical models to interactive explanation and cinematic media.

**Persian title:** اودیسهٔ هوش — از هندسهٔ ذهن تا معماری دانش  
**Project codename:** HAA-D-3 · **Narrative title:** The Neural Odyssey  
**Foundation baseline:** 0.1.0  
**Status:** Research planning, documentation foundation and illustrative vertical slice  
**Repository:** https://github.com/metsam-mastem/HAA-D-3

## Mission
Build a traceable, modular and platform-independent system to research, model, simulate, explain, visualize and turn selected scientific/engineering findings into high-quality audiovisual experiences. The program connects neuroscience, mathematics, physics, computer science, scientific visualization, interaction design, animation, cinematography and original sound design.

This repository does not claim a validated novel neural architecture, measured performance gain or biologically accurate simulation.

## Three-chapter creative frame
1. **The Genesis / پیدایش:** foundations, questions, mathematical language and concept formation.
2. **The Convergence / همگرایی:** architecture, relationships, feedback, modeling and the research-to-scene bridge.
3. **The Emergence / ظهور:** validation, synthesis, visual storytelling and cinematic presentation.

## Product architecture
- **Research Engine:** sources, claims, datasets, models, experiments, validation and benchmarks.
- **Computational Core:** portable domain logic, contracts, deterministic transforms and CLI.
- **Knowledge & Scene Bridge:** versioned transformation from approved evidence/model outputs to scene specifications.
- **Creative Engine:** storyboard, shots, camera, lighting, animation, sound, rendering and QC.
- **Adapters:** replaceable model providers, renderers, simulators, storage, search and compute backends.
- **Interfaces:** CLI first; web, desktop, mobile and service API as optional surfaces.

No LLM, cloud provider, renderer, operating system or frontend framework is mandatory for the core. Read [AGENTS.md](AGENTS.md) before contributing.

## Start here
- [Contributor rules](AGENTS.md)
- [Contribution guide](CONTRIBUTING.md)
- [Documentation map](docs/README.md)
- [Mandatory continuity and knowledge-ingestion protocol](docs/13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md)
- [Platform portability strategy](docs/14-platform/PLATFORM-PORTABILITY.md)
- [Adapter capability contract](docs/03-architecture/ADAPTER-CAPABILITY-CONTRACT.md)
- [Architecture decision records](docs/16-decisions/README.md)

## Repository map
| Path | Purpose |
|---|---|
| docs/ | Governance, architecture, research, product, production and operational documentation |
| research/ | Durable source-backed research packs and findings |
| schemas/ | Machine-readable versioned contracts |
| src/haa_d3/ | Portable Python core and CLI |
| adapters/ | Provider, renderer, simulator, storage and compute integrations |
| tests/ | Contract and behavior tests |
| examples/ | Reproducible sample inputs and workflows |
| creative/ | Creative briefs, storyboard and production planning |
| scenes/ | Canonical renderer-independent scene specifications |
| demo/ | Small runnable prototypes |
| artifacts/ | Manifests and pointers for large generated outputs |
| releases/ | Release manifests and quality evidence |
| .github/ | CI workflows |

## Initial vertical slice — Neural Emergence
A lightweight browser scene explores Genesis → Convergence → Emergence using a deterministic synthetic graph, chapter controls, play/pause and a timeline scrubber.

**Scientific status:** illustrative synthetic graph only. It is not a neural simulation, connectome, anatomical reconstruction or measured dataset. No copyrighted audio, lyrics or media are bundled.

[Open the demo source](demo/neural-odyssey/) · [Read the slice specification](docs/05-vertical-slice/VS-01-NEURAL-EMERGENCE.md)

## Portable core: quick start
Requires Python 3.11+.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m haa_d3.cli validate-scene examples/scenes/synthetic-emergence.scene.json
```

The initial CLI performs dependency-free semantic checks. JSON Schema files are the canonical machine-readable contract; full JSON Schema runtime validation is a planned follow-up.

## Research and evidence integrity
Every meaningful claim/visual distinguishes OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR and UNKNOWN. A render is not scientific validation. A synthetic demo is not biological evidence. See the [claim and provenance policy](docs/11-governance/CLAIM-AND-PROVENANCE-POLICY.md).

## Licensing
The project license has not yet been selected by the repository owner. Do not assume that public visibility grants reuse rights. External dependencies, datasets, models, fonts, images, audio and video require individual license/provenance review.

## Development status
The foundation branch contains the initial documentation, governance rules, portable contract validator, example SceneSpec, tests and CI workflow. Test execution and CI results must be checked from GitHub Actions before claiming PASS. The branch is intentionally separate from main; no merge is implied.
