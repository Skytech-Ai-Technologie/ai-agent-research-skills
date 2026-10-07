---
name: paper-summarizer
description: Summarize a research paper into TL;DR, method, results, limitations.
version: 1.0.0
---

# paper-summarizer

## Input
Paper text (from pdf-reader) or abstract + full text.

## Output format (always use this)
1. **TL;DR (2 sentences)**
2. **Problem**
3. **Method** (bullets, include architecture/dataset)
4. **Results** (numbers, benchmarks)
5. **Limitations**
6. **Cite-worthy sentence** (one line to quote in a review)

## Rules
- Be faithful, no hallucinating numbers.
- If method unclear, say "not specified".
- Keep under 250 words unless user asks for deep dive.
