# Creative, Educational, and Cinematic Content Pipeline

**Project:** HAA-D-3 — The Neural Odyssey  
**Status:** Research-backed proposal; implementation gates not yet accepted  
**Updated:** 2026-11-08

## 1. Goal and scope

Build a reproducible pipeline that converts a scientifically reviewed idea into:
- a cinematic long-form YouTube episode,
- derivative YouTube Shorts and Instagram Reels,
- educational diagrams/visual assets,
- source-linked, rights-aware release bundles.

This document defines a target workflow. It does **not** claim Blender/Manim/Remotion production validation or human scientific/creative approval until an actual render and review are logged.

## 2. Recommended renderer architecture

Use a renderer-neutral SceneSpec/Storyboard contract, then route each scene to a specialist adapter. Keep source code, editorial metadata, asset manifest, and render parameters versioned; keep large generated media outside ordinary Git history (artifact storage/release bundle).

| Output / scene type | Candidate | Reason | Validation still required |
|---|---|---|---|
| Math, neural dynamics, scientific plots | Manim Community | Precise code-authored explanatory animation | Install/health check, sample scene, render time and legibility benchmark |
| Cinematic 2D/3D sequences, camera, light, compositing | Blender | Broad scene and animation capability | Headless smoke render; render determinism; resource/time budget |
| Text, titles, brand templates, reusable data-driven compositions | Remotion | React-based compositions and templating | Licensing review, dependency pinning, render comparison |
| Assembly, transcode, audio mix, subtitles, vertical crops | FFmpeg | CLI backbone for repeatable media packaging | Validate codec/profile, audio loudness, subtitle burn-in, crop safety |
| Web interactive visualizations | Three.js | Browser/WebGL visual exploration | Browser/device performance and fallback accessibility |

**Initial practical stack recommendation:** Manim Community for scientific sequences + Blender for cinematic shots + FFmpeg for assembly/delivery. Add Remotion when branded templated derivatives become a repeated need. Do not require all renderers in the MVP.

## 3. Stage-gated production pipeline

| Gate | Work | Required artifact | Exit condition |
|---|---|---|---|
| G0 — Brief | Audience, learning objective, format, duration, language, platform | `brief.yaml` | Owner approves scope |
| G1 — Evidence | Literature search, source capture, claims and uncertainty | `evidence-register.csv` + claim ledger | Every factual claim has traceable source; unresolved claims flagged |
| G2 — Script | Hook, narrative arc, narration, chapter beats | `script.md` | Science reviewer and editor approve |
| G3 — Storyboard | Scene purpose, visuals, timing, voice, transition, renderer | `storyboard.yaml` | Each scene has one core learning point and defined source/visual mapping |
| G4 — Design | Style frame, palette, type, motion rules, accessibility | `visual-bible.md` + approved style frame | Visual direction locked |
| G5 — Asset prep | Asset IDs, origin, author, license, attribution, modifications | `asset-manifest.csv` | Rights status known for every included asset |
| G6 — Build | Generate scene code, data visualizations, sound cues | Versioned scene sources | Schema/lint checks pass |
| G7 — Preview render | Low-resolution/short test render | Preview MP4 + render log | Technical QA and narrative review pass |
| G8 — Final render | Full quality, voice/music mix, subtitles | Master MP4 + SRT/VTT + metadata | Render complete; hashes and provenance captured |
| G9 — QC | Science, edit, sound, visual, accessibility, platform checks | QC report/checklist | No blocker; owner signs off |
| G10 — Derivatives/release | 16:9 master, 9:16 short, 1:1/4:5 variants, thumbnails | Release bundle + publishing copy | Correct dimensions, rights, captions and title/description |
| G11 — Learn | Analytics and review notes | Post-release review | Insights converted into versioned backlog/rules |

### Required SceneSpec fields (minimum)

- `scene_id`, `chapter`, `duration_seconds`, `learning_objective`
- `narration` and narration timing (or explicit silent-scene marker)
- `visual_type` and renderer adapter identifier
- data values, units, and evidence-source IDs where scientific
- `camera/motion` directives or keyframes
- `transition_in/out`, `audio_cues`, `caption_text`
- `safe_area`, `aspect_ratio_targets`, `accessibility_notes`
- `review_status` and deterministic render settings

