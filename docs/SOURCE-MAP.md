# HAA-D-3 Source Map and Repository Topology

**Canonical source map · Version 0.2.0**

## One authoritative home per responsibility

| Responsibility | Canonical location | Rule |
|---|---|---|
| Project entry and identity | README.md | Only root project overview |
| Agent/contributor rules | AGENTS.md | Mandatory; no local competing copies |
| Contribution workflow | CONTRIBUTING.md | Branch, review and test rules |
| Charter and manifesto | docs/00-charter/ | Mission, boundaries, principles |
| Product/architecture/domain | docs/02-product/, docs/03-architecture/, docs/04-domain/ | Product scope and stable design |
| Research/knowledge | docs/02-knowledge/, docs/06-research/, research/ | Source-backed inquiry and findings |
| Data/provenance/contracts | docs/07-data/, schemas/ | Lineage and machine-readable contracts |
| Python runtime | src/haa_d3/ | Single canonical package |
| Tests | tests/ | Single canonical Python test root |
| Example inputs | examples/ | Small, versioned, non-sensitive fixtures |
| External integrations | adapters/ | Optional provider/renderer/compute bridges |
| Scene packages | scenes/ | Renderer-neutral scene specifications |
| Creative plans | creative/, docs/09-creative-tech/, docs/12-production/ | Story, shots, direction, production |
| Browser demonstration | demo/neural-odyssey/ | Self-contained illustrative web demo |
| Generated outputs | artifacts/, releases/ | Outputs are not source of truth |
| Automation | .github/workflows/quality.yml | Single quality workflow |
| Architecture decisions | docs/16-decisions/ | ADRs are durable decision records |

## Runtime source tree

~~~text
src/haa_d3/
├── __init__.py
├── capabilities.py      # capability descriptors and adapter selection
├── cli.py               # stable command-line entry point
├── contracts.py         # Finding and SceneSpec semantic checks
├── kuramoto.py          # numerical coupled-oscillator prototype
├── knowledge_graph.py   # graph validation, SVG projection, hash receipt
└── scene_mappings.py    # model-output to SceneSpec transforms
~~~

Dependency direction:
- Core domain modules do not depend on adapters or UI.
- CLI orchestrates core modules; domain modules never import CLI.
- Adapters depend on public core contracts, never the reverse.
- Demos consume exported data/contracts; they do not duplicate scientific logic.

## Repository topology

~~~text
.
├── .github/workflows/   # quality gates
├── adapters/            # optional integrations
├── artifacts/           # generated output policy/manifests
├── creative/             # authored creative plans
├── demo/neural-odyssey/ # browser illustrative experience
├── docs/                 # governed project knowledge
├── examples/             # canonical sample inputs
├── releases/             # release manifests
├── research/             # research workspaces
├── scenes/               # renderer-neutral scene packages
├── schemas/              # versioned JSON contracts
├── scripts/              # repository integrity checks
├── src/haa_d3/           # single Python runtime source
└── tests/                # single Python test root
~~~

## Consolidation decision
The former prototype/ package duplicated the haa_d3 import namespace, used a second PYTHONPATH, had separate tests and a separate CI workflow. Its graph functionality is consolidated into src/haa_d3/knowledge_graph.py; the fixture moves to examples/knowledge/; tests move to tests/. The duplicate package and workflow are removed. This preserves the graph behavior while eliminating a second runtime truth.

## Documentation taxonomy
Existing document paths are preserved in this foundation change to avoid breaking historical references. Numbered folders are stable subject identifiers, not execution sequence or priority. docs/README.md is the single navigation index; docs/13-planning/DOCUMENT-CATALOG.md is the machine-checked inventory. Any future path migration requires a complete link rewrite and migration map in one reviewed change.

## Why there is no root index.html
The root is a multi-domain source repository, not a deployed static web application. A root index.html would create a false second application entry point. The browser demo owns demo/neural-odyssey/index.html. A unified web workbench must first declare a frontend package, build tool, routing contract and deployment workflow.

## Change control
Before adding a top-level folder or second implementation of an existing capability, update this map and submit an ADR. Extend the canonical package or add a documented adapter. Do not create parallel prototype/v2/final-final package roots.
