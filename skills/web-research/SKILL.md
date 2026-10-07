---
name: web-research
description: Multi-hop web research with cited evidence.
version: 1.0.0
---

# web-research

## Workflow
1. Break question into 3-5 sub-queries.
2. Search each, collect top sources (URL + date + snippet).
3. Cross-check: at least 2 independent sources per claim.
4. Output: answer + **Evidence** section with [1][2] links.

## Rules
- No uncited factual claims.
- Prefer primary sources (papers, docs, official blogs).
- Mark uncertainty explicitly.
