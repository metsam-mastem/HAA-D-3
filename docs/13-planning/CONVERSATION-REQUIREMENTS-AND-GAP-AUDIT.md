# Conversation-Derived Requirements, Recovery and Gap Audit

**Audit date:** 2026-11-08  
**Scope:** HAA-D-3 requirements recoverable from the project conversation and retrieved project context.  
**Status:** Working audit; user confirmation and technical verification remain required for items marked UNKNOWN or NOT RUN.  
**Purpose:** Convert conversational intent into a durable backlog so requirements are not silently forgotten, diluted, duplicated, or mistaken for completed implementation.

> This is a requirements-recovery record, not a claim that every requested investigation or feature has already been performed. The repository is the system of record; conversation is an input source.

## 1. Executive findings

1. The user’s central creative/technical ambition is a coherent three-chapter educational/creative series built around the ordered soundtrack, with an end-to-end research-to-visual-production workflow.
2. The user also asked for deep technical exploration and engineering implementation: scientific foundations, vertical slices, reusable repositories/tools, animation-by-code and prompt-based workflows, GitHub Actions, complete documentation and GitHub publication.
3. Existing lifecycle specification `docs/END-TO-END-LIFECYCLE.md` already defines gates G0–G10. This audit complements it by mapping recovered user intent to deliverables, evidence and open gaps.
4. The latest foundation is consolidated in `src/haa_d3/`, a single test root and a single Quality workflow. CI success establishes only the checks actually executed; it does not establish scientific validity, finished media, rights clearance or complete fulfillment of the broader research request.
5. The exact working label MLMF-NX is captured in a research brief, but its acronym expansion, operational definition, architecture, experiments and results remain unresolved/not executed.
6. Public discovery of GitHub/Nature and creative portals was requested. Existing source maps are research leads; individual Dribbble/Pinterest/YouTube items are not all curated and reviewed. A comprehensive audit of all account repositories and external sources remains a separate work package.
7. Scope boundary retrieved from the conversation: inspect the user’s GitHub account; for Nature/Dribbble/Pinterest, use public discovery only for material relevant to the projects. Do not imply the user has accounts on services not stated.

## 2. Recovered intent and requirement register

Statuses: **DOCUMENTED** = represented in canonical docs; **PARTIAL** = some artifacts or initial exploration exist; **NOT RUN** = no evidence of execution; **UNKNOWN** = requires user decision or source verification.

