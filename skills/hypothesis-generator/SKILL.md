---
name: hypothesis-generator
description: Generate testable hypotheses and experiment designs.
version: 1.0.0
---

# hypothesis-generator

## Workflow
1. Input: observation + context papers.
2. Generate 3 hypotheses (H1-H3), each with:
   - Statement (if X then Y because Z)
   - Falsifiable prediction (metric + threshold)
   - Experiment (dataset, baseline, ablation)
   - Cost (compute/time estimate)
3. Rank by novelty x feasibility.

## Rules
- Each hypothesis must be falsifiable.
- No vague claims like "improves performance".
