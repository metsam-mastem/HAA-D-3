# HAA-D-3 Reference Architecture

**Status:** Proposed architecture; not a complete implemented platform.

## Principles
- Modular monolith first; split services only when evidence justifies it.
- Python for research, numerical computation, data processing and orchestration.
- Versioned JSON for experiment configurations and scene specifications.
- Blender for initial high-quality 3D production; browser SVG/Canvas/WebGL for lightweight explainers.
- Research models remain independent of renderers.
- Reproducibility, provenance and uncertainty are first-class data.
- CPU-first with optional GPU acceleration; profile before optimizing.
- No mandatory paid APIs in the core.

## Logical planes
1. Research: source registry, claim ledger, dataset catalog, experiment and model registries.
2. Computation: numerical kernels, graph/dynamics models, simulator adapters, runners, profiler and validators.
3. Knowledge: typed entities/relations, provenance graph, evidence status, units, coordinate systems and time metadata.
4. Scene: SceneSpec, object registry, geometry, materials, camera, lighting, motion and annotations.
5. Production: storyboard, shots, timeline, rendering, compositing, audio stems, subtitles, export and QC.
6. Interface: research workbench, experiment console, interactive viewer, scene editor and artifact browser.

## Core contracts
**Finding:** id, title, statement, evidence_class, source_ids, method, uncertainty, limitations, version.  
**Experiment:** id, question, hypothesis, model_id, dataset_ids, config, seed, environment, metrics, artifacts, status.  
**Model:** id, name, version, family, assumptions, input_schema, output_schema, validation_status.  
**SceneSpec:** schema_version, scene_id, title, evidence_refs, interpretation_mode, duration, frame_rate, canvas, objects, camera, lighting, motion, annotations, audio_cues.  
**RenderArtifact:** artifact_id, scene_id, scene_spec_hash, renderer, renderer_version, settings, output_uri, checksum, qc_status.

## Scene bridge
Accept only approved findings, model outputs, hypotheses or explicitly marked metaphors. Every mapping records input field/unit, visual property, transform and parameters, evidence class, author/version and validation test or artistic rationale.

## Candidate adapters
| Capability | Candidate | Role |
|---|---|---|
| 2D mathematical animation | Manim Community | Equations and explanatory motion |
| 3D cinema | Blender | Modeling, animation, camera, lighting, compositing |
| Neural circuit visualization | Neural Circuit Visualizer, neuVid | Research precedents |
| Biophysical simulation | Jaxley, Brian2 | Optional research backends |
| Geometric graph learning | PyTorch Geometric / MARBLE | Research methods |
| Scientific 3D data | VTK / PyVista | Volumes and meshes |
| Browser interaction | SVG / Canvas / Three.js | Lightweight explainers |
| Media assembly | FFmpeg | Audio/video export |

These are candidates, not adopted dependencies. Verify license, maintenance, compatibility and hardware needs before integration.

## Repository boundaries
docs/, research/, schemas/, src/haa_d3/, adapters/, examples/, demo/, tests/, artifacts/, decisions/ and .github/workflows/. Keep large renders outside Git unless there is a specific reason.

## Security
Validate imported files, schemas, sizes and paths. Do not execute arbitrary generated Python. Prefer constrained scene specifications and approved renderer operations. Keep credentials outside version control.
