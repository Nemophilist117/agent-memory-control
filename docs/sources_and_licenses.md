# Sources and licenses

| Source | Cases | Adaptation and attribution |
|---|---:|---|
| CoMem | 248 | Project-authored fictional work histories. Scenarios share protocol and mechanism families. Distinct source IDs do not establish independent real users. |
| LongMemEval cleaned oracle | 348 | Selected history sessions form the source material for CoMem events, control instructions, tasks and truth. The pinned cleaned dataset declares MIT. Retain the upstream copyright and permission notice. |
| LongMemEval-V2 | 4 | Text episodes derived from benchmark task trajectories, with CoMem events and evaluator annotations. The pinned dataset declares Apache-2.0. This release distributes modified text records. Screenshots and archives are excluded. |

**LongMemEval.** Cite Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang and Dong Yu, *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. The authors describe simulated, human-edited evidence sessions. The cleaned oracle file used here has SHA-256 `821a2034d219ab45846873dd14c14f12cfe7776e73527a483f9dac095d38620c`. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html) · [Pinned data card](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned/blob/98d7416c24c778c2fee6e6f3006e7a073259d48f/README.md) · [MIT notice](licenses/LongMemEval-MIT.txt)

**LongMemEval-V2.** Cite Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng and Kai-Wei Chang, *LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues*. The authors describe customized benchmark environments and synthetic or benchmark-generated task content. CoMem uses the four source trajectories identified in the catalog. [Pinned dataset and documentation](https://huggingface.co/datasets/xiaowu0162/longmemeval-v2/tree/f152293e235517d504809563c833d7190b8c713b) · [Apache License 2.0](licenses/LongMemEval-V2-Apache-2.0.txt)

**Contact-like strings.** Context and provenance matter. The upstream simulation process, example-domain addresses and organizational role addresses support retaining those classes of text. Thirteen oracle-derived cases contain other contact-like strings whose individual status could not be established, including telephone-like sequences. Their complete rows are available through [local reconstruction](data_format.md#recover-the-other-13-rows). No replacement scenario or redacted evaluation target is used.

The catalog preserves the source group, original record identifier and selected session identifiers for each adaptation. Upstream notices apply to their respective materials. This release adds no blanket license for project-authored or third-party content.
