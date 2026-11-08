# Agent and Contributor Operating Rules — HAA-D-3

This file is mandatory context for every human contributor, coding agent, research agent and creative-production agent working in this repository.

## 1. Mission
HAA-D-3 is a platform-independent scientific research, computational engineering, knowledge and cinematic-production program. It is not tied to one LLM, vendor, operating system, renderer, simulator or frontend framework.

## 2. Before changing anything
1. Read README.md and docs/README.md.
2. Read docs/00-charter/PROGRAM-OPERATING-MODEL.md.
3. Read docs/03-architecture/REFERENCE-ARCHITECTURE.md and docs/13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md.
4. Inspect the relevant code, tests, schemas, decisions and recent commits.
5. State the task scope, files to be changed, risks and acceptance checks.
6. Never assume an undocumented feature exists.

## 3. Non-destructive change policy
- Never delete, rename, overwrite or relocate existing user work without an explicit task and a migration plan.
- Prefer additive changes and focused commits.
- Do not rewrite the whole README or a document to make a small correction.
- Preserve provenance, author attribution, citations, original source material and history.
- Generated output belongs in artifacts/ or an external artifact store, not mixed into source directories.
- Do not commit secrets, credentials, private user data, huge renders, caches or temporary files.
- Do not silently change public contracts. Version schemas and document migrations.

## 4. Evidence and scientific integrity
Use only these evidence labels: OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR, UNKNOWN. A visual render is not scientific validation. A synthetic demo is not a biological simulation. Record sources, dates, versions, licenses, assumptions, uncertainty and limitations.

## 5. Architecture rules
- Core domain logic must not import a specific LLM SDK, cloud vendor, GUI, renderer or operating-system API.
- Integrations belong behind adapters and capability contracts.
- Prefer open formats and documented interchange contracts.
- Keep computation, research provenance, scene specification and presentation separate.
- Use a modular monolith until measured scale or deployment requirements justify services.
- CPU-first and offline-capable paths are preferred; GPU and remote execution are optional capabilities.
- No mandatory paid service or account is allowed in the core.

## 6. Cross-platform requirements
Every capability declares its execution requirements and supported environments. Support headless CLI and library use first; then web, desktop, mobile and render-farm adapters. Avoid platform-specific paths, assumptions about case sensitivity, shell syntax or installed codecs. Keep portable data formats and explicit export contracts.

## 7. Engineering workflow
For behavior changes: write or update tests first, implement the smallest coherent change, run tests, inspect the diff, update docs and record evidence. Do not claim tests passed unless actually run. Status values: PASS, FAIL, NOT RUN, BLOCKED.

## 8. Research workflow
Capture a source before recording a claim. Claims link to sources and methods. Research notes must distinguish primary literature, reviews, preprints, software documentation and opinion. Never invent DOIs, results, benchmark numbers or citations.

## 9. Creative workflow
Every scene records its evidence class, data bindings, visual interpretation, rights/provenance, duration, frame rate and render settings. Music and media must be original, licensed or explicitly cleared. Artistic metaphors must not be presented as measured data.

## 10. Task handoff
Every non-trivial task must leave: objective, scope, changed files, decisions, test results, remaining risks, next steps and links to artifacts. Update docs/13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md when new durable project knowledge or workflow changes are introduced.

## 11. Definition of done
A task is complete only when its acceptance criteria are met, evidence is recorded, docs are synchronized, no unrelated user work was damaged and remaining NOT RUN/BLOCKED items are explicit.
