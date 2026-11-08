# Document Catalog and Completeness Gate

**Generated inventory · 2026-11-08 ·** This is a path inventory, not an assertion that every document is approved or implemented.

The checker compares this exact list with tracked Markdown paths. A new, moved or deleted Markdown file must update this catalog and the navigation index in the same change.

## Tracked Markdown inventory

| Repository-relative path | Class |
|---|---|
| `.github/pull_request_template.md` | Workflow template |
| `AGENTS.md` | Repository guide |
| `CONTRIBUTING.md` | Repository guide |
| `README.md` | Repository guide |
| `adapters/README.md` | Repository guide |
| `adapters/blender/README.md` | Repository guide |
| `artifacts/README.md` | Repository guide |
| `creative/README.md` | Repository guide |
| `demo/neural-odyssey/README.md` | Repository guide |
| `docs/00-charter/MANIFESTO.md` | Project document |
| `docs/00-charter/PROGRAM-OPERATING-MODEL.md` | Project document |
| `docs/00-charter/PROJECT-CHARTER.md` | Project document |
| `docs/01-creative/THREE-CHAPTERS-SERIES-BIBLE.md` | Project document |
| `docs/02-knowledge/KNOWLEDGE-UNIVERSE.md` | Project document |
| `docs/02-knowledge/RESEARCH-PLAN.md` | Project document |
| `docs/02-product/PRODUCT-SCOPE.md` | Project document |
| `docs/03-architecture/ADAPTER-CAPABILITY-CONTRACT.md` | Project document |
| `docs/03-architecture/CONCEPT-ARCHITECTURE.md` | Project document |
| `docs/03-architecture/MLMF-NX-RESEARCH-BRIEF.md` | Project document |
| `docs/03-architecture/REFERENCE-ARCHITECTURE.md` | Project document |
| `docs/04-domain/DOMAIN-MODEL.md` | Project document |
| `docs/04-engineering-spec/ES-DRAFT-0.1.md` | Project document |
| `docs/05-vertical-slice/VERTICAL-SLICE-FEASIBILITY.md` | Project document |
| `docs/05-vertical-slice/VS-01-NEURAL-EMERGENCE.md` | Project document |
| `docs/05-vertical-slice/VS-02-COUPLED-OSCILLATORS.md` | Project document |
| `docs/06-planning/WBS-ROADMAP.md` | Project document |
| `docs/06-research/RESEARCH-OPERATIONS.md` | Project document |
| `docs/07-data/DATA-AND-PROVENANCE.md` | Project document |
| `docs/07-reuse/REPOSITORY-REUSE-AUDIT.md` | Project document |
| `docs/08-contracts/RESEARCH-TO-SCENE-MAPPING.md` | Project document |
| `docs/08-contracts/SCENE-SPEC-CONTRACT.md` | Project document |
| `docs/08-evaluation/COMPETITOR-LANDSCAPE.md` | Project document |
| `docs/08-evaluation/RESOURCE-BENCHMARK-PLAN.md` | Project document |
| `docs/09-creative-tech/SCIENTIFIC-TO-CINEMA-PIPELINE.md` | Project document |
| `docs/09-creative-tech/VISUAL-ANIMATION-PIPELINE.md` | Project document |
| `docs/10-references/CREATIVE-REFERENCE-MAP.md` | Project document |
| `docs/10-references/GITHUB-NATURE-LANDSCAPE.md` | Project document |
| `docs/10-references/SOURCES.md` | Project document |
| `docs/11-governance/CLAIM-AND-PROVENANCE-POLICY.md` | Project document |
| `docs/11-governance/RISK-REGISTER.md` | Project document |
| `docs/11-governance/STATUS-CHANGELOG.md` | Project document |
| `docs/12-production/CREATIVE-DIRECTION-BIBLE.md` | Project document |
| `docs/13-planning/CONVERSATION-REQUIREMENTS-AND-GAP-AUDIT.md` | Project document |
| `docs/13-planning/DOCUMENT-CATALOG.md` | Project document |
| `docs/13-planning/HANDOFF-2026-11-08-foundation-v02.md` | Project document |
| `docs/13-planning/HANDOFF-2026-11-08-foundation.md` | Project document |
| `docs/13-planning/HANDOFF-2026-11-08-vs02.md` | Project document |
| `docs/13-planning/HANDOFF-TEMPLATE.md` | Project document |
| `docs/13-planning/LEGACY-DOCUMENT-INVENTORY.md` | Project document |
| `docs/13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md` | Project document |
| `docs/13-planning/ROADMAP-AND-GATES.md` | Project document |
| `docs/14-platform/PLATFORM-PORTABILITY.md` | Project document |
| `docs/15-operations/RELEASE-AND-QUALITY.md` | Project document |
| `docs/16-decisions/ADR-0001-portable-core-adapter-first.md` | Project document |
| `docs/16-decisions/README.md` | Project document |
| `docs/17-delivery/PHASED-DELIVERY-PLAN.md` | Project document |
| `docs/END-TO-END-LIFECYCLE.md` | Project document |
| `docs/GOVERNANCE.md` | Project document |
| `docs/README.md` | Project document |
| `docs/SOURCE-MAP.md` | Project document |
| `releases/README.md` | Repository guide |
| `research/README.md` | Repository guide |
| `scenes/README.md` | Repository guide |

## Structural invariants
- One Python runtime root: `src/haa_d3/`.
- One Python test root: `tests/`.
- One navigation index: `docs/README.md`.
- One quality workflow: `.github/workflows/quality.yml`.
- One canonical source map: `docs/SOURCE-MAP.md`.
- One lifecycle contract: `docs/END-TO-END-LIFECYCLE.md`.

## Automated checks
- `python scripts/check_document_catalog.py` — exact Markdown inventory.
- `python scripts/check_markdown_links.py` — local Markdown link destinations.
- `PYTHONPATH=src python -m unittest discover -s tests -v` — complete Python test suite.
- Quality Gate validates JSON Schema and semantic contracts, generates a Kuramoto SceneSpec, builds an end-to-end ZIP release (simulation, SceneSpec, SVG frames, MIDI cue and SHA-256 manifest), and produces graph JSON/SVG/provenance receipt.

## Interpretation
A green catalog check means only that tracked Markdown paths are enumerated. It does not validate document truth, approval, scientific claims or completeness of planned work.