Model-generated output should be constrained to validated SceneSpec, not unrestricted code execution. Renderer code is authored/reviewed in controlled source files.

## 4. YouTube and Instagram output strategy

| Derivative | Aspect / canvas | Editorial use |
|---|---|---|
| YouTube episode | 16:9, 1920×1080 baseline | Complete narrative, citations and full context |
| YouTube Shorts | 9:16, 1080×1920 baseline | One self-contained concept, immediate hook, concise payoff |
| Instagram Reels | 9:16, 1080×1920 baseline | Strong first seconds, prominent captions, vertical-safe layout |
| Feed visual/card | 1:1 or 4:5 | Key diagram, chapter announcement, takeaway |
| Thumbnail | Platform-specific template | One focal point, concise title, contrast and visual consistency |

Keep important text/diagram labels inside a configurable vertical safe region; never merely center-crop a 16:9 scientific scene. Generate a separate framing plan per target. Platform dimensions and publishing limits must be rechecked against official current platform guidance before release.

## 5. Scientific visualization and editorial QA

Apply these review principles:
- Communicate the takeaway and comparison before adding decorative complexity.
- Label axes, units, scales, baselines, data provenance, and uncertainty where applicable.
- Avoid misleading perspective, truncation, or color encoding that changes the apparent magnitude.
- Use color palettes that remain interpretable for color-vision differences; pair color with shape, label, or line style.
- Ensure text size and contrast remain legible at mobile viewing scale.
- Distinguish observed data, simulation, conceptual illustration, and speculative visualization.
- Preserve source values and provide a reproducible data-to-visual mapping.
- Have a subject-matter reviewer approve science-sensitive scenes.

Reference: Jambor, “A checklist for designing and improving the visualization of scientific data,” Nature Cell Biology (2025), https://www.nature.com/articles/s41556-025-01684-z . Also Fujii, “How to design effective scientific figures,” Nature Human Behaviour (2026), https://www.nature.com/articles/s41562-026-02466-9 .

## 6. Research and GitHub discovery register

Candidate projects to evaluate, not automatically adopt:
- Manim Community: https://github.com/ManimCommunity/manim — explanatory math animation; MIT.
- ManimML: https://github.com/helblazer811/ManimML — composable machine-learning concept visualizations; MIT.
- Paper-to-Animation: https://github.com/ayushnangia/paper-to-animation — storyboarded research-paper-to-Manim workflow; MIT.
- Science Animation Factory: https://github.com/gamehack/science-animation-factory — constrained storyboard-driven Manim production direction; verify project maturity and current implementation before reuse.
- Educational Video Pipeline: https://github.com/nafeu/educational-video-pipeline — paired Manim/Remotion and local transcription workflow; inspect dependencies/license before adopting.
- Blender: https://github.com/blender/blender — cinematic 3D and compositing; GPL-2.0-or-later.
- FFmpeg: https://github.com/FFmpeg/FFmpeg — media assembly; LGPL/GPL configuration depends on build.
- Remotion: https://www.remotion.dev/ — React video compositions; review its current license and commercial terms.

Before adoption: inspect recent commit activity, license text, dependency security, reproducible setup, tests, rendering outputs, maintenance signal, and whether it adds a capability not already in HAA-D-3 or STD. No dependency or code was imported as part of this research-only document.

## 7. Repo portfolio audit — snapshot

The accessible account inventory contained 18 repositories at the time of the audit. README-level evidence so far:

