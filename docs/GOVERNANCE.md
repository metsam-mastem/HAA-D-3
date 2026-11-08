# HAA-D-3 Repository Governance and Team Operating Rules

**Canonical governance standard · Version 0.2.0**

## Single-project rule
HAA-D-3 is one program. Work is organized by capability and deliverable, not by whichever contributor or AI agent starts it. No agent may establish a parallel project root, duplicate package, competing documentation index or unreviewed contract.

## Accountability

| Role | Accountability |
|---|---|
| Project owner | Mission, scope, priorities, license and irreversible decisions |
| Work-package owner | One accountable owner per bounded deliverable |
| Domain reviewer | Research, numerical, software, creative or rights review |
| Integrator | Contract compatibility, dependency direction, tests and release evidence |
| Contributor/agent | Assigned scope only; complete handoff |

AI agents are contributors, not project owners. One person may hold multiple roles, but every work package has exactly one accountable owner.

## Canonical-source rules
1. One Python package: src/haa_d3/.
2. One Python test root: tests/.
3. One documentation navigation index: docs/README.md.
4. One tracked-Markdown inventory: docs/13-planning/DOCUMENT-CATALOG.md.
5. One current task/decision record per work package; old handoffs remain historical.
6. One quality workflow: .github/workflows/quality.yml.
7. Integrations are adapters, never alternate cores.
8. Generated output never belongs in source or test directories.

## Work intake
Every non-trivial task starts with problem/value, accountable owner/reviewer, bounded scope/non-goals, affected paths/contracts, dependencies/risks, acceptance criteria, verification commands, expected artifact and handoff.

Before implementation inspect current branch and source. For behavior changes use RED → GREEN → REFACTOR. Code creation alone does not mean completion.

## Branch and review policy
Use feat/, fix/, research/, creative/, docs/ and foundation/ prefixes. Never work directly on main. Keep PRs focused and update source map/index/catalog after structural changes. No agent merges a PR unless the owner explicitly instructs it.

## Decision authority
Mission, product boundaries, license, data sharing and paid-service decisions require owner approval. Architecture decisions are ADRs with context, options, consequences and status (Proposed, Accepted, Superseded, Rejected). Contributors may propose but cannot silently accept an ADR. Contract changes require schema version, migration notes, examples and compatibility tests.

## Evidence and status
Evidence classes: OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR, UNKNOWN.
Work statuses: PASS, FAIL, NOT RUN, BLOCKED, DRAFT, IN REVIEW.
PASS requires an executed check and commit/evidence link. NOT RUN is not a soft pass. BLOCKED requires a named dependency and next action. Green CI proves only the checks it actually ran.

## Anti-sprawl controls
Reject or redesign changes that add a second core package/test root; duplicate a policy without canonical link; create an undocumented top-level directory; import renderer/provider SDKs into domain logic; make a paid external service mandatory; add tools without a concrete workflow and acceptance test; or leave temporary/generated files in tracked source.

## Definition of done
Acceptance criteria pass, tests/evidence are recorded, documentation is synchronized, provenance/rights are known, unrelated work is preserved and the next owner can continue from the handoff without hidden context.
