"""Load and list skills."""
from pathlib import Path

def load_skill(path):
    p = Path(path) / "SKILL.md"
    text = p.read_text(encoding="utf-8")
    # split frontmatter
    prompt = text
    meta = {}
    if text.startswith("---"):
        _, fm, rest = text.split("---", 2)
        prompt = rest.strip()
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return {"path": str(p), "meta": meta, "prompt": prompt}

def list_skills(root="skills"):
    return sorted([d.name for d in Path(root).iterdir() if (d / "SKILL.md").exists()]) if Path(root).exists() else []
