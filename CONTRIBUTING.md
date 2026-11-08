# Contributing to HAA-D-3

## Start here
Read AGENTS.md, README.md, docs/README.md, docs/SOURCE-MAP.md, docs/GOVERNANCE.md and docs/END-TO-END-LIFECYCLE.md.

## One project, one source of truth
Do not create parallel package roots, prototypes, test directories, documentation indexes or workflows. Extend src/haa_d3/ for core behavior; place tests in tests/; examples in examples/; optional integrations in adapters/; scenes in scenes/; generated output in artifacts/ or releases/.

## Branches and commits
Use focused branches: feat/<topic>, fix/<topic>, research/<topic>, creative/<topic>, docs/<topic>, foundation/<topic>. Never push directly to main. Use conventional commit prefixes: feat:, fix:, test:, docs:, research:, creative:, chore:.

## Work-package brief
Every non-trivial PR states problem/value, owner, scope, non-goals, affected contracts, dependencies, acceptance criteria, verification commands, risks, rights/provenance and rollback/migration notes.

## Tests and quality
Use RED → GREEN → REFACTOR for behavior changes. Run:
~~~bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m haa_d3.cli validate-scene examples/scenes/synthetic-emergence.scene.json
PYTHONPATH=src python -m haa_d3.cli render-knowledge-graph examples/knowledge/seed-graph.json --out /tmp/haa-d3-graph
~~~
The GitHub Quality Gate runs these checks on PRs. If an environment is unavailable, mark it NOT RUN and explain.

## Assets and licensing
The project license is undecided. Public visibility does not grant reuse rights. Track license and attribution for external code, datasets, models, images, fonts, audio and video. Do not commit credentials, private datasets or large generated renders.

## Review discipline
Keep PRs focused. Update README, source map, docs index and document catalog when structure changes. Do not merge a PR unless the project owner explicitly authorizes it.
