#!/usr/bin/env python3
"""Enforce HAA-D-3 single-source repository topology."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
tracked = subprocess.run(
    ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
).stdout.decode("utf-8").split("\0")
paths = [Path(value).as_posix() for value in tracked if value]
errors = []

package_roots = set()
test_roots = set()
for value in paths:
    parts = Path(value).parts
    for index in range(len(parts) - 1):
        if parts[index:index + 2] == ("src", "haa_d3"):
            package_roots.add("/".join(parts[:index + 2]))
        if parts[index] == "tests" and value.endswith(".py"):
            test_roots.add("/".join(parts[:index + 1]))

if package_roots != {"src/haa_d3"}:
    errors.append(f"expected only src/haa_d3 as Python package root; found {sorted(package_roots)}")
if test_roots != {"tests"}:
    errors.append(f"expected only tests as Python test root; found {sorted(test_roots)}")

workflow_paths = sorted(
    path for path in paths
    if path.startswith(".github/workflows/") and Path(path).suffix in {".yml", ".yaml"}
)
if workflow_paths != [".github/workflows/quality.yml"]:
    errors.append(f"expected one quality workflow; found {workflow_paths}")

if "docs/README.md" not in paths:
    errors.append("missing canonical documentation index: docs/README.md")
if "docs/SOURCE-MAP.md" not in paths:
    errors.append("missing canonical source map: docs/SOURCE-MAP.md")
if "AGENTS.md" not in paths:
    errors.append("missing root agent rules: AGENTS.md")

if errors:
    print("REPOSITORY STRUCTURE CHECK FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("PASS: one Python package root, one test root, one quality workflow and canonical project maps.")
