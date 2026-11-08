# Contributing to HAA-D-3

## Start here
Read [AGENTS.md](AGENTS.md), [the documentation index](docs/README.md), and [the continuity protocol](docs/13-planning/PROJECT-CONTINUITY-AND-INGESTION-PROTOCOL.md).

## Contribution types
- Research: source-backed question, claim ledger, methods, limitations and reproducibility.
- Engineering: issue, interface/contract, tests, implementation and compatibility notes.
- Creative: brief, storyboard/shot specification, asset rights, scene files and QC evidence.
- Documentation: owner, status, scope, references and update date.

## Branches and commits
Use focused branches: `docs/<topic>`, `feat/<topic>`, `fix/<topic>`, `research/<topic>`, `creative/<topic>`. Never push experimental work directly to main. Use conventional commit prefixes such as docs:, feat:, fix:, test:, research:, creative:, chore:.

## Pull requests
A PR must state problem, proposed change, scope, non-goals, affected contracts, evidence, test commands/results, risks, licensing and migration/rollback notes. Keep PRs small enough to review. Large research/creative contributions may be split into linked PRs.

## Tests
Run `python -m unittest discover -s tests -v` for the initial Python core. Add tests for every new behavior and schema change. If a toolchain is unavailable, mark the check NOT RUN and explain why.

## Assets and licensing
Do not assume repository content is open-source licensed. Until a root license is explicitly chosen, treat copyright and reuse rights as unresolved. Add attribution and license records for external code, datasets, models, images, fonts, audio and video. Do not add large binary renders to Git by default.

## No destructive cleanup
Never remove apparently unused files without checking history, references, ownership and user intent. Propose migrations before restructuring existing content.
