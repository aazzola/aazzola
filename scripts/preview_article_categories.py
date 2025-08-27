from pathlib import Path
import re, sys

root = Path(".")
content = root / "content"

def split_fm(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)\Z", text, re.S)
    if not m: return None, text
    return m.group(1), m.group(2)

def parse_categories_from_body(body):
    for line in body.splitlines():
        if re.match(r"^\s*Categories?\s*:\s*", line, re.I):
            rhs = re.sub(r"^\s*Categories?\s*:\s*", "", line, flags=re.I).strip()
            rhs = re.sub(r"[•|·]", ",", rhs)
            parts = [p.strip() for p in re.split(r",|;|\|", rhs) if p.strip()]
            cats = []
            for p in parts:
                p = re.sub(r"\s+", " ", p).strip(" .-")
                if p and p.lower() != "categories":
                    cats.append(p)
            return list(dict.fromkeys(cats))
    return []

def current_categories(fm):
    m = re.search(r"(?mi)^\s*categories\s*:\s*(.+)$", fm)
    if not m: return None
    line = m.group(1).strip()
    arr = re.findall(r'"([^"]+)"', line)
    if arr: return arr
    arr = [x.strip() for x in re.split(r"\[|\]|,|\s+", line) if x.strip() and x.strip('",') not in ("[","]")]
    return arr or None

total = 0
changed = 0
for md in content.rglob("index.md"):
    txt = md.read_text(encoding="utf-8", errors="ignore")
    fm, body = split_fm(txt)
    if fm is None: continue
    total += 1
    cur = current_categories(fm) or []
    found = parse_categories_from_body(body)
    if not found: continue
    if cur != found:
        changed += 1
        print(f"{md} -> {found}")
print(f"Total files: {total}")
print(f"Would change: {changed}")
