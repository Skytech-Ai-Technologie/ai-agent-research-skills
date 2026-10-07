# AI Agent Research Skills

> Plug-and-play skills for research AI agents — search, read, summarize, cite, and track experiments.
> Offline-friendly, tool-agnostic (OpenCode / Claude / LangChain / AutoGen compatible).

## 🧩 Skills included

| Skill | What it does |
|---|---|
| [arxiv-search](skills/arxiv-search/SKILL.md) | Search arXiv, rank papers by relevance |
| [paper-summarizer](skills/paper-summarizer/SKILL.md) | TL;DR + method + results + limitations |
| [pdf-reader](skills/pdf-reader/SKILL.md) | Extract text/tables from PDFs offline |
| [web-research](skills/web-research/SKILL.md) | Multi-hop web research with evidence |
| [citation-manager](skills/citation-manager/SKILL.md) | BibTeX + APA/MLA formatting |
| [literature-review](skills/literature-review/SKILL.md) | Synthesize 10+ papers into a review table |
| [hypothesis-generator](skills/hypothesis-generator/SKILL.md) | Generate testable hypotheses + experiments |
| [experiment-tracker](skills/experiment-tracker/SKILL.md) | Log runs, metrics, artifacts |

## 🚀 Quick Start

```bash
git clone https://github.com/midoo2020/ai-agent-research-skills.git
cd ai-agent-research-skills
pip install -r requirements.txt
python main.py --list
python main.py --skill arxiv-search --query "edge VLM quantization"
```

## Using a skill

Each skill is one folder with a `SKILL.md` (instruction prompt) + optional `tool.py`:

```python
from src.skill_loader import load_skill, run_skill

skill = load_skill("skills/arxiv-search")
print(skill["prompt"])
```

Works with any agent loop — copy `skills/<name>/SKILL.md` into your system prompt.

## Structure

```text
skills/<name>/SKILL.md   # skill prompt + workflow
skills/<name>/tool.py    # optional runnable helper
src/skill_loader.py      # load/list skills
src/agent.py             # minimal ReAct research loop
main.py                  # CLI
```

## License

MIT — see [LICENSE](LICENSE).
