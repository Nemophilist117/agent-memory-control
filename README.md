# Agent Memory Control Benchmark

How does an agent handle later tasks when an earlier memory is deleted, invalidated, superseded, or restricted? This benchmark records a sequence of inputs, control events, and queries for each scenario. It distinguishes completing a task from respecting the memory state applicable at that point.

This release contains the benchmark dataset and documentation. Experiment and evaluation code will be released separately.

## Coverage

| Collection | Scenarios indexed | Scenario bodies included | Normal tasks in collection | Probes in collection |
|---|---:|---:|---:|---:|
| Main experiment (candidate600_v4) | 600 | 248 | 1,900 | 4,550 |
| Cross-model subset (stage240_20261118_v1) | 240 | 53 | 760 | 1,820 |

The 248 included scenarios contain 820 normal tasks and 1,959 probes. Their 53-scene overlap with the subset contains 181 normal tasks and 437 probes. The remaining 352 adaptations are indexed for provenance. Their histories and evaluator material are withheld pending confirmation of embedded-content redistribution scope.

The history types are short histories, multi-stage histories with successive phases, and long histories. Each type contributes 200 main scenarios and 80 subset scenarios. Each type-by-primary-operation cell has 50 main scenarios and 20 subset scenarios.

| Primary operation | Intended behavior after the operation takes effect |
|---|---|
| DELETE | Stop using the targeted information within the specified scope. |
| INVALIDATE | Treat the targeted claim as invalid for current decisions. |
| SUPERSEDE | Use the replacement version for current tasks. Historical use follows the scenario rule. |
| ISOLATE | Enforce the specified access boundary for the principal, branch, and purpose. |

Normal tasks advance the working trajectory. Probes test behavior at a checkpoint without writing their answers back into that trajectory. Counts are query events per scenario before repetition across methods or models. Submission, acknowledgement, and effect are distinct events.

## Files and use

All JSON and JSON Lines files use UTF-8. JSON Lines has one object per line.

| Path | Contents |
|---|---|
| `catalog/main600.jsonl` | One row per stable `scenario_id`. Includes history type, primary operation, source dataset, group, original record and session IDs, and `content_included`. |
| `subsets/stage240.jsonl` | The 240 scenario IDs in frozen manifest order. Join on `scenario_id` to select the subset. |
| `data/scenarios.jsonl` | Original scenario rows for the included cases. Read `events` in sequence order. Each event has a kind and ID. Query events carry the prompt, mode, checkpoint, and access context. |
| `data/evaluator_truth.jsonl` | Evaluator-only rows keyed by scenario ID. Facts, version and copy relations, operation targets, checkpoint states, and query-specific rules specify the expected behavior. Keep these rows outside agent inputs. |
| `data/source_evidence/selected_original_records.json` | JSON array of the included fictional source histories. Join the catalog's `original_record_id` to `question_id`. The session IDs and session arrays identify the source material. |

To select cases, look up the subset IDs in the catalog, filter on `content_included`, then retrieve the matching scenario and truth rows by ID. Within each row, join query events to `query_rules` by `query_id`. Stable IDs are preserved. The subset has no duplicate copy of the scenario text.

## Sources, attribution, and access

CoMem contributes 248 project-authored fictional work histories. Scenarios can share protocol and mechanism families. Distinct source IDs do not establish independent real users. No new data license is granted by this release.

For the other 352 entries, the catalog identifies the upstream records. Original sources can be obtained as follows. The upstream downloads supply source histories; they do not supply CoMem's withheld adapted scenarios or truth rows.

- **348 LongMemEval cleaned oracle adaptations.** Obtain the pinned oracle JSON and match the catalog's original record ID to its question ID. These are evidence-selected histories, so their results concern the supplied history. The pinned dataset card declares MIT. Cite Di Wu et al., *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. [Oracle file](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned/resolve/98d7416c24c778c2fee6e6f3006e7a073259d48f/longmemeval_oracle.json) · [Dataset card](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned/blob/98d7416c24c778c2fee6e6f3006e7a073259d48f/README.md)
- **4 LongMemEval-V2 adaptations.** Use the catalog's original record IDs to locate the upstream trajectories. The pinned dataset card declares Apache-2.0. Embedded third-party material has separate scope considerations. Cite Di Wu et al., *LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues*. [Pinned dataset and access instructions](https://huggingface.co/datasets/xiaowu0162/longmemeval-v2/tree/f152293e235517d504809563c833d7190b8c713b)

## Version checks

The main experiment configuration binds the freeze manifest (SHA-256 `892dcd8449a1d8686a2561c3c111e69b03cf688c7377919e1409ab5f6663514f`) and evaluator truth. The cross-model handoff binds the ordered subset manifest (SHA-256 `b5f8f23b6c50366d736dc2359d3eab187b01fe4839c30811801223e94a461f14`). All 240 frozen scenario and truth objects matched their main-set counterparts before release filtering. These digests identify the original input manifests.
