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

Runtime-verified: Blender background-render adapter on Blender 4.0.2 / BLENDER_EEVEE in GitHub Actions. The gate rendered 11 frames at 1920×1080, verified PNG signatures/dimensions/count and SHA-256 inventory, reopened the saved .blend, and confirmed original Cube/Camera/Light objects and visibility were preserved. Render output remains RENDERED_NOT_REVIEWED; human scientific/creative/accessibility/rights approval is still NOT RUN.

Not implemented as complete production capabilities: full research/source/claim registry, complete automated scientific validation and uncertainty workflow, Manim adapter, synchronized multitrack audio timeline, full browser-to-media E2E workflow, professional editing/compositing, human creative/scientific/rights QC and production release approval.

Phase A hardening was merged to main in PR #14 (squash commit 3dc73a7). It adds bounded graph, simulation, SceneSpec keyframe and SVG rendering budgets; strict finite-value, enum, animation and root-type validation; a 16 MiB JSON input cap with duplicate-key/non-standard-number rejection; Blender SceneSpec preflight, preservation of unowned Blender objects and explicit overwrite protection; FFprobe stream checks, audio/video duration alignment and full MP4 decode verification; pip-audit and CycloneDX SBOM generation; patched setuptools build tooling; security reporting guidance; Dependabot; CODEOWNERS routing; and commit-SHA-pinned Node 24 compatible workflow actions. The full pre-merge Quality Gate passed on head efca1a5 (61 Python tests, dependency audit and release pipeline). Post-merge verification is tracked separately; Blender 4.0.2 runtime is verified by CI; human scientific, creative, accessibility and rights review remains NOT RUN.


## Conversation-derived requirement traceability

The gate model above is the canonical process contract. The recovered user-intent register and current omissions are tracked separately in [Conversation Requirements and Gap Audit](13-planning/CONVERSATION-REQUIREMENTS-AND-GAP-AUDIT.md). Every substantial work package should reference one or more CR-xx requirement IDs from that audit and satisfy the continuity/handoff protocol. This avoids treating a lifecycle diagram or CI green status as evidence that the user's broader creative, research, account-wide repository, animation, soundtrack or release objectives are fulfilled.

At minimum, reconcile the audit register at each milestone and release. If a requirement changes, record the source and decision; if it is deferred, assign a status and next action; if it is complete, link the evidence artifact and exact verification. The E2E production path is accepted only after a real representative item traverses research/formalization/experiment/validation/SceneSpec/story/renderer/QC with provenance and release evidence.
