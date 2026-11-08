# Blender adapter

**Status:** implemented as an optional adapter; Blender runtime execution is **NOT RUN** in the repository CI environment.

## Requirements
- Blender 4.x with bundled `bpy`.
- A valid HAA-D-3 SceneSpec JSON file.

## Run
```bash
blender --background --python adapters/blender/render_scene.py -- \
  --scene examples/scenes/synthetic-emergence.scene.json \
  --output artifacts/blender
```

Outputs:
- `scene.blend` — editable Blender project.
- `frame_0001.png` onward — rendered image sequence.
- `render-manifest.json` — renderer/version/settings and evidence scope.

The adapter maps oscillator position keyframes to animated spheres and scalar coherence to an animated ring scale. It does not infer anatomy. The rendered result is marked `RENDERED_NOT_REVIEWED`; a human must complete scientific, creative, accessibility and rights review before release.
