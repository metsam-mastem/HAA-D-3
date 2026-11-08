# HAA-D-3 — Compressed Delivery Plan

**Delivery target:** a reproducible, reviewable scientific-to-cinematic vertical slice, not a claim that a feature-film production is complete.

## Phase A — Reproducible contracts and numerical core
- JSON Schema validation at runtime and in CLI.
- Deterministic Kuramoto simulation.
- Independent pairwise implementation, analytical K=0 case and convergence checks.
- Provenance-aware SceneSpec.
- Gate: full test suite and CI pass.

**State:** PASS in current implementation.

## Phase B — Executable media vertical slice
- Renderer-neutral SceneSpec to deterministic SVG frame sequence.
- Explicit MIDI data-sonification mapping from the order parameter.
- Synthesize deterministic WAV data-sonification; encode an H.264/AAC MP4 preview from SVG frames with FFmpeg/CairoSVG.\n- Bundle simulation, SceneSpec, SVG/MP4/WAV/MIDI outputs and SHA-256 artifact inventory.
- Gate: release archive opens, required artifacts exist, tests pass, checksums are recorded.

**State:** PASS — Quality Gate run 42465542376 ran 33 tests, encoded and checked an MP4/WAV/MIDI release bundle, and uploaded the ZIP artifact.

## Phase C — Optional 3D production adapter
- Blender background adapter creates editable scene, animated oscillator objects, coherence ring and PNG sequence.
- Gate: execute in a pinned Blender version, compare frame count and render manifest, inspect frames and confirm no unsupported scientific depiction.

**State:** PASS — Blender 4.0.2 / BLENDER_EEVEE executed in GitHub Actions. 11 PNG frames at 1920×1080 were rendered and assembled into an H.264/AAC MP4 with deterministic Kuramoto order-parameter WAV sonification. FFprobe and full FFmpeg decode passed; audio/video duration delta was 0.02 s. Hashes, dimensions, frame count and saved .blend reopen passed; original factory Cube/Camera/Light were preserved and restored. Run [42473039140](https://github.com/metsam-mastem/HAA-D-3/actions/runs/42473039140); evidence artifact ID 13614063107 (10,937,896 bytes).

## Phase D — Production acceptance and release
- Scientific review of model assumptions and selected source/data.
- Creative, accessibility, audio and rights review.
- Cross-platform render smoke tests and reproducibility check.
- Versioned release with credits, license decisions, source pack, checksums and known limitations.
- Gate: signed review checklist and immutable release artifact.

**State:** NOT RUN. Human review and project-owner licensing decisions are required.

## Critical path
A → B → C → D. Phases A and B are software gates. Phase C depends on an available Blender runtime. Phase D cannot be auto-approved by CI; it requires domain review and rights decisions.

## Status semantics
PASS means evidence exists. IMPLEMENTED means code exists but its runtime gate has not necessarily run. NOT RUN means no execution evidence. BLOCKED means an external dependency or approval is missing.
