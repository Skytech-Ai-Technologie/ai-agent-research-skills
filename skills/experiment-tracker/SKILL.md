---
name: experiment-tracker
description: Log runs, metrics and artifacts reproducibly.
version: 1.0.0
---

# experiment-tracker

## Log format (JSONL `runs.jsonl`)
```json
{"run_id": "2026-10-07_qwen_edge", "hypothesis": "H1", "config": {"lr": 1e-4},
 "metrics": {"acc": 0.81}, "artifacts": ["ckpt.pt"], "notes": ""}
```

## Rules
1. Every run gets a unique run_id.
2. Never overwrite past runs, append only.
3. Commit `runs.jsonl` after each experiment.
