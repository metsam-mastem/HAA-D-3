# Platform Portability and Provider Independence

## Portability objective
A single project definition and set of contracts should be usable from local desktop, mobile, browser, headless server, CI and render workers without rewriting scientific or domain logic.

## Layers
1. Portable core: Python library, domain entities, validation and deterministic transforms.
2. CLI: headless workflows and automation.
3. Service API: optional HTTP interface over the same core.
4. Web UI: browser client consuming stable contracts.
5. Desktop shell: optional native wrapper; no domain logic in the shell.
6. Mobile shell: optional constrained capture/review/control client.
7. Worker adapters: Blender, Manim, FFmpeg, scientific simulators and GPU jobs.
8. Provider adapters: LLM, storage, search and compute providers behind capability interfaces.

## Capability negotiation
An adapter declares id, version, capabilities, inputs/outputs, platform constraints, optional dependencies, license, offline support, resource requirements and health check. The orchestrator selects by capability and policy, not hard-coded vendor name.

## Model/provider neutrality
Core logic must not import provider SDKs. Use a normalized request/response contract with provider-specific adapters. Support no-model workflows, local models, remote models and multiple providers. Record provider/model/version/settings for generated content. Model output is untrusted input and must be validated.

## Renderer neutrality
SceneSpec is canonical. Blender, Manim, browser graphics and other renderers are adapters. Do not let renderer-specific data leak into core scientific entities.

## Platform matrix
| Surface | Role | First priority |
|---|---|---|
| CLI/headless | automation, reproducibility, batch processing | P0 |
| Desktop Windows/Linux/macOS | full authoring and local compute | P1 |
| Web | review, collaboration, interactive explainers | P1 |
| Android | capture, inspect, review, lightweight scene control | P2 |
| iOS | review and lightweight capture/control | P3 |
| Server/CI/render farm | repeatable jobs and scale-out rendering | P1 |

The priority is a planning order, not a promise that every target is implemented.

## Offline-first
Core validation, metadata, local project access and deterministic small demos must work without network. Remote services are optional. Cache remote metadata with provenance and freshness indicators.

## Portability tests
Run contract tests on supported Python versions and OS runners. Avoid assumptions about filesystem case, path separators, locale, GPU, shell or codec availability. Capability tests should skip with explicit NOT RUN/BLOCKED reasons where hardware or licensed software is unavailable.