| ID | Recovered requirement / intent | Current evidence | Status | Gap / acceptance evidence |
|---|---|---|---|---|
| CR-01 | Organize the project as a complete, coherent three-chapter series | Series Bible, 15-episode scaffold | DOCUMENTED / concept | Approved scripts, storyboard and production package per episode |
| CR-02 | Follow the supplied soundtrack ordering | Series Bible records six tracks in chapter order | DOCUMENTED | Confirm track/version/runtime, cue positions and rights |
| CR-03 | Build a research-to-cinema pipeline, not isolated visuals | End-to-End Lifecycle, SceneSpec, research-to-scene mapping | PARTIAL | One media E2E run with traceable research, experiment, scene, render and QC |
| CR-04 | Research scientific foundations and neural architecture hypotheses | Knowledge Universe, Research Plan, sources, MLMF-NX brief | PARTIAL | Source-backed claim ledger, independent review and formal definitions |
| CR-05 | Preserve and develop MLMF-NX idea | MLMF-NX Research Brief; Issue #3 | DOCUMENTED as hypothesis | Expand acronym or explicitly leave name provisional; formal model, baselines, implementation, experiments |
| CR-06 | Develop executable vertical slices | VS-01, VS-02; Kuramoto and graph-to-SVG foundation | PARTIAL | Acceptance checks, visual QA, user review and broader integration |
| CR-07 | Explore VINT or comparable repositories for reuse | VINT Reel Intelligence report inspected; reuse notes recorded | PARTIAL | Feature-by-feature capability/license/maintenance/security/fit comparison and integration decision |
| CR-08 | Explore the user’s GitHub account/repositories, not assume other connected accounts | User constraint retrieved; HAA-D-3 audited | PARTIAL | Inventory all accessible repos, classify complete/incomplete/duplicate/idea/debt; verify account coverage |
| CR-09 | Research relevant external GitHub and Nature projects | Landscape and selected citations documented | PARTIAL | Query log, source register, selection rationale, claims mapped to design choices |
| CR-10 | Explore code/prompt-based animation and production tools/pipelines | Manim, Blender, neuVid, PyVista, VTK leads in Creative Reference Map | PARTIAL | Tested tool matrix and runnable proof-of-concept pipeline |
| CR-11 | Use GitHub capabilities such as Actions and robust version control | One Quality workflow, CI gates, merged foundation PRs | PARTIAL / implemented foundation | Additional automation mapped to needs; release, artifact, issue and provenance automation |
| CR-12 | Put durable work, artifacts and documentation in GitHub | Governed docs, source map, catalog, code, schemas, examples and tests | PARTIAL / ongoing | Ensure each work package, decision, output and handoff is logged; large binaries handled by policy |
| CR-13 | Deeply document the project and prevent forgetting | Continuity protocol, handoffs, catalog, lifecycle and this audit | DOCUMENTED / process | Run the checklist at every milestone and reconcile this register with issues |
| CR-14 | Discover creative references from public sources (Nature/GitHub plus Dribbble/Pinterest etc. as project relevant) | Creative reference map contains portals and film case studies | PARTIAL | Individually curated records, creator/source, license, technique and applicability |
| CR-15 | Preserve scientific provenance and distinguish evidence from metaphor | Claim/provenance policy, lifecycle evidence classes | DOCUMENTED | Enforce on every finding and scene; reviewer sign-off |
| CR-16 | Create a reusable, modular software factory / extensible platform foundation | Source Map, adapter-first ADR, CLI/contracts | PARTIAL | Confirm whether this is HAA-D-3’s product scope or an adjacent ecosystem; explicit boundary and integration ADR |
| CR-17 | Align with adjacent ecosystem concepts (HTH, SOVEREIGN, SSG, VINT, STD and shared research/agents/verification) | Prior context proposes an ecosystem and repo reports were inspected selectively | PARTIAL / boundary unresolved | Define responsibility boundaries, interfaces, dependencies and avoid copying/duplicating sibling capabilities |
| CR-18 | Validate output quality technically, scientifically, visually, audibly and legally | Release and Quality, lifecycle gates | PARTIAL | Actual QC run, external scientific review, accessibility and license/right evidence |
| CR-19 | Define target audience, episode length, production medium, resource budget and release format | Not found as approved constraints in current reviewed material | UNKNOWN | User decision or a proposal marked explicitly as draft |
| CR-20 | Establish ownership, approval authority and milestone priorities | Work-package template exists | PARTIAL | Assign owner/reviewer, priority and deadlines for active work packages |

## 3. Recovered soundtrack and chapter sequence

The following ordering is treated as user-supplied creative input, not permission to use the tracks:

### Chapter I — THE GENESIS / پیدایش
1. Aaron — “Endless Song” by Musigen: https://on.soundcloud.com/Mqv1P2Fsc8lwdTUagf

### Chapter II — THE CONVERGENCE / همگرایی
2. “Welcome G” — Khali G x Shayan Roohi: https://on.soundcloud.com/XmVrz9jdq75DlWBpGZ  
3. “The Look” — Metronomy: https://on.soundcloud.com/ZZhZ90sOMj4V2kG8Rl

### Chapter III — THE EMERGENCE / ظهور
4. “Pain in my Heart” — Schrotthagen: https://on.soundcloud.com/tSLUbmBdLv76rPaWto  
5. “Life” — Kako Band: https://on.soundcloud.com/m26dzgMfvZUyarB2xC  
6. “Balthazar — bunker” — user799835639: https://on.soundcloud.com/ch2TtqmDfgVGQcnbVt

**Unresolved audio work:** exact track/version identity, duration, BPM/meter, cue/tempo map, license/platform terms, sync permissions, rights clearance, and alternate sound design if a track cannot be used. Do not ingest audio/lyrics/stems without rights.

## 4. Hidden, forgotten, or under-specified items

These are risks of omission discovered by reconciling the intent against current canonical docs:

