# Scientific-to-Cinema Production Pipeline

## Pipeline
1. Question: define audience, scientific question and learning outcome.
2. Research pack: collect primary sources, datasets, methods, caveats and licenses.
3. Claim ledger: classify each claim as OBSERVED, REPRODUCED, MODEL_OUTPUT, HYPOTHESIS, INTERPRETATION, METAPHOR or UNKNOWN.
4. Formal model: define variables, units, equations, assumptions, boundary conditions and numerical method.
5. Experiment: capture configuration, seed, environment, logs and outputs.
6. Validation: compare with analytical solutions, benchmarks, published results or independent measurements.
7. SceneSpec: map approved variables/events into visual properties through explicit transforms.
8. Storyboard: define acts, shots, narration, camera, rhythm, sound and transitions.
9. Production: generate assets and render frames deterministically.
10. Post-production: composite, edit, mix, subtitle and encode.
11. QC: scientific, visual, audio, accessibility and rights review.
12. Release: package video, sources, credits, project files, render settings and limitations.

## Shot specification
Each shot records shot_id, scene_id, duration, aspect ratio, frame range, narrative purpose, evidence references/class, visual objects/data bindings, camera, lighting, motion, narration/music/effects, transitions and acceptance criteria.

## Visual truth policy
A visual may be Literal, Analytical, Explanatory or Metaphorical. Never present metaphor as anatomy or measurement. Link literal/analytical visuals to their source and transform.

## Renderer strategy
Browser SVG/Canvas for quick review; Manim for equation-led 2D explanation; Blender for 3D cinema; VTK/PyVista for scientific volumes/meshes; FFmpeg for deterministic assembly and QC. Keep adapters separate from scientific models.

## Audio
Specify tempo, meter, harmonic language, energy curve, density, register, instrumentation and silence where useful. Synchronize cues to scene events. Keep music, ambience, effects and narration stems separate. Record composer/source, license and edit permissions. Neuroscience of music informs hypotheses; it does not prescribe universal emotional response.

## Export and QC
Record codec, container, frame rate, resolution, color management, audio sample rate, loudness target, subtitles and checksum. Review representative frames, audio sync, dropped frames, clipping, text safe areas and scientific labels.
