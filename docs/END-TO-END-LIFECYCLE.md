# HAA-D-3 End-to-End Lifecycle

**Canonical operating specification · Version 0.2.0**

## Purpose
Make every output traceable from the initial question to a reproducible release. HAA-D-3 is one production system: Research Engine → Computational Engine → Knowledge & Scene Bridge → Creative Production Engine.

## Lifecycle and release gates

| Gate | Stage | Required input | Required output/evidence | Exit condition |
|---|---|---|---|---|
| G0 | Intake | User brief/question | Work ID, owner, scope, non-goals, acceptance criteria | One accountable owner and bounded scope |
| G1 | Research | Question/search strategy | Source register, claim ledger, source quality, rights | Claims traceable; uncertainty explicit |
| G2 | Formalization | Approved claims/hypothesis | Variables, units, equations, assumptions, model contract | Independent reviewer can reproduce definition |
| G3 | Experiment | Model, data, configuration | Versioned config, seed, environment, logs, metrics, hashes | Reproducible behavior or explained stochasticity |
| G4 | Validation | Experiment outputs | Analytical checks, convergence, baselines, ablations, independent comparison | Thresholds met or deviation documented |
| G5 | Scene compilation | Approved findings/model outputs | Versioned SceneSpec, mapping table, provenance links | Scene validates; each binding has a declared transform |
| G6 | Story design | SceneSpec, audience, learning goal | Storyboard, shot list, timing, narration and sound cues | Scientific and creative intent reviewable |
| G7 | Production | Approved scene/shot package | Assets, render settings, renderer logs, media outputs | Reproducible render; rights cleared |
| G8 | Quality control | Candidate media | Scientific, visual, audio, accessibility, technical and rights review | Release-blocking checks PASS |
| G9 | Release | Approved media/source package | Versioned release, checksums, credits, limitations, reproduction steps | Release manifest complete |
| G10 | Learning loop | Release and feedback | Retrospective, issues, decision updates, next hypotheses | Findings feed the backlog |

A gate may be BLOCKED with a named dependency; it may not be bypassed by relabeling a result.

## Required work-package record
Each work package records: work ID, title, accountable owner, status, priority, problem/question, scope, non-goals, dependencies, input artifact IDs/versions, acceptance criteria, verification method, decision/reviewer links, output artifact IDs/checksums, risks, limitations, next action and handoff.

## Evidence and scene contract
Allowed evidence classes: OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR, UNKNOWN.

Every scene binding declares:
- source reference and exact source field;
- source unit (or explicit unitless);
- transform ID/version and parameters;
- target scene property;
- evidence class and interpretation mode;
- validation test, reviewer or artistic rationale.

Interpretation modes: LITERAL, ANALYTICAL, EXPLANATORY, METAPHORICAL. Renderer changes may alter presentation, not source meaning. A changed mapping gets a new transform version and downstream regeneration.

## Verification pyramid
- Unit: contracts, transforms, numerical kernels, deterministic serialization.
- Integration: CLI, schemas, adapters, import/export and artifact manifests.
- End-to-end: one research item through validation, SceneSpec, renderer and QC.
- Scientific: analytical solutions, timestep refinement, convergence, baselines, uncertainty and independent implementation.
- Creative/technical: continuity, legibility, frame timing, audio sync, encoding and rights.

PASS applies only to the exact check and commit recorded. Green CI does not validate scientific interpretation, creative quality or legal rights.

## Failure and rework
Preserve failing inputs, logs and hashes; classify deviation; create a bounded corrective task; add/update tests and acceptance criteria; rerun failed and affected downstream gates; mark old outputs superseded or withdrawn. Never silently overwrite a released artifact.

## Release package
Include media, source project/SceneSpec, research references, model/experiment config, renderer/dependency versions, credits/licenses, QC report, checksums, limitations and reproduction instructions. Large media belongs in release/artifact storage; Git tracks manifests and lightweight reproducible inputs.

## Current implementation boundary
Implemented and covered by the repository Quality Gate: Python contracts/CLI, JSON Schema runtime validation, Kuramoto prototype, independent numerical checks (pairwise reference, analytical zero-coupling case and Heun convergence), research-to-scene mapping, deterministic knowledge-graph SVG projection, provenance receipts, SVG frame rendering, MIDI/WAV sonification, MP4 preview generation and reproducible ZIP release bundling.

Implemented but not fully runtime-verified: Blender background-render adapter. Its source compiles in CI; Blender itself is not installed/executed in the current Quality Gate, so scene preservation, render behavior and output quality remain NOT RUN.

Not implemented as complete production capabilities: full research/source/claim registry, complete automated scientific validation and uncertainty workflow, Manim adapter, synchronized multitrack audio timeline, full browser-to-media E2E workflow, professional editing/compositing, human creative/scientific/rights QC and production release approval.

Current hardening branch additionally introduces bounded graph, simulation and SVG rendering budgets; stricter finite-value and root-type validation; Blender SceneSpec preflight and preservation of unowned Blender objects; security reporting guidance; Dependabot; CODEOWNERS routing; and commit-SHA-pinned Node 24 compatible workflow actions. These changes remain subject to PR review and full Quality Gate verification until merged.


## Conversation-derived requirement traceability

The gate model above is the canonical process contract. The recovered user-intent register and current omissions are tracked separately in [Conversation Requirements and Gap Audit](13-planning/CONVERSATION-REQUIREMENTS-AND-GAP-AUDIT.md). Every substantial work package should reference one or more CR-xx requirement IDs from that audit and satisfy the continuity/handoff protocol. This avoids treating a lifecycle diagram or CI green status as evidence that the user's broader creative, research, account-wide repository, animation, soundtrack or release objectives are fulfilled.

At minimum, reconcile the audit register at each milestone and release. If a requirement changes, record the source and decision; if it is deferred, assign a status and next action; if it is complete, link the evidence artifact and exact verification. The E2E production path is accepted only after a real representative item traverses research/formalization/experiment/validation/SceneSpec/story/renderer/QC with provenance and release evidence.
