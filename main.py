"""CLI: list skills, run helpers."""
import argparse
from src.skill_loader import list_skills, load_skill

def main():
    ap = argparse.ArgumentParser(description="AI Agent Research Skills")
    ap.add_argument("--list", action="store_true", help="list skills")
    ap.add_argument("--skill", default="", help="show SKILL.md for a skill")
    ap.add_argument("--query", default="", help="demo query (arxiv-search)")
    a = ap.parse_args()
    if a.list or (not a.skill and not a.query):
        for s in list_skills():
            print(f"- {s}")
        return
    if a.skill:
        sk = load_skill(f"skills/{a.skill}")
        print(f"# {a.skill}\n{sk['prompt']}")
    if a.query:
        import sys
        sys.path.insert(0, "skills/arxiv-search")
        from tool import search
        for i, p in enumerate(search(a.query), 1):
            print(f"{i}. [{p['id']}] {p['title']} ({p['published']}) {p['pdf']}")

if __name__ == "__main__":
    main()
