# Portfolio Deep-Audit Snapshot — 2026-11-08

**Scope:** read-only source-tree and key-file review of the five non-empty sibling repositories, plus the active HAA-D-3 repo. This is deeper than README-only triage, but it is not a complete source audit, security assessment, or independently executed test run. Findings are based on repository trees, key source/docs, CI definitions, and recorded project status.

## Executive classification

| Repository | Evidence observed | Current classification | Main risk / next gate |
|---|---|---|---|
| `1` — SOVEREIGN Workbench / UGI | Android Kotlin source and unit tests; UGI Python source, release/SBOM docs, acceptance policy, CI workflows; project status records prior passing test/build runs | Active, multi-component; UGI alpha candidate, Android preview | License grant unresolved for SOVEREIGN OS; UGI alpha.7 archive not yet published/fetched back; physical-device/offline, secure credential storage, complete SBOM, independent security review and signing remain open |
| `4` — SSG | Python package `src/ssg`, schemas, examples, tests, docs; CI workflow for Python 3.11 | Active reference-core prototype / specification | Root license TBD; must verify actual test run against current revision; no lossless reconstruction claim until round-trip tests cover source bytes and hashes; graph projection remains separate from backup |
| `SssssssskiLLL` | Repository Intelligence Archive docs, methodology, comparative matrices, source and test registers; explicit L0-L4 evidence model | Research/archive asset, not one executable product | Test counts are heuristic path counts and marked NOT RUN; upstream licenses, revisions, vendored assets and provenance need repo-by-repo validation before reuse |
| `STD` — Studio & Technical Direction | Research baseline, proposed engine map, skill matrix, integrations and phase handoff; no implementation root/tests at inspected snapshot | Research-only / MVP candidate | No license identified; no engine install, render, benchmark or core contract implementation validated. Highest value is a deterministic 2D proof before 3D |
| `VINT` — Reel Intelligence | Python package with contracts, intake, probe, catalog, extraction, analysis modules and tests; CLI entrypoints; CI includes Python matrix and native media fixture workflow; static offline web app | Implemented local-first workbench foundation; not a complete semantic media analyzer | README explicitly limits browser flow to intake/metadata and reports native media integration still NOT RUN locally; validate actual current CI and production processors, then add OCR/ASR/scene-evidence quality tests and privacy review |
| `HAA-D-3` — The Neural Odyssey | Schema-validated SceneSpec/Finding, deterministic SVG/MIDI/WAV, FFmpeg MP4 preview/release bundle, Python tests and CI | Active technical vertical slice; public episode not complete | Scientific interpretation, human approval, Blender runtime, accessibility, soundtrack/assets rights, final media QA and empirical MLMF-NX validation remain gates |

## Cross-repository boundaries (recommended; not an approved ADR)

- **HAA-D-3:** owns neural-science research claims, source evidence register, scene-level scientific mapping, episode narrative, and reviewed science-cinema release.
- **STD:** owns the generic media-workbench research and renderer-adapter/control-plane design. Do not duplicate a renderer queue or engine abstraction inside HAA-D-3 without a specific lightweight need.
- **VINT / Reel Intelligence:** owns platform-independent media intake, probe/extraction, asset catalog, timestamped evidence/claim contracts and general media analysis. HAA-D-3 may consume exported evidence manifests through a versioned interface; avoid embedding VINT’s full workbench.
- **SssssssskiLLL:** research and provenance archive; reuse its evidence taxonomy and audit methodology, not presumed upstream code.
- **SSG (`4`):** symbolic graph/provenance research; optional future adapter for provenance/visual projection. It is not a media renderer or backup system.
- **SOVEREIGN / UGI (`1`):** offline Git workbench and provider/tooling boundary. Treat as separate product/runtime; use Git bundles or documented interfaces for exchange, not shared source-tree coupling.

## Priority gates

### P0 — Safety, reproducibility, and legal clarity
1. Resolve explicit license/NOTICE posture per repository and per nested component. GitHub license metadata was null for the inspected repos; `1` documents the SOVEREIGN OS license ambiguity and `4` states its license is TBD. Do not assume public visibility grants reuse rights.
2. On `1`, publish UGI alpha.7 archive, verify remote SHA-256, execute hosted Python matrix, official CycloneDX schema validation and Android physical-device acceptance before release.
3. For HAA-D-3, keep the scientific claim → evidence → scene mapping and human-review gate mandatory; generated preview/bundle is not a peer-reviewed episode.
4. For VINT, treat untrusted media as hostile input: bounded duration/frame count/size/timeouts, no shell, no source mutation, no unrestricted URL fetching, and tests for cleanup on failure.

### P1 — Shortest useful media vertical slice
1. STD: render a deterministic 5–10 second 2D vector motion graphic with SVG/PNG → frame sequence → FFmpeg MP4, probe output, calculate expected frame count, hash artifacts, and repeat the build.
2. HAA-D-3: apply that generic proof only via a small adapter or external job contract; first produce one 30–60 second educational clip with evidence annotations, narration/captions, mobile-safe composition, and review checklist.
3. VINT: integrate with HAA-D-3 using a versioned exported manifest (asset hash, time ranges, extraction provenance, claim/evidence references); do not depend on platform URLs as the primary input.
4. Record benchmark environment, CPU/RAM, render duration, versions and output checksums. CI-green code is not the same as acceptable creative quality.

### P2 — Broader feature roadmap
- Motion Canvas / Remotion for templated branded/social derivatives only after core contracts and benchmarks.
- Blender headless renderer for 3D cinematic shots after 2D proof and CPU/RAM/time ceilings.
- Add subtitles, audio normalization, loudness/peak checks, safe-area and aspect-ratio derivatives (16:9 master; separately composed 9:16 Shorts/Reels), accessibility and rights manifests.
- Do not add SaaS, distributed workers, multi-agent orchestration, platform scraping or paid model dependencies until a demonstrated workflow needs them.

## Confidence and limits

- High confidence: repository trees and inspected files exist at the time of this snapshot; listed paths and stated documentation are observed.
- Medium confidence: classification and boundary proposals based on current structure, selected docs, and CI definitions.
- Not established here: current CI pass state for every sibling repository, exhaustive source-level security, dependency-license closure, test coverage, device/runtime performance, deployment, production quality, or legal compliance.
- No sibling repository was modified in this audit. All recommendations remain proposals for owner review.
