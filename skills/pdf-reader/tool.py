"""PDF text extractor (pdfplumber -> pypdf fallback)."""
import argparse
from pathlib import Path

def extract(pdf_path):
    text = ""
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += (page.extract_text() or "") + "\n"
        if text.strip():
            return text
    except ImportError:
        pass
    from pypdf import PdfReader
    reader = PdfReader(str(pdf_path))
    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"
    return text

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    t = extract(Path(a.pdf))
    print(t[:4000])
    if a.out:
        Path(a.out).write_text(t, encoding="utf-8")
