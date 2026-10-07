---
name: pdf-reader
description: Extract clean text and tables from research PDFs offline.
version: 1.0.0
tools: [pypdf, pdfplumber]
---

# pdf-reader

## Workflow
1. Try `pdfplumber` for text + tables (best for two-column papers).
2. Fallback to `pypdf` for scanned/simple PDFs.
3. Return: title (first line), sections (Abstract/Method/Results), tables as markdown.
4. If PDF is scanned images, report "needs OCR" and suggest `easyocr`.

## Usage
`python skills/pdf-reader/tool.py --pdf papers/example.pdf --out out.txt`
