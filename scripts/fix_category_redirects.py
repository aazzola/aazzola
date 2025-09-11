#!/usr/bin/env python3
import csv, sys, re
inp = "redirects.csv"
out = "redirects.csv"
rows = []
changed = 0
with open(inp, newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames or ["old_path","new_url"]
    for row in r:
        old = (row.get("old_path") or "").strip()
        new = (row.get("new_url") or "").strip()
        if not old:
            rows.append({"old_path": old, "new_url": new})
            continue
        if not old.startswith("/"):
            old = "/" + old
        if old in ("/category", "/category/"):
            new2 = "https://andreaazzola.com/categories/"
            if new2 != new:
                new = new2; changed += 1
        else:
            m = re.fullmatch(r"/category/([^/]+)/?", old, flags=re.I)
            if m:
                tag = m.group(1)
                new2 = f"https://andreaazzola.com/categories/{tag}/"
                if new2 != new:
                    new = new2; changed += 1
        rows.append({"old_path": old, "new_url": new})
with open(out, "w", newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=["old_path","new_url"])
    w.writeheader()
    w.writerows(rows)
print(changed)
