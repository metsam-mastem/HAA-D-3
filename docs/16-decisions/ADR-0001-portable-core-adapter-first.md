# ADR-0001: Portable Core and Adapter-First Architecture

- Status: Proposed
- Date: 2026-11-08
- Scope: platform, model provider, renderer and simulator integrations

## Context
HAA-D-3 must be usable across multiple operating systems and execution surfaces. It must not be coupled to a single LLM, cloud provider, renderer, simulator or GUI framework. The project is early, so premature microservices and framework commitments would add cost and reduce portability.

## Decision
Adopt a portable core with explicit contracts and adapters. Keep domain logic in a modular monolith. Expose the same core through CLI first, then optional API, web, desktop and mobile shells. Treat model providers, renderers, simulators, storage and search as replaceable adapters.

## Options considered
1. One framework/provider owns the entire stack — rejected due to lock-in.
2. Microservices from day one — rejected as premature operational complexity.
3. Portable modular core plus capability adapters — proposed.

## Consequences
Positive: provider neutrality, offline/local path, testability, reusable contracts and gradual platform expansion. Negative: adapter interfaces and compatibility tests require discipline; some integrations will have feature gaps.

## Validation plan
Demonstrate the same SceneSpec validation from CLI and library; add at least two independent renderer adapters before claiming renderer neutrality; test supported OS workflows before claiming cross-platform compatibility.

## Revisit when
Measured scaling, team boundaries, deployment isolation or security requirements justify service extraction.
