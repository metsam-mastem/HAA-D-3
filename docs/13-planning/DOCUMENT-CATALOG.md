# Document Catalog & Completeness Checks

**Catalog revision:** 2026-11-08 · Inventory covers all tracked Markdown paths in this repository tree.
This file is an inventory, not an approval or assertion that all planned work is implemented.

## Markdown inventory

| Repository-relative path | Class | Presence status |
|---|---|---|
| `.github/pull_request_template.md` | GitHub workflow/template | Tracked Markdown; checked in CI |
| `AGENTS.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `CONTRIBUTING.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `adapters/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `artifacts/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `creative/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `demo/neural-odyssey/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `docs/00-charter/MANIFESTO.md` | Project document | Tracked Markdown; checked in CI |
| `docs/00-charter/PROGRAM-OPERATING-MODEL.md` | Project document | Tracked Markdown; checked in CI |
| `docs/00-charter/PROJECT-CHARTER.md` | Project document | Tracked Markdown; checked in CI |
| `docs/01-creative/THREE-CHAPTERS-SERIES-BIBLE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/02-knowledge/KNOWLEDGE-UNIVERSE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/02-knowledge/RESEARCH-PLAN.md` | Project document | Tracked Markdown; checked in CI |
| `docs/02-product/PRODUCT-SCOPE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/03-architecture/ADAPTER-CAPABILITY-CONTRACT.md` | Project document | Tracked Markdown; checked in CI |
| `docs/03-architecture/CONCEPT-ARCHITECTURE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/03-architecture/REFERENCE-ARCHITECTURE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/04-domain/DOMAIN-MODEL.md` | Project document | Tracked Markdown; checked in CI |
| `docs/04-engineering-spec/ES-DRAFT-0.1.md` | Project document | Tracked Markdown; checked in CI |
| `docs/05-vertical-slice/VERTICAL-SLICE-FEASIBILITY.md` | Project document | Tracked Markdown; checked in CI |
| `docs/05-vertical-slice/VS-01-NEURAL-EMERGENCE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/05-vertical-slice/VS-02-COUPLED-OSCILLATORS.md` | Project document | Tracked Markdown; checked in CI |
| `docs/06-planning/WBS-ROADMAP.md` | Project document | Tracked Markdown; checked in CI |
| `docs/06-research/RESEARCH-OPERATIONS.md` | Project document | Tracked Markdown; checked in CI |
| `docs/07-data/DATA-AND-PROVENANCE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/07-reuse/REPOSITORY-REUSE-AUDIT.md` | Project document | Tracked Markdown; checked in CI |
| `docs/08-contracts/RESEARCH-TO-SCENE-MAPPING.md` | Project document | Tracked Markdown; checked in CI |
| `docs/08-contracts/SCENE-SPEC-CONTRACT.md` | Project document | Tracked Markdown; checked in CI |
| `docs/08-evaluation/COMPETITOR-LANDSCAPE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/08-evaluation/RESOURCE-BENCHMARK-PLAN.md` | Project document | Tracked Markdown; checked in CI |
| `docs/09-creative-tech/SCIENTIFIC-TO-CINEMA-PIPELINE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/09-creative-tech/VISUAL-ANIMATION-PIPELINE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/10-references/CREATIVE-REFERENCE-MAP.md` | Project document | Tracked Markdown; checked in CI |
| `docs/10-references/GITHUB-NATURE-LANDSCAPE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/10-references/SOURCES.md` | Project document | Tracked Markdown; checked in CI |
| `docs/11-governance/CLAIM-AND-PROVENANCE-POLICY.md` | Project document | Tracked Markdown; checked in CI |
| `docs/11-governance/RISK-REGISTER.md` | Project document | Tracked Markdown; checked in CI |
| `docs/11-governance/STATUS-CHANGELOG.md` | Project document | Tracked Markdown; checked in CI |
| `docs/12-production/CREATIVE-DIRECTION-BIBLE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/13-planning/DOCUMENT-CATALOG.md` | Project document | Tracked Markdown; checked in CI |
| `docs/13-planning/HANDOFF-2026-11-08-foundation.md` | Project document | Tracked Markdown; checked in CI |
| `docs/13-planning/HANDOFF-2026-11-08-vs02.md` | Project document | Tracked Markdown; checked in CI |
| `docs/13-planning/HANDOFF-TEMPLATE.md` | Project document | Tracked Markdown; checked in CI |
| `docs/13-planning/LEGACY-DOCUMENT-INVENTORY.md` | Project document | Tracked Markdown; checked in CI |
| `docs/13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md` | Project document | Tracked Markdown; checked in CI |
| `docs/13-planning/ROADMAP-AND-GATES.md` | Project document | Tracked Markdown; checked in CI |
| `docs/14-platform/PLATFORM-PORTABILITY.md` | Project document | Tracked Markdown; checked in CI |
| `docs/15-operations/RELEASE-AND-QUALITY.md` | Project document | Tracked Markdown; checked in CI |
| `docs/16-decisions/ADR-0001-portable-core-adapter-first.md` | Project document | Tracked Markdown; checked in CI |
| `docs/16-decisions/README.md` | Project document | Tracked Markdown; checked in CI |
| `docs/README.md` | Project document | Tracked Markdown; checked in CI |
| `prototype/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `releases/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `research/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |
| `scenes/README.md` | Repository/workspace guide | Tracked Markdown; checked in CI |

## Non-Markdown artifact families
| Paths | Purpose | Check |
|---|---|---|
| `schemas/*.schema.json` | JSON contracts | Quality validation + review |
| `src/haa_d3/*.py` | application core and CLI | unit tests + CI |
| `prototype/src/haa_d3/*.py` | graph validator, SVG renderer, hash receipt | prototype tests + CI |
| `tests/*.py`, `prototype/tests/*.py` | automated tests | CI |
| `examples/**/*.json`, `prototype/data/*.json` | samples/configs | semantic validation and tests |
| `demo/neural-odyssey/*` | browser-based illustrative demo | visual review separately |
| `.github/workflows/*.yml` | automated workflows | Actions results |
| `pyproject.toml`, `.gitignore` | package/tool and repo config | review |
| `scenes/`, `creative/`, `adapters/`, `research/`, `artifacts/`, `releases/` | canonical workspaces | inventory and workspace README |

## Audit checklist
- [x] Recursive default-branch Git tree inspected; API response not truncated.
- [x] All Markdown paths captured in the table.
- [x] Documentation index reorganized by discipline/workflow.
- [x] Outdated README merge-state statement identified for correction.
- [x] Historical handoff notes reconciled by appended current-status notes.
- [ ] Markdown link destination checker is not yet enforced.
- [ ] Dedicated JSON Schema engine in CI remains planned.
- [ ] Owner approval of the full documentation suite remains pending.
- [ ] Project license remains undecided.
- [ ] Research benchmarks, scientific independent review and final animation pipeline remain NOT RUN.

## Anti-forgetting operating rules
1. New Markdown requires category, canonical path, status and index/catalog entry.
2. Contract changes require version, migration note, sample and tests.
3. Substantial tasks update changelog and handoff.
4. Green CI means only the checked software behaviors pass; it does not validate scientific claims or draft documents.
5. Never remove or rename docs without a migration map and preserved history.
6. CI compares tracked Markdown files to the catalog; missing/extra entries fail.
7. Add link checking as a later deterministic job, after choosing a tool and defining offline behavior.
