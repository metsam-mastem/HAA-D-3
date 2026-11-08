# Project Continuity, Knowledge Ingestion and Handoff Protocol

**Status:** Mandatory operating rule  
**Purpose:** Prevent loss, scattering, duplication, context drift and unsafe restructuring as HAA-D-3 grows or work moves between models, agents and human contributors.

## 1. Standing instruction — never lose project knowledge
Every durable discovery, research result, design decision, requirement, code change, experiment, asset, test result and unresolved issue must be captured in the repository in its correct location. Chat messages are not the system of record.

This is a persistent project rule. Every future contributor and AI agent must read and follow this document.

## 2. What goes where
| Information | Canonical location |
|---|---|
| Mission, scope, architecture, workflows | docs/ |
| Research notes and source-backed findings | research/ |
| Dataset/model/experiment cards | research/datasets/, research/models/, research/experiments/ |
| Machine-readable contracts | schemas/ |
| Core implementation | src/haa_d3/ |
| Provider, renderer, simulator and storage integrations | adapters/ |
| Tests and fixtures | tests/ |
| Examples and reproducible tutorials | examples/ |
| Storyboards, shot plans, creative briefs | creative/ |
| Scene specifications | scenes/ |
| Small runnable demos | demo/ |
| Large renders, footage and derived binaries | artifacts/ or external storage; Git manifest only |
| Architectural decisions | docs/16-decisions/ |
| Delivery notes and release evidence | releases/ |
| Temporary scratch work | local scratch only; promote durable findings before handoff |

## 3. Required ingestion workflow
1. Identify the artifact type and owner.
2. Inspect the source and preserve the original.
3. Record provenance: source, author, date, version, license, checksum and acquisition method where applicable.
4. Extract durable facts, requirements, assumptions, findings and open questions.
5. Classify evidence and confidence; separate observation from interpretation and metaphor.
6. Check for duplicates and existing canonical documents.
7. Add or update the canonical file without deleting history.
8. Update docs/README.md and relevant cross-links.
9. Add tests, schema validation or reproducibility evidence when applicable.
10. Record the change in a handoff note and commit with a focused message.

## 4. Mandatory handoff record
Every substantial task ends with a record containing:
- Task ID, date, contributor/agent and branch.
- Objective, scope and non-goals.
- Sources inspected and artifacts ingested.
- Files created/updated and why.
- Decisions and their ADR links.
- Commands/tests executed and exact results.
- PASS / FAIL / NOT RUN / BLOCKED statuses.
- Known limitations, risks and unresolved questions.
- Next recommended task and acceptance criteria.
- Commit SHA and relevant links.

Template: docs/13-planning/HANDOFF-TEMPLATE.md.

## 5. Rules for multiple models and agents
- The repository is the shared source of truth; chat context is not authoritative.
- Every agent reads AGENTS.md and this protocol before acting.
- Agents must announce scope and avoid overlapping writes.
- One owner per file/work package at a time.
- Use branches and pull requests; do not concurrently rewrite the same document.
- Agents must not invent prior decisions. If context is missing, inspect records or mark UNKNOWN.
- Agent-generated content is a draft until reviewed according to evidence and quality rules.
- Do not let one model's assumptions become requirements without a recorded decision.

## 6. Research and code preservation
- Keep raw source material separate from summaries and derived outputs.
- Store citations and source snapshots/locators when rights permit.
- Keep reproducible commands, dependency versions, seeds and checksums.
- Do not commit huge or restricted datasets; add a manifest and retrieval instructions.
- Never replace a working implementation with pseudocode or a stub without explicit approval.
- Do not claim execution or validation based only on code inspection.

## 7. Repository organization and evolution
- Every directory has a README when its purpose is not obvious.
- Prefer stable names and numbered documentation domains; avoid deep nesting without need.
- Move files only with link updates and a migration note.
- Archive superseded documents; do not silently erase them.
- Keep one canonical source for each policy or contract and link to it elsewhere.
- New dependencies require purpose, license, maintenance, security and platform review.

## 8. Completion checklist
- [ ] All durable findings and outputs are in the repository.
- [ ] Original source and provenance are preserved.
- [ ] Correct canonical location selected.
- [ ] README/index/cross-links updated.
- [ ] Tests and evidence recorded honestly.
- [ ] Handoff note completed.
- [ ] No user work or unrelated file was deleted.
- [ ] Next owner can continue without relying on hidden chat context.

## 9. Reminder to future contributors
Before ending a task, ask: **What did I learn or create that the next person would need?** If the answer is anything beyond the code diff, record it. This applies to every model, agent, developer, researcher and creative contributor.
