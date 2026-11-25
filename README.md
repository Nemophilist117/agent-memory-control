# Agent Memory Control Benchmark

This benchmark tests how an agent uses memory after deletion, invalidation, supersession, or an access restriction, and whether it can still complete subsequent tasks.

| Collection | Indexed | Included in full | Recoverable from the pinned source | Normal tasks | Probes |
|---|---:|---:|---:|---:|---:|
| Main benchmark | 600 | 587 | 13 | 1,900 | 4,550 |
| Cross-model subset | 240 | 234 | 6 | 760 | 1,820 |

Query totals cover each complete collection. The 587 included main scenarios contain 1,860 normal tasks and 4,451 probes. All 13 remaining scenario, truth, and evidence records were restored locally and compared with the frozen originals.

Start with the [main catalog](data/main600/catalog.jsonl). Read each included [scenario](data/main600/scenarios.jsonl) in event order. Use the [ordered subset IDs](data/subsets/stage240.jsonl) to select the cross-model sample. The [format guide](docs/data_format.md) includes a reading example and the exact recovery procedure.

- [Dataset design and counts](docs/dataset.md)
- [Sources, licenses, and attribution](docs/sources_and_licenses.md)
- [Coverage by source, history, and operation](data/manifests/coverage.json)
- [File checksums](data/manifests/SHA256SUMS)

This release contains the benchmark dataset and documentation. Experiment and evaluation code will be released separately.
