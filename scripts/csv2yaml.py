#!/usr/bin/env python3
import csv, sys, yaml

inp = sys.argv[1] if len(sys.argv) > 1 else "redirects.csv"
out = sys.argv[2] if len(sys.argv) > 2 else "data/redirects.yaml"

redirects = {}
with open(inp, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        old = row["old_path"].strip()
        new = row["new_url"].strip()
        if old and new:
            redirects[old] = new

with open(out, "w", encoding="utf-8") as f:
    yaml.dump(redirects, f, sort_keys=False, allow_unicode=True)

print(f"Written {out} with {len(redirects)} entries")