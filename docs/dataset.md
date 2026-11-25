# Dataset design

The experimental freeze is `candidate600_v4`. The main configuration binds manifest SHA-256 `892dcd8449a1d8686a2561c3c111e69b03cf688c7377919e1409ab5f6663514f`. The cross-model freeze is `stage240_20261118_v1`, with ordered manifest SHA-256 `b5f8f23b6c50366d736dc2359d3eab187b01fe4839c30811801223e94a461f14`. The 240 frozen scenario and truth objects matched the corresponding main-set records.

**Histories.** Short histories present a compact context. Multi-stage histories divide the work into successive phases. Long histories carry decisions across a longer supplied history. The oracle-derived cases use selected source evidence, which limits conclusions about unfiltered retrieval.

**Operations.** DELETE removes the target from permitted use within scope. INVALIDATE marks the target as invalid for current decisions. SUPERSEDE introduces a replacement and specifies how the previous version may be used on a historical route. ISOLATE restricts use by principal, branch, or purpose. Apply the rule for the event's checkpoint. Submission, acknowledgement, and effect are separate events.

**Queries.** Normal tasks advance the working trajectory. Probes test behavior at a checkpoint without writing the probe answer back. Count each query event once per scenario, before repetition across models or methods.

| Collection | Short / multi-stage / long | DELETE / INVALIDATE / SUPERSEDE / ISOLATE | Normal tasks | Probes |
|---|---|---|---:|---:|
| Main 600 | 200 / 200 / 200 | 150 / 150 / 150 / 150 | 1,900 | 4,550 |
| Cross-model 240 | 80 / 80 / 80 | 60 / 60 / 60 / 60 | 760 | 1,820 |
| Directly included 587 | 197 / 194 / 196 | 148 / 145 / 146 / 148 | 1,860 | 4,451 |

Each history-by-operation cell contains 50 main scenarios and 20 subset scenarios. The subset overlaps the main collection. Within the subset, 234 included bodies contain 741 tasks and 1,774 probes.
