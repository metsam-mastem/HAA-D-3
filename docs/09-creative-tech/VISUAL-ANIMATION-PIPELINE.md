# Visual & Animation Pipeline — Code, Prompts, Production
**Status:** proposed; no animation rendered.

## Purpose
Translate validated concepts and typed data into diagrams, procedural motion, storyboards, and eventually a three-chapter educational/cinematic series. Rendered art is a projection, not evidence.

## Pipeline
Research card + data → scientific review → scene-spec JSON → procedural geometry → SVG/3D scene → camera/lighting → motion/timing → music cue sheet → render → editorial/scientific QA → accessible export.

## Candidate tools
Python/SVG for deterministic diagrams; Graphviz/Mermaid; Blender Python API; Three.js/WebGL; Houdini (commercial terms); Unreal (terms); FFmpeg for assembly after rights checks; generative tools for concept frames only with provenance.

## Scene schema (draft)
Scene ID; concept IDs; evidence IDs; metaphor disclaimer; primitives; node/edge map; camera; lighting; FPS/duration; keyframes/easing; color semantics; labels; audio cue ID; format; review state.

## Prompt-to-animation workflow
1 Write a brief with intended meaning and sourced facts.
2 Separate observation from metaphor.
3 Storyboard establishing/explanation/close-up/transition/summary shots.
4 Separate style, camera, motion and negative constraints.
5 Produce concept keyframes as appropriate.
6 Convert validated graph/data to procedural animation.
7 Version prompts/assets and manifest; no copyrighted track files in repo.
8 Preview at low resolution, review labels/fidelity, then render final.
9 Sync to cue sheet only after BPM/runtime/rights verified.
10 Archive scene config, tool version, hash and review decision.

## Prompt template
Subject: spatial neural graph with explicit xyz coordinates.
Scientific constraints: edges exactly match adjacency; no invented links; axes described as abstract coordinates; feedback arrows distinguished from forward flow.
Style: cinematic scientific visualization, restrained glow, clear depth and legible labels.
Camera: slow orbital motion; topology remains locked.
Motion: activation pulses follow supplied time-series; pulse intensity only encodes activation; fixed legend.
Negative constraints: no biological realism claims, arbitrary brain folds, hallucinated labels or unsupported numbers.
Output: storyboard/preview with provenance ID.

## Music cue sheet
Track URL/title/artist; version/runtime; verified BPM/meter; cue in/out; scene/episode; transition; rights and sync status. BPM UNKNOWN until measured. SoundCloud link does not grant synchronization or redistribution rights.

## QA
Scientific correctness; source traceability; text legibility; color semantics; motion continuity; accessibility; provenance; music rights; unsupported inference.