# Research-to-Scene Mapping Contract

**Status:** Draft 0.1

## Purpose
Make the conversion from research/model outputs to visuals explicit, inspectable and reproducible.

## Mapping record
A mapping records source model/finding, source field, evidence class, transform formula, units, coordinate system, parameters, target scene property, author/version and validation method or artistic rationale.

## Kuramoto reference mapping
- Phase θᵢ → 2D point position: xᵢ = R cos(θᵢ), yᵢ = R sin(θᵢ).
- Order parameter r(t) → normalized global coherence indicator.
- Source class: MODEL_OUTPUT.
- Scene interpretation: ANALYTICAL.
- The mapping is not a biological reconstruction and does not imply neural anatomy.

## Requirements
1. No silent transforms: formula and parameters must be stored.
2. Preserve source run identity, model version, seed and configuration.
3. Keep units and coordinate system explicit.
4. Keep data bindings separate from renderer-specific shader/material implementations.
5. Validate input shape and sample alignment before creating scenes.
6. Mark missing data and extrapolation explicitly; do not interpolate silently.
7. A SceneSpec mapping is not scientific validation.
