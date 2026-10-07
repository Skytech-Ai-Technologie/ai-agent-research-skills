---
name: arxiv-search
description: Search arXiv and rank papers by relevance for a research query.
version: 1.0.0
tools: [http, arxiv-api]
---

# arxiv-search

## Goal
Find the most relevant papers for a user query.

## Workflow
1. Parse query -> keywords + date range + max_results (default 10).
2. Call arXiv API: `http://export.arxiv.org/api/query?search_query=all:{keywords}&max_results={n}&sortBy=submittedDate`.
3. For each entry extract: id, title, authors, published, summary, pdf_url.
4. Rank by keyword overlap + recency.
5. Output markdown table: rank | title | year | authors | why-relevant | pdf link.

## Rules
- Never invent arXiv IDs. Only return real API results.
- Prefer last 3 years unless user asks for seminal.
- Always include pdf_url.

## Example call
`python skills/arxiv-search/tool.py --query "edge VLM quantization" --max 10`
