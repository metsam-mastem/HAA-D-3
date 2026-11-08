# HAA-D-3 Documentation Map

**Canonical navigation and index.** The document catalog enumerates all tracked Markdown and CI checks catalog completeness. File presence does not imply owner approval or implementation; status and evidence govern.

## Governance and identity
- [PROJECT CHARTER](00-charter/PROJECT-CHARTER.md)
- [MANIFESTO](00-charter/MANIFESTO.md)
- [PROGRAM OPERATING MODEL](00-charter/PROGRAM-OPERATING-MODEL.md)
- [CLAIM AND PROVENANCE POLICY](11-governance/CLAIM-AND-PROVENANCE-POLICY.md)
- [RISK REGISTER](11-governance/RISK-REGISTER.md)
- [STATUS CHANGELOG](11-governance/STATUS-CHANGELOG.md)

## Product, architecture, domain and specification
- [PRODUCT SCOPE](02-product/PRODUCT-SCOPE.md)
- [DOMAIN MODEL](04-domain/DOMAIN-MODEL.md)
- [CONCEPT ARCHITECTURE](03-architecture/CONCEPT-ARCHITECTURE.md)
- [REFERENCE ARCHITECTURE](03-architecture/REFERENCE-ARCHITECTURE.md)
- [ADAPTER CAPABILITY CONTRACT](03-architecture/ADAPTER-CAPABILITY-CONTRACT.md)
- [ES DRAFT 0.1](04-engineering-spec/ES-DRAFT-0.1.md)
- [PLATFORM PORTABILITY](14-platform/PLATFORM-PORTABILITY.md)
- [README](16-decisions/README.md)
- [ADR 0001 Portable Core Adapter First](16-decisions/ADR-0001-portable-core-adapter-first.md)

## Research, knowledge, evidence and data
- [KNOWLEDGE UNIVERSE](02-knowledge/KNOWLEDGE-UNIVERSE.md)
- [RESEARCH PLAN](02-knowledge/RESEARCH-PLAN.md)
- [RESEARCH OPERATIONS](06-research/RESEARCH-OPERATIONS.md)
- [DATA AND PROVENANCE](07-data/DATA-AND-PROVENANCE.md)
- [REPOSITORY REUSE AUDIT](07-reuse/REPOSITORY-REUSE-AUDIT.md)
- [COMPETITOR LANDSCAPE](08-evaluation/COMPETITOR-LANDSCAPE.md)
- [RESOURCE BENCHMARK PLAN](08-evaluation/RESOURCE-BENCHMARK-PLAN.md)
- [GITHUB NATURE LANDSCAPE](10-references/GITHUB-NATURE-LANDSCAPE.md)
- [SOURCES](10-references/SOURCES.md)

## Delivery planning, handoffs and quality
- [WBS ROADMAP](06-planning/WBS-ROADMAP.md)
- [ROADMAP AND GATES](13-planning/ROADMAP-AND-GATES.md)
- [PROJECT CONTINUITY AND INGESTION PROTOCOL](13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md)
- [HANDOFF TEMPLATE](13-planning/HANDOFF-TEMPLATE.md)
- [HANDOFF 2026 11 08 Foundation](13-planning/HANDOFF-2026-11-08-foundation.md)
- [HANDOFF 2026 11 08 Vs02](13-planning/HANDOFF-2026-11-08-vs02.md)
- [LEGACY DOCUMENT INVENTORY](13-planning/LEGACY-DOCUMENT-INVENTORY.md)
- [DOCUMENT CATALOG](13-planning/DOCUMENT-CATALOG.md)
- [RELEASE AND QUALITY](15-operations/RELEASE-AND-QUALITY.md)

## Vertical slices and contracts
- [VERTICAL SLICE FEASIBILITY](05-vertical-slice/VERTICAL-SLICE-FEASIBILITY.md)
- [VS 01 NEURAL EMERGENCE](05-vertical-slice/VS-01-NEURAL-EMERGENCE.md)
- [VS 02 COUPLED OSCILLATORS](05-vertical-slice/VS-02-COUPLED-OSCILLATORS.md)
- [SCENE SPEC CONTRACT](08-contracts/SCENE-SPEC-CONTRACT.md)
- [RESEARCH TO SCENE MAPPING](08-contracts/RESEARCH-TO-SCENE-MAPPING.md)

## Creative and serial production
- [THREE CHAPTERS SERIES BIBLE](01-creative/THREE-CHAPTERS-SERIES-BIBLE.md)
- [SCIENTIFIC TO CINEMA PIPELINE](09-creative-tech/SCIENTIFIC-TO-CINEMA-PIPELINE.md)
- [VISUAL ANIMATION PIPELINE](09-creative-tech/VISUAL-ANIMATION-PIPELINE.md)
- [CREATIVE DIRECTION BIBLE](12-production/CREATIVE-DIRECTION-BIBLE.md)
- [CREATIVE REFERENCE MAP](10-references/CREATIVE-REFERENCE-MAP.md)

## Root and workspace guides
- [README](../README.md)
- [AGENTS](../AGENTS.md)
- [CONTRIBUTING](../CONTRIBUTING.md)
- [Pull Request Template](../.github/pull_request_template.md)
- [README](../adapters/README.md)
- [README](../artifacts/README.md)
- [README](../creative/README.md)
- [README](../demo/neural-odyssey/README.md)
- [README](../prototype/README.md)
- [README](../research/README.md)
- [README](../scenes/README.md)
- [README](../releases/README.md)

## Machine-readable and code artifacts
- `pyproject.toml` — package and tool configuration
- `schemas/scene-spec.schema.json`, `schemas/finding.schema.json` — machine-readable contracts
- `src/haa_d3/` — portable core, CLI, model simulation and mapping
- `prototype/src/haa_d3/` — graph validation, SVG projection, provenance receipt
- `tests/`, `prototype/tests/` — test suites
- `examples/`, `prototype/data/` — examples and experiment configurations
- `demo/neural-odyssey/` — browser illustrative demo
- `.github/workflows/quality.yml`, `.github/workflows/ci.yml` — CI pipelines
- `scenes/`, `creative/`, `adapters/`, `research/`, `artifacts/`, `releases/` — canonical workspaces

## Status interpretation
- **File present:** tracked in the repository.
- **Implemented:** behavior exists in source and has tests/evidence.
- **Draft:** authored, awaiting owner/scientific/design review.
- **Planned / NOT RUN:** not delivered or executed.
- **Historical handoff:** accurate at its date; later changes are appended in the changelog.

## Maintenance
Any PR adding, moving, deleting or materially changing durable artifacts updates this map and [Document Catalog](13-planning/DOCUMENT-CATALOG.md). The catalog check must pass. Keep one canonical policy/contract and link to it rather than duplicating requirements.
