# Domain Model

**Status:** Draft 0.1 — conceptual, not a complete database schema.

## Core entities
- Project: identity, purpose, owners, status and policy.
- Source: publication, dataset, repository, documentation, media or interview with locator, version, date and rights.
- Claim: a bounded statement with evidence class, source links, confidence note and limitations.
- Dataset: source, schema, version, license, units, preprocessing and restrictions.
- Model: formal description, assumptions, implementation, inputs, outputs and validation status.
- Experiment: question, hypothesis, model, dataset, configuration, seed, environment, metrics and artifacts.
- Finding: result or interpretation with evidence class, method and uncertainty.
- Scene: versioned visual composition with evidence references and creative intent.
- Shot: timed segment with camera, objects, motion, sound, transitions and acceptance criteria.
- Asset: source, creator, license, checksum, usage rights and transformations.
- Render: scene hash, renderer/adapter version, settings, output and QC record.
- Decision: context, options, decision, consequences, status and review trigger.

## Relations
Source supports Claim; Dataset is used by Experiment; Model is executed by Experiment; Experiment produces Finding and Artifact; Finding is mapped to Scene; Scene contains Shot; Shot references Asset and Finding; Render is generated from Scene; Decision governs a Project, Contract or Adapter.

## Rules
1. IDs are stable and never reused.
2. Every derived artifact records its inputs and transformation.
3. Units and coordinate systems are explicit where applicable.
4. Timestamps use ISO 8601 UTC in machine records; retain original timezone in source metadata.
5. A relation does not imply truth: source links must be reviewed.
6. Separate descriptive data from presentation labels.
7. Version schemas and migrations independently from app releases.
