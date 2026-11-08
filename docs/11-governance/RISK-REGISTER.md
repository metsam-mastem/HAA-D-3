# Risk Register
| ID | Risk | Likelihood | Impact | Mitigation / trigger |
|---|---|---|---|---|
| R01 | Scope creep | High | High | WBS/gates; feature lacks outcome |
| R02 | Novelty unsupported | Med | High | literature review; superiority claim |
| R03 | Feedback instability | Med | High | bounded loops, stability metrics; divergence |
| R04 | Resource overrun | Med | High | profiling, budget, limits; RAM/latency cap |
| R05 | Integration mismatch | High | High | typed adapters; contract failure |
| R06 | Model license unclear | Med | High | model-card audit; redistribution/fine-tune |
| R07 | Third-party rights conflict | Med | High | license/provenance review; code/media reuse |
| R08 | Evidence conflated with inference | Med | High | evidence ledger; unsupported statement |
| R09 | Visualization misleading | Med | Med | scientific review and metaphor labels |
| R10 | Benchmark leakage | Med | High | grouped splits, duplicates; leakage found |
| R11 | CI green but visual output poor | Med | Med | separate artifact review |
| R12 | Music sync rights missing | Med | High | cue sheet/clearance; use in edit |
| R13 | Repo media dump | Med | High | ignore raw media/model caches |
| R14 | Solo schedule optimistic | High | Med | ranges, reprioritize |
| R15 | Unsafe parser/import | Low-Med | High | sandbox, no script execution |

Review at each gate and when task, model, dataset, license, architecture or budget changes.