- **Acronym/definition debt:** MLMF-NX name expansion and precise computational semantics are unknown. Prevent the working label from hardening into a false definition.
- **Series-to-engineering traceability:** episode cards should link each story beat to research question → claim/evidence → model/experiment → scene transform → shot → QC. The Bible provides scaffolding but not a fully populated trace matrix.
- **Music rights and timing:** a playlist order is not a synchronization plan or license.
- **External repo reuse diligence:** record license, project health, dependency/security posture, maintenance, platform compatibility, API fit, and whether reuse is approved. “Inspected” does not mean “adopted.”
- **Account-wide GitHub inventory:** a single project audit does not complete an inventory of all the user’s repositories.
- **Research query provenance:** capture exact query, search date, source inclusion/exclusion reason, and research coverage gaps to avoid repeating or assuming exhaustiveness.
- **Creative portal curation:** search portals (Dribbble/Pinterest/YouTube) are not individual vetted references; each selected item needs source/creator, technique notes, rights and originality safeguards.
- **Animation tool proof:** documentation of Manim/Blender/neuVid leads does not prove an end-to-end runnable pipeline; one representative proof is required.
- **Media E2E and QC:** currently the lifecycle’s full research→render→QC→release path is not implemented. CI’s scene/graph outputs are not a rendered episode.
- **Scientific claims and scope:** numerical verification of the Kuramoto implementation is not external scientific validation, biological evidence, or support for MLMF-NX superiority.
- **Release engineering:** define release manifest, artifact storage, checksums, reproducibility environment, captions/subtitles, accessibility, technical encoding and rollback/withdrawal.
- **Rights beyond soundtrack:** images, footage, fonts, models, datasets, software licenses, attribution and derivative-work conditions.
- **Cross-project boundary:** the wider HTH/SOVEREIGN/SSG/VINT/STD concept may be an ecosystem around HAA-D-3, not a reason to fold all responsibilities into this repository. This boundary needs an ADR.
- **Product decisions:** audience, intended format (web/interactive/video), episode runtime, budget/hardware, language/subtitles, release venue and user acceptance authority remain UNKNOWN.
- **Chat-only discoveries:** any future result from conversation must be ingested with provenance and a handoff rather than left solely in chat.

## 5. Prioritized gap backlog

### P0 — Resolve requirements and create traceability
- [ ] Confirm MLMF-NX expansion/definition or mark the label provisional.
- [ ] Add requirement IDs to work packages/issues and link them to evidence and acceptance criteria.
- [ ] Define HAA-D-3 boundary versus sibling ecosystem projects through an ADR.
- [ ] Establish target audience, output format, episode runtime, language/subtitle plan and acceptance owner.

### P1 — Research and repository audit
- [ ] Inventory every repository accessible in the user’s GitHub account; identify incomplete, dormant, overlapping, promising and high-debt projects.
- [ ] Produce a VINT/comparable-repository comparison including license, maintenance, technical fit and integration decision.
- [ ] Extend Nature/GitHub research with a reproducible query log, inclusion criteria and claim-to-source mapping.
- [ ] Curate specific creative references from the named portals rather than leaving portal searches as leads.

### P2 — Experimental rigor
- [ ] Define MLMF-NX formal model, tasks, baseline(s), ablations, metrics, compute budget, seeds and falsification criteria.
- [ ] Implement and run at least one reproducible experimental vertical slice.
- [ ] Separate software verification, model performance, empirical validity and external scientific review.

### P3 — Production proof
- [ ] Create one representative scene/shot pipeline (research/model output → SceneSpec → Manim or Blender renderer → media QC).
- [ ] Add scene-to-episode traceability and versioned shot/cue sheets.
- [ ] Resolve soundtrack and all asset rights; prepare audio cue/tempo map.
- [ ] Execute a full media E2E and record render logs, checksums, accessibility and QC.

### P4 — Release and continuity
- [ ] Define release manifest, artifact storage, reproducibility instructions, captions, credits, limitations and rollback.
- [ ] Add a recurring audit cadence and require register reconciliation in each handoff.
- [ ] Convert accepted gaps into GitHub Issues with priorities, dependencies and explicit acceptance criteria.

## 6. Anti-forgetting checklist for each work package

- [ ] Link one or more requirement IDs (CR-xx).
- [ ] Declare scope, non-goals, owner, reviewer and dependencies.
- [ ] Record source links, dates, provenance, license and confidence.
- [ ] Choose the canonical repository location; avoid parallel copies.
- [ ] Define acceptance criteria before implementation.
- [ ] Preserve inputs/configuration/seeds/environment and output hashes when reproducibility applies.
- [ ] Run relevant tests and record exact PASS/FAIL/NOT RUN/BLOCKED.
- [ ] Distinguish observed facts, reproduced results, model outputs, hypotheses, interpretations, metaphors and unknowns.
- [ ] Update index, catalog, changelog, issues and handoff as appropriate.
- [ ] Identify downstream consumers (research, scene, episode, renderer, release).
- [ ] State what remains unfinished and the single next action.

## 7. Relationship to canonical lifecycle

Use `docs/END-TO-END-LIFECYCLE.md` as the process/gate specification G0–G10. Use this document as the conversation-derived requirement and gap register. Use `docs/13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md` to ingest each result and `docs/13-planning/DOCUMENT-CATALOG.md` to keep the inventory exact.

The E2E lifecycle is not “complete” merely because this document exists. Completion requires evidence from a real work package traversing the relevant gates, including end-to-end media QC for the production path.
