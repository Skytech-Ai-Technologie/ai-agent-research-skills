---
name: literature-review
description: Synthesize 10+ papers into a comparative review table + gaps.
version: 1.0.0
---

# literature-review

## Input
List of paper summaries (from paper-summarizer).

## Output
1. Comparison table: paper | method | dataset | metric | result | limitation.
2. **Trends** (3 bullets).
3. **Gaps** (3 bullets - what nobody did yet).
4. **Suggested direction** (2 sentences).

## Rules
- Group by method family, not chronologically.
- Call out contradictory results explicitly.
