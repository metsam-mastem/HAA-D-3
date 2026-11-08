# Data, Provenance and Asset Management

## Data classes
Public, licensed, user-provided, sensitive/private, derived, synthetic and generated. Apply the strictest applicable handling requirement.

## Required metadata
Stable ID, title, creator/source, acquisition date, source URL or locator, version, checksum, media type, schema, license/rights, attribution, transformation history, privacy restrictions, retention and intended use.

## Storage policy
- Small text and code: Git.
- Schemas/configs/metadata: Git.
- Large datasets, raw footage, renders and model weights: external artifact/object storage or documented local workspace.
- Never commit secrets, personal records, private source dumps or unlicensed copyrighted media.
- Keep a manifest and checksum for artifacts stored outside Git.

## Reproducibility bundle
Include manifest, source references, code revision, environment/dependency lock, commands, random seeds, parameters, logs, metrics, outputs and checksums.

## Retention and cleanup
No automatic deletion of source research or user-created assets. Cleanup requires ownership check, retention policy, backup and an auditable decision. Temporary caches may be regenerated and excluded from Git.

## Licensing
A repository being public does not make its content open-source. Record license per external dependency and asset. Project-level license remains undecided until explicitly selected by the repository owner.