| Repository | Observed status |
|---|---|
| `1` | Prior inspection identified SOVEREIGN Workbench / UGI / SOVEREIGN OS; full content audit pending |
| `2` | Empty repository |
| `3` | Empty repository |
| `4` | Prior inspection identified SSG, Python reference core v0.5.0; deeper audit pending |
| `HTH` | Empty repository |
| `H2H` | Empty repository |
| `-JRYAN` | Empty repository |
| `JRYAN` | Empty repository |
| `RISMAAAN` | Empty repository |
| `SAEQE` | Empty repository |
| `KAAVAAK-` | Empty repository |
| `KAAVAAK` | Empty repository |
| `HAA-D-3` | Active project; recent main commit adds playable MP4 research-to-cinema preview |
| `SHEED` | Empty repository |
| `SssssssskiLLL` | Repository Intelligence Archive; README/docs index describe 8 upstream repositories across memory/context, benchmark, MCP, agent runtime, multi-agent IDE, local AI deployment and scoped-access security. Its README says code-flow deep dive and isolated test execution are not yet done in that archive. |
| `RaYa` | Empty repository |
| `STD` | Research-only media workbench baseline; MVP engine and local render validation open |
| `VINT` | Root contains `projects/reel-intelligence/WORK_REPORT_0001.md`; VINT describes Reel Intelligence as a platform-independent, local-first multimodal media analysis workbench. It is research/architecture proposal, not a production analyzer; its report prefers user-supplied media over platform URL dependence. |

“Empty” above means the repository contents endpoint explicitly returned GitHub’s “repository is empty” response. A README 404 alone is not interpreted as repository-empty. This section is the initial README/index snapshot; the subsequent source-tree/key-file review and its limits are recorded in [Portfolio Deep-Audit Snapshot](PORTFOLIO-DEEP-AUDIT-2026-11-08.md).

## 8. Prioritized implementation backlog

### P0 — prove the smallest useful vertical slice
1. First establish STD’s deterministic 5–10 second 2D SVG/PNG → frame sequence → FFmpeg MP4 proof with metadata and checksums; only then expand to the HAA-D-3 30–60 second scientific concept (no new claims without evidence).
2. Make one approved script and 5–8-scene storyboard.
3. Render a Manim test scene and Blender headless smoke scene; record machine, versions, duration, and output hashes.
4. Assemble narrated MP4 with FFmpeg and export a vertical derivative using a separate safe-area layout.
5. Run science/visual/audio/accessibility/rights checklist and record reviewer decisions.

### P1 — make it repeatable
- SceneSpec JSON Schema validation and schema version.
- Renderer adapters with common artifact metadata and failure reporting.
- Asset/evidence manifests, source attribution, license audit.
- CI: schema, lint, unit tests, lightweight render smoke tests, media metadata validation.
- Artifact storage and retention policy; avoid committing binary masters to Git.

### P2 — content factory features
- Reusable chapter templates and brand design tokens.
- Narration transcript → word-level timestamps → captions and animation cue alignment.
- Auto-generated 16:9 / 9:16 / 1:1 scene layouts with human-approved framing.
- Thumbnail and title variants, export manifests, publishing checklist.
- Feedback/analytics loop with human review; never optimize for engagement by sacrificing scientific accuracy.

## 9. Risks and non-goals

- Generative visuals can fabricate mechanisms or scientific detail: label conceptual visuals and review claims.
- Licenses of code, models, fonts, music, footage, and generated assets are independent; maintain a cue/asset sheet.
- API/AI generation is optional and must not be a required dependency of the deterministic core.
- Do not promise fully unattended cinematic release: final science, editorial, accessibility, and rights approvals remain human gates.
- This plan is not an approved product architecture until an ADR and benchmark are accepted.


## 10. Perceptual design controls — research update

Animated scientific graphics should be constrained by the task the viewer must perceive, not by how many objects the renderer can move. Jiang et al. (2026) consolidate perceptual-capacity-based guidelines for tracking, holistic judgments, and object additions/removals: https://doi.org/10.1186/s41235-026-00724-y . Operationalize this as:
- Keep simultaneously tracked moving objects to a small, deliberate set; when comparison is important, consider small multiples or staged reveals instead of fast temporal transitions.
- Slow critical transitions, hold the “aha” state, and allow replay/pause where the format permits.
- Use a single visual focal point and restrained annotation; labels should clarify the science, not become a competing overlay.
- Distinguish empirical data, model simulation, conceptual metaphor and unknown/speculative elements in both narration and asset metadata.

Cinematic 3D science communication audience research (Jensen et al.; survey experiment, n=577) found that labels raised perceived quality ratings, while many other audience outcomes did not significantly change; the paper points toward story structure, voiceover and audiovisual content as major determinants. Reference: https://pubmed.ncbi.nlm.nih.gov/39418271/ . So the editorial rubric must grade comprehension/story/narration, not label count or visual spectacle alone.
