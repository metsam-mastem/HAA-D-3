#!/usr/bin/env python3
"""Check local Markdown link destinations for tracked files/directories."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = sorted(ROOT.rglob("*.md"))
LINK = re.compile(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
errors = []
for source in MARKDOWN:
    body = source.read_text(encoding="utf-8")
    for match in LINK.finditer(body):
        destination = match.group(1) or match.group(2) or ""
        destination = destination.strip()
        parsed = urlparse(destination)
        if parsed.scheme or destination.startswith("//") or not parsed.path:
            continue
        path_text = unquote(parsed.path)
        target = (source.parent / path_text).resolve() if not path_text.startswith("/") else (ROOT / path_text.lstrip("/")).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {destination}")
            continue
        if not target.exists():
            errors.append(f"{source.relative_to(ROOT)}: missing target: {destination}")
if errors:
    print("MARKDOWN LINK CHECK FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"PASS: checked local Markdown destinations in {len(MARKDOWN)} Markdown files.")
