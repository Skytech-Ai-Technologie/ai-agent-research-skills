"""Minimal ReAct research loop (bring your own LLM)."""
from .skill_loader import load_skill

def build_system_prompt(skills=("arxiv-search", "paper-summarizer", "citation-manager")):
    parts = ["You are a research agent. Use these skills:"]
    for s in skills:
        try:
            sk = load_skill(f"skills/{s}")
            parts.append(f"\n## Skill: {s}\n{sk['prompt'][:1500]}")
        except FileNotFoundError:
            continue
    parts.append("\nAlways cite sources. Never invent paper IDs.")
    return "\n".join(parts)
