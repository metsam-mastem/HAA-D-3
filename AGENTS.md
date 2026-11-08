# HAA-D-3 — Mandatory Agent and Contributor Rules

This is the single source of operating rules for every human, coding agent, research agent and creative-production agent in this repository. Read it before acting.

## Mission
HAA-D-3 is one interdisciplinary research-to-cinema system: evidence → formal models → reproducible experiments → validated findings → scene contracts → storytelling → media production. It is not a collection of unrelated demos.

## Mandatory startup sequence
1. Read README.md, docs/README.md, docs/SOURCE-MAP.md and docs/GOVERNANCE.md.
2. Read docs/END-TO-END-LIFECYCLE.md and docs/00-charter/PROGRAM-OPERATING-MODEL.md.
3. Inspect the active branch, current tree, relevant source, tests, schemas, ADRs and latest CI.
4. Write a bounded task brief: owner, objective, non-goals, affected paths, acceptance checks and risks.
5. Continue existing work; do not create a parallel implementation because a file is unfamiliar.

## Canonical ownership
- Python runtime: src/haa_d3/ only.
- Python tests: tests/ only.
- Documentation navigation: docs/README.md only.
- Markdown inventory: docs/13-planning/DOCUMENT-CATALOG.md only.
- Quality workflow: .github/workflows/quality.yml only.
- Sample inputs: examples/; renderer-neutral scenes: scenes/.
- Optional integrations: adapters/; browser demonstration: demo/neural-odyssey/.
- Generated output: artifacts/ or releases/, never source/test folders.

Do not create another package root, prototype root, test root, competing index, policy or contract. Extend the canonical owner or add a documented adapter.

## Non-destructive changes
Preserve user work, provenance, original references and historical handoffs. No unrelated deletion, forced rewrite, unrequested dependency, paid service, license selection or main-branch push. Structural moves require a migration map and complete link updates. Do not claim an uninspected file is obsolete.

## Architecture boundaries
Core domain modules must not import provider SDKs, cloud services, GUI frameworks, renderer SDKs or OS-specific APIs. Adapters depend on public core contracts; core never depends on adapters. Prefer open formats, CPU-first/offline paths and modular monolith architecture until measured requirements justify services.

## Evidence discipline
Evidence classes: OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR, UNKNOWN. Work statuses: PASS, FAIL, NOT RUN, BLOCKED, DRAFT, IN REVIEW. PASS requires executed evidence at a specific commit. A visual render is not scientific validation; a synthetic graph is not a connectome.

## Engineering workflow
For behavior changes use RED → GREEN → REFACTOR. Run focused tests and the full repository suite. Update contracts, examples, docs, source map and catalog together. Inspect the diff. Never report tests passed unless Actions or a local run proves it.

## Research and creative workflow
Capture sources before claims. Record methods, dates, licenses, uncertainty and limitations. Every scene mapping records source field/unit, transform/version, target property and evidence class. Metaphor must be labeled. Media rights must be cleared before release.

## Decision and handoff
Owner approval is required for mission, scope, license, paid services, sensitive data and irreversible architecture decisions. Record architecture decisions as ADRs. Every substantial task leaves objective, changes, decisions, tests, risks, artifacts and next steps.

## Definition of done
Acceptance criteria pass; affected tests and CI pass; documentation is synchronized; provenance and rights are recorded; unrelated work remains intact; and a future contributor can continue without hidden context.
