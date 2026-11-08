# Claim, Evidence and Provenance Policy

## Evidence classes
| Class | Meaning | Presentation |
|---|---|---|
| OBSERVED | Directly recorded/extracted data | Show source, units and context |
| REPRODUCED | Independently regenerated result | Show method, version and reproduction evidence |
| MODEL_OUTPUT | Output of a specified model | Name model, parameters and limitations |
| HYPOTHESIS | Testable proposition not established | Label as hypothesis |
| INTERPRETATION | Reasoned explanation | Identify author and supporting evidence |
| METAPHOR | Artistic analogy | Label as illustrative/metaphorical |
| UNKNOWN | Not established | Do not imply certainty |

## Provenance fields
source_id, source_type, title, author_or_organization, publication_date, access_date, DOI_or_URL, license, locator, claim_ids, confidence_note.

For datasets also record version, accession, license, population/species where relevant, preprocessing, units, missingness and restrictions.

## Rules
1. A citation does not automatically validate a claim; verify that the source supports the exact statement.
2. Distinguish peer-reviewed evidence, preprints, documentation, software examples and opinion.
3. Record contradictory evidence and uncertainty.
4. A rendered result is not scientific validation.
5. A visually plausible animation is not proof of a mechanism.
6. Link claim → model/experiment → scene → shot → final artifact.
7. Preserve original data and document transformations.
8. Review license and attribution before reuse.
9. Do not redistribute copyrighted music, footage, figures or assets without permission.
10. Review claims and rights before publication.

## Statuses
PASS / FAIL / NOT RUN / BLOCKED. Each status requires reviewer, date, scope and evidence pointer.
