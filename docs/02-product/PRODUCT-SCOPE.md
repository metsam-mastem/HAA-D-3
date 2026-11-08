# Product Scope and Product Boundaries

**Status:** Draft 0.1

## Product vision
A platform-independent environment for turning scientific and engineering questions into reproducible models, trustworthy knowledge objects, interactive explanations and cinematic media.

## Product surfaces
1. Research Workbench — sources, claims, datasets, experiments, methods and evidence.
2. Modeling Workbench — equations, numerical methods, simulation and model comparison.
3. Knowledge Workbench — entities, relationships, units, provenance and versioned graphs.
4. Scene Workbench — structured scenes, visual mappings, timelines, storyboard and annotations.
5. Production Workbench — rendering, compositing, editing, sound, subtitles, export and QC.
6. Delivery Workbench — packages, reports, interactive experiences, reusable assets and releases.

## User roles
Researcher, engineer, mathematician, educator, scientific communicator, visual artist, animator, sound designer, reviewer, producer and platform integrator. Roles are workflow perspectives, not mandatory account types.

## Product boundaries
- The platform orchestrates tools; it does not need to reimplement every specialist tool.
- It can call multiple model providers but does not require an LLM for core operations.
- It supports both local/offline and remote execution where capabilities exist.
- It does not certify scientific truth automatically; it records evidence and validation.
- It does not redistribute unlicensed third-party media or datasets.
- It does not promise cinematic quality from a single prompt.

## Non-goals for the first foundation release
Multi-tenant SaaS, mandatory cloud backend, proprietary model dependency, custom 3D renderer, full video editor, automatic scientific peer review and universal simulation engine.

## Product quality attributes
Portability, reproducibility, scientific traceability, modularity, accessibility, offline capability, inspectability, exportability, security, maintainability and low-resource operation.

## Success measures
Track reproducible experiment rate, source-to-claim traceability, scene contract validity, render reproducibility, cross-platform test coverage, asset rights completeness, time from research pack to reviewed scene and user-reported clarity. Do not invent targets before baselines exist.
