#!/usr/bin/env python3
"""Fail CI when any tracked Markdown document is absent from DOCUMENT-CATALOG.md."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "docs/13-planning/DOCUMENT-CATALOG.md"
text = CATALOG.read_text(encoding="utf-8")
listed = set(re.findall(r"^\|\s+`([^\`]+\.md)`\s+\|", text, flags=re.MULTILINE))
tracked = subprocess.run(
    ["git", "ls-files", "--", "*.md"],
    cwd=ROOT, check=True, capture_output=True, text=True,
).stdout.splitlines()
expected = set(tracked)
missing = sorted(expected - listed)
stale = sorted(listed - expected)
if missing or stale:
    print("DOCUMENT CATALOG DRIFT")
    if missing:
        print("Missing from catalog:")
        print("\n".join(f"  - {p}" for p in missing))
    if stale:
        print("Catalog paths not tracked:")
        print("\n".join(f"  - {p}" for p in stale))
    sys.exit(1)
print(f"PASS: catalog enumerates all {len(expected)} tracked Markdown files.")
