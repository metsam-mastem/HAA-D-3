# Legacy Documentation Inventory and Recovery Plan

**Created:** 2026-11-08  
**Purpose:** Preserve the original README's documentation map and prevent planned/referenced material from being silently lost during repository reorganization.

## Audit finding
The original README on `main` referenced the documents below. The inspected `main` Git tree contained only `README.md`; the referenced document files were not present in that tree at the time of inspection. Therefore, their contents cannot be presumed or reconstructed as if they were recovered originals.

This inventory preserves their names, intended purpose and recovery status. It does not mark them as deleted by this work. Recreate them only from recoverable source material or as clearly labeled new drafts.

## Legacy references

| Original path | Intended content | Status |
|---|---|---|
| docs/00-charter/PROJECT-CHARTER.md | Mission, vision, scope, governance, deliverables | NOT FOUND in inspected main tree |
| docs/00-charter/MANIFESTO.md | Principles and program philosophy | NOT FOUND |
| docs/01-creative/THREE-CHAPTERS-SERIES-BIBLE.md | Narrative structure, soundtrack references, episodic potential | NOT FOUND; narrative references preserved in README |
| docs/02-knowledge/KNOWLEDGE-UNIVERSE.md | Multidisciplinary taxonomy and research paths | NOT FOUND |
| docs/02-knowledge/RESEARCH-PLAN.md | Discovery protocol, source and claim handling | NOT FOUND; new research operations draft exists |
| docs/03-architecture/CONCEPT-ARCHITECTURE.md | Planes, components, data/control flows | NOT FOUND; new reference architecture draft exists |
| docs/04-engineering-spec/ES-DRAFT-0.1.md | Preliminary requirements, interfaces, verification | NOT FOUND |
| docs/05-vertical-slice/VERTICAL-SLICE-FEASIBILITY.md | Thin end-to-end prototype scope and evaluation | NOT FOUND; new VS-01 specification exists |
| docs/06-planning/WBS-ROADMAP.md | Work breakdown, phases, gates, dependencies | NOT FOUND; new roadmap draft exists |
| docs/07-reuse/REPOSITORY-REUSE-AUDIT.md | VINT, SSG, research patterns and reuse boundaries | NOT FOUND; do not invent the audit findings |
| docs/08-evaluation/COMPETITOR-LANDSCAPE.md | Comparison categories and differentiated value | NOT FOUND |
| docs/08-evaluation/RESOURCE-BENCHMARK-PLAN.md | Metrics, resource accounting and evaluation protocol | NOT FOUND |
| docs/09-creative-tech/VISUAL-ANIMATION-PIPELINE.md | Code/prompt workflows, storyboard and render pipeline | NOT FOUND; new scientific-to-cinema pipeline exists |
| docs/10-references/SOURCES.md | Initial source registry | NOT FOUND; new Nature/GitHub landscape exists |
| docs/11-governance/RISK-REGISTER.md | Risks and mitigations | NOT FOUND |
| docs/11-governance/STATUS-CHANGELOG.md | Truthful project status and changes | NOT FOUND; Git history and handoff records are now authoritative |

## Recovery rules
1. Search all branches, tags, commits, backups and user-provided archives before declaring a legacy document unrecoverable.
2. If the original is recovered, preserve it and record its source commit or archive.
3. If a new document replaces the old concept, record a migration map and label it as a new draft; do not claim it is the original.
4. Never fabricate the contents of the VINT/SSG reuse audit, competitor analysis, benchmark plan or source registry.
5. Update this inventory and docs/README.md when a document is recovered or recreated.
