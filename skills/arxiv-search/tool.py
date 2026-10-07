"""arXiv search helper (real API, no key needed)."""
import argparse, urllib.request, xml.etree.ElementTree as ET

def search(query, max_results=10):
    q = query.replace(" ", "+")
    url = f"http://export.arxiv.org/api/query?search_query=all:{q}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    with urllib.request.urlopen(url, timeout=30) as r:
        data = r.read()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(data)
    out = []
    for e in root.findall("a:entry", ns):
        pid = e.find("a:id", ns).text
        out.append({
            "id": pid.split("/abs/")[-1],
            "title": " ".join(e.find("a:title", ns).text.split()),
            "authors": [a.find("a:name", ns).text for a in e.findall("a:author", ns)],
            "published": e.find("a:published", ns).text[:10],
            "summary": " ".join(e.find("a:summary", ns).text.split())[:600],
            "pdf": pid.replace("/abs/", "/pdf/") + ".pdf",
        })
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", required=True)
    ap.add_argument("--max", type=int, default=10)
    a = ap.parse_args()
    for i, p in enumerate(search(a.query, a.max), 1):
        print(f"{i}. [{p['id']}] {p['title']} ({p['published']})")
        print(f"   {', '.join(p['authors'][:4])}")
        print(f"   {p['pdf']}\n")
