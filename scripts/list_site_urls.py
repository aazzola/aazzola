#!/usr/bin/env python3
import os, sys
root = sys.argv[1] if len(sys.argv)>1 else "content"
rows = []
for r, _, files in os.walk(root):
    for fn in files:
        if not fn.lower().endswith(".md"): continue
        p = os.path.join(r, fn)
        rel = os.path.relpath(p, root)
        parts = rel.split(os.sep)
        if fn == "index.md":
            url = "/" + "/".join(parts[:-1]) + "/"
        elif fn == "_index.md":
            url = "/" + "/".join(parts[:-1]) + "/"
        else:
            stem = os.path.splitext(fn)[0]
            url = "/" + "/".join(parts[:-1] + [stem]) + "/"
        url = url.replace("//", "/")
        slug = [s for s in url.split("/") if s][-1] if any(s for s in url.split("/") if s) else ""
        rows.append((url, p, slug))
rows.sort()
for url, p, slug in rows:
    print(f"{url}\t{p}\t{slug}")
