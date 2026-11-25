# Files and joins

Read JSON Lines as UTF-8, one object per line. The included source evidence is a single JSON array. Paths below start at the repository root.

| Path | What to read |
|---|---|
| `data/main600/catalog.jsonl` | Stable scenario ID, history type, primary operation, source dataset and group, original record and session IDs, body availability. |
| `data/main600/scenarios.jsonl` | One included scenario per row. Read `events` in sequence order. Each event has a kind and an event ID. Query events carry a query ID, checkpoint, mode, prompt and access context. |
| `data/main600/evaluator_truth.jsonl` | Evaluator-only facts, operation targets, version and copy relations, checkpoint states, and query rules. Keep this file outside model inputs. |
| `data/main600/source_evidence/selected_original_records.json` | Source histories keyed by `question_id`. The catalog's `original_record_id` links to this field. Within a history, the session and session-ID arrays correspond by position. |
| `data/subsets/stage240.jsonl` | One scenario ID per row, in frozen cross-model order. |
| `data/reconstruction/` | Data-only recovery instructions and a standard-library Python reader. A recipe holds literals plus character spans into the compact UTF-8 JSON representation of a particular oracle record. Hashes bind the restored rows. |
| `data/manifests/` | Coverage and repository-relative SHA-256 checksums. Checksums cover every tracked release file except the checksum list itself. |

Read from the repository root:

```python
import json
from pathlib import Path

def read_rows(path):
    with Path(path).open(encoding="utf-8") as stream:
        yield from map(json.loads, stream)

by_id = {s["scenario_id"]: s for s in read_rows("data/main600/scenarios.jsonl")}
subset = [s["scenario_id"] for s in read_rows("data/subsets/stage240.jsonl")]
available = [by_id[i] for i in subset if i in by_id]
assert len(available) == 234
```

Join the truth row by scenario ID and a query's rule by `query_rules[query_id]`. Some evaluator fields retain historical review or source locators from the freeze. Use the catalog and bundled evidence for portable source lookups.

## Recover the other 13 rows

1. Download the [pinned LongMemEval oracle JSON](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned/resolve/98d7416c24c778c2fee6e6f3006e7a073259d48f/longmemeval_oracle.json).
2. From the repository root run `python data/reconstruction/restore.py longmemeval_oracle.json restored`. Choose a new output directory. The tool checks the input file hash and each recovered record hash.
3. Read the additional `scenarios.jsonl` and `evaluator_truth.jsonl` from that directory alongside the included rows. The recovered `selected_original_records.jsonl` has one source object per line. Join all rows by ID and use catalog or subset order when selecting cases.

Recovery preserves the experimental JSON values, including the original prompts and truth. Whitespace in a serialized JSON object may differ. No models or evaluation software are needed.
