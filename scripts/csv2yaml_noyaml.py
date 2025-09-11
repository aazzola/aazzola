#!/usr/bin/env python3
import csv, sys, os

inp = sys.argv[1] if len(sys.argv)>1 else "redirects.csv"
out = sys.argv[2] if len(sys.argv)>2 else "data/redirects.yaml"

def q(s): return '"' + s.replace('"','\\"') + '"'

rows = []
with open(inp, newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for row in r:
        old = (row.get("old_path") or "").strip()
        new = (row.get("new_url") or "").strip()
        if not old or not new: continue
        if not old.startswith("/"): old = "/" + old
        if "?" not in old and "." not in old and not old.endswith("/"): old += "/"
        rows.append((old, new))

os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    for k,v in rows:
        f.write(f"{q(k)}: {q(v)}\n")
print(f"written {out} {len(rows)}")
