from pathlib import Path
import re

root = Path(".")
targets = [
    ("content/post", "post"),
    ("content/it", "it"),
]

def split_fm(text):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)\Z', text, re.S)
    return (m.group(1), m.group(2)) if m else (None, text)

def upsert_kv(fm, key, value):
    lines = fm.splitlines()
    k = key.lower()
    done = False
    out = []
    for ln in lines:
        s = ln.strip()
        if s.lower().startswith(k + ":"):
            out.append(f'{key}: {value}')
            done = True
        else:
            out.append(ln)
    if not done:
        out.insert(1, f'{key}: {value}')
    return "\n".join(out)

changed = 0
for base, typ in targets:
    b = root / base
    if not b.exists(): 
        continue
    for md in b.rglob("index.md"):
        txt = md.read_text(encoding="utf-8", errors="ignore")
        fm, body = split_fm(txt)
        if fm is None:
            continue
        fm2 = upsert_kv(fm, "type", typ)
        fm2 = upsert_kv(fm2, "draft", "false")
        new = f"---\n{fm2}\n---\n{body}"
        if new != txt:
            md.write_text(new, encoding="utf-8")
            changed += 1

print(f"Updated: {changed}")
