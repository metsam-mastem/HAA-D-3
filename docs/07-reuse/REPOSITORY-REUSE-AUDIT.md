# Repository & Reuse Audit — Initial Pass (2026-11-08)
## Destination
https://github.com/metsam-mastem/HAA-D-3 was public, writable via connected GitHub, and empty at inspection; README initialized. No prior files were present to preserve.

## VINT — Reel Intelligence
https://github.com/metsam-mastem/VINT
Inspected projects/reel-intelligence/WORK_REPORT_0001.md. Its report describes platform-independent multimodal workbench, local-first modular monolith, intake, modality processors, timestamped evidence timeline, claim ledger, review, analysis receipts, and cost-aware frame selection. Report is an architecture/research artifact; implementation status for listed features is not presumed.
Potential ADAPT: provenance/receipt, evidence timeline, pipeline profiles, human-review/uncertainty. Direct code integration not established.

## Repo 4 — SSG (Symbolic Systems Grammar)
https://github.com/metsam-mastem/4
README describes graph-first canonical knowledge, stable IDs, provenance, relations, versions, visual projections, Vec2/Vec3, graph validation/metrics, hash-chain provenance, Merkle proof, SVG renderer and read-only source/Git metadata scans.
Potential ADAPT: canonical graph, source/projection separation, provenance, SVG ideas.
Caution: README says license TBD; verify license and APIs before copying. Visualization is not automatically reversible backup/encryption.

## Repo 1 — SOVEREIGN Workbench
https://github.com/metsam-mastem/1
README describes UGI local-first Git infrastructure and SOVEREIGN OS Android dev workspace, separate runtimes/provider-neutral Git contract.
Potential REFERENCE: Git workflows, provider contract, CI, local-first.
Caution: README notes SOVEREIGN OS license not declared in mirrored revision; do not assume reuse rights. UGI described as MIT, but inspect package and dependencies.

## SssssssskiLLL
https://github.com/metsam-mastem/SssssssskiLLL
Inspected docs index: taxonomy, source/file maps, evidence register, repository inventory, architecture/feasibility comparison, license/provenance and test register.
Potential REFERENCE: documentation methodology and claim statuses.

## Account scan limits
Account repo listing showed many repositories. This was a targeted audit of VINT, 4, 1 and SssssssskiLLL based on relevance, not exhaustive source-level audit of all owned repositories. VINT identified, no need to guess.

## External research/code leads
seRNN https://github.com/8erberg/spatially-embedded-RNN ; Norse https://github.com/norse/norse ; snnTorch https://github.com/jeshraghian/snntorch ; PyTorch Geometric https://github.com/pyg-team/pytorch_geometric ; Transformers https://github.com/huggingface/transformers ; llama.cpp https://github.com/ggml-org/llama.cpp ; vLLM https://github.com/vllm-project/vllm .
All are REFERENCE candidates pending fit, maintenance, licenses and model terms.

## Labels
ADOPT=dependency after audit; ADAPT=compatible pattern; REFERENCE=learn only; DEFER=not yet; REJECT=unsuitable.