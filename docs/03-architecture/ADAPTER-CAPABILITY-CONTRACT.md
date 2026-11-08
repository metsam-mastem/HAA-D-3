# Adapter Capability Contract

**Status:** Draft 0.1

## Purpose
Prevent provider, model, renderer, simulator and platform lock-in. Integrations advertise capabilities and constraints; orchestration selects by required capability and runtime policy, not by hard-coded vendor.

## Descriptor
Each adapter declares:
- Stable adapter ID and version.
- Capability identifiers provided.
- Supported platforms.
- Offline capability.
- GPU/hardware requirements.
- License identifier and maturity.
- Input/output contract versions.
- Configuration schema, health check and known limitations (required before production maturity).

## Selection
The initial core selector filters by capability, platform, offline requirement and GPU availability, then returns a deterministic ID-sorted list. Selection is not an endorsement. The caller must inspect license, maturity, security and compatibility before activation.

## Isolation
Provider SDK imports belong inside adapter packages. Core contracts use plain Python data structures and stable JSON. Adapter failure must not corrupt canonical project data. All external/model-generated content is untrusted until validated.

## Maturity levels
experimental, preview, stable, deprecated. Promotion requires tests, docs, license review, security review and compatibility evidence.

## Future extension
Add resource budgets, supported contract versions, streaming/batch semantics, determinism guarantees, cancellation, health state and sandbox policy without making any single provider mandatory.
