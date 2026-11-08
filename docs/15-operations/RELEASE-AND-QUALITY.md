# Release, Quality and Operations

## Quality gates
1. Static structure and documentation links.
2. Schema and contract validation.
3. Unit and integration tests.
4. Reproducibility and provenance checks.
5. Platform and adapter capability checks.
6. Scientific review for claims and model outputs.
7. Creative review for narrative, visual/audio quality and accessibility.
8. Rights/security review.
9. Packaging, checksums and release notes.

## Status vocabulary
PASS: executed and passed with evidence. FAIL: executed and failed. NOT RUN: not executed. BLOCKED: cannot execute because a dependency or permission is missing. Never convert NOT RUN to PASS.

## Versioning
Use semantic versioning for public APIs and schemas. Use date/version identifiers for research packs and datasets. Keep project release versions separate from scene versions and adapter versions.

## CI
CI should run on pull requests and main updates. Start with Python unit tests, JSON contract tests and documentation checks. Add cross-platform runners and render smoke tests only when dependencies are stable and available.

## Release manifest
Release ID, Git commit, schema versions, dependencies, adapters, evidence references, licenses, outputs, checksums, QC results and known limitations.

## Rollback
Preserve prior release artifacts and manifests. Roll back by selecting a previous immutable version; do not rewrite Git history as routine recovery.
