# Adapters

Integrations for model providers, renderers, simulators, storage, search and compute belong here. Each adapter declares capability ID, version, platforms, requirements, offline behavior, license, input/output contracts, configuration and health check. Core domain modules must not import provider-specific SDKs.

## Available renderer
- [Blender adapter](blender/README.md): optional background renderer for SceneSpec to editable `.blend` plus PNG frame sequence. Blender 4.2+ required; runtime execution is NOT RUN in default CI.

## Portable render path
The core renderer in `src/haa_d3/render_svg.py` uses only Python standard library and is exercised by the required CI suite. It is the default low-dependency preview/export path.
