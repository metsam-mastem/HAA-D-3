# SceneSpec Contract

**Status:** Draft 0.1. JSON Schema is the machine-readable contract in schemas/scene-spec.schema.json.

## Purpose
A renderer-independent description of a scene. It carries meaning, timing, visual structure and evidence references without embedding renderer-specific commands.

## Required fields
schema_version, scene_id, title, duration_seconds, frame_rate, interpretation_mode, evidence_refs and objects.

## Interpretation modes
LITERAL, ANALYTICAL, EXPLANATORY, METAPHORICAL. This is distinct from evidence class. For example, a METAPHORICAL scene can be inspired by OBSERVED research but must not depict the metaphor as measurement.

## Object model
Each object has id, type, transform and optional material, geometry, animation, data_binding, annotations and asset references. Renderer adapters may extend objects in namespaced extension blocks; core fields remain portable.

## Timing
Use seconds for time and explicit frame rate for frame-accurate delivery. Do not assume all renderers share frame numbering or coordinate conventions.

## Coordinate systems
Declare coordinate_system and units when spatial geometry is present. Adapter conversions must be explicit and tested.

## Versioning
Breaking changes require a new schema major version and migration guide. Unknown optional extension namespaces may be ignored; unknown core fields should be rejected by strict validators or reported clearly.

## Validation
Schema validation, semantic validation, provenance validation and renderer capability validation are separate checks. A schema-valid scene is not automatically scientifically valid or renderable.
