#!/usr/bin/env python3
import sys, os, re, csv, argparse, glob

def load_map(csv_path):
    by_rel, by_base, by_guid = {}, {}, {}
    if os.path.exists(csv_path):
        with open(csv_path, newline="") as f:
            r = csv.reader(f); next(r, None)
            for row in r:
                if len(row) < 2: continue
                src_rel = row[0].strip().lstrip("/").replace("\\","/")
                dest_base = row[1].strip()
                by_rel[src_rel] = dest_base
                base = os.path.splitext(os.path.basename(src_rel))[0].lower()
                by_base[base] = dest_base
                m = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", src_rel, re.I)
                if m:
                    by_guid[m.group(0).lower()] = dest_base
    return by_rel, by_base, by_guid

def find_mirror_html(mirror_root, slug):
    a = glob.glob(os.path.join(mirror_root, "**", slug, "index.html"), recursive=True)
    if a: return a[0]
    b = glob.glob(os.path.join(mirror_root, "**", f"{slug}.html"), recursive=True)
    return b[0] if b else None

def extract_img_srcs(html_path):
    try:
        with open(html_path, "r", encoding="utf-8", errors="ignore") as f: s = f.read()
    except:
        return []
    return [m.group(1) for m in re.finditer(r"<img[^>]+src=[\"']([^\"'>]+)[\"']", s, re.IGNORECASE)]

def norm_src(src):
    s = src.strip()
    s = re.sub(r"^https?://(www\.)?andreaazzola\.com/?", "/", s, flags=re.IGNORECASE)
    s = s.replace("\\","/")
    if s.startswith("./"): s = s[2:]
    while s.startswith("//"): s = s[1:]
    m = re.match(r'^/?resource\?id=([A-Za-z0-9\-]+)', s)
    if m:
        return f"resource/{m.group(1)}"
    return s

def key_candidates(src_rel):
    k = src_rel.lstrip("/").replace("\\","/")
    out = {k}
    base = os.path.splitext(os.path.basename(k))[0].lower()
    out.add(base)
    m = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", k, re.I)
    if m:
        out.add(m.group(0).lower())
    if "?" in k:
        out.add(k.split("?",1)[0])
    return list(out)

def map_to_dest(src_rel, idx_rel, idx_base, idx_guid):
    for cand in key_candidates(src_rel):
        if cand in idx_rel:
            return "/images/" + idx_rel[cand]
        if cand in idx_base:
            return "/images/" + idx_base[cand]
        if cand in idx_guid:
            return "/images/" + idx_guid[cand]
    return None

def has_images_in_md(txt):
    return bool(re.search(r"!\[.*?\]\(.*?\)", txt) or re.search(r"<img\s", txt, re.IGNORECASE))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mirror_root")
    ap.add_argument("content_root")
    ap.add_argument("mapping_csv")
    ap.add_argument("--max-per-post", type=int, default=3)
    ap.add_argument("--only", type=str, default="")
    ap.add_argument("--include-already", action="store_true")
    ap.add_argument("--csv", action="store_true")
    ap.add_argument("--out", type=str, default="")
    args = ap.parse_args()

    only = set([x.strip() for x in args.only.split(",") if x.strip()]) if args.only else set()
    idx_rel, idx_base, idx_guid = load_map(args.mapping_csv)
    rows = []
    for root, _, files in os.walk(args.content_root):
        for fn in files:
            if fn.lower() != "index.md": continue
            p = os.path.join(root, fn)
            slug = os.path.basename(os.path.dirname(p))
            if only and slug not in only: continue
            try:
                with open(p, "r", encoding="utf-8", errors="ignore") as f: md = f.read()
            except:
                continue
            if has_images_in_md(md) and not args.include_already:
                rows.append((slug, p, 0, ""))
                continue
            html = find_mirror_html(args.mirror_root, slug)
            if not html:
                rows.append((slug, p, 0, ""))
                continue
            srcs = extract_img_srcs(html)
            urls = []
            for s in srcs:
                n = norm_src(s)
                if not n: continue
                d = map_to_dest(n, idx_rel, idx_base, idx_guid)
                if d and d not in urls: urls.append(d)
                if len(urls) >= args.max_per_post: break
            rows.append((slug, p, len(urls), ", ".join(urls)))

    if args.out:
        with open(args.out, "w", newline="") as f:
            if args.csv:
                w = csv.writer(f)
                w.writerow(["slug","md_path","found","proposed"])
                for r in rows: w.writerow([r[0], r[1], r[2], r[3]])
            else:
                f.write("slug\tmd_path\tfound\tproposed\n")
                for r in rows: f.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\n")
    else:
        if args.csv:
            print("slug,md_path,found,proposed")
            for r in rows:
                print(",".join([str(r[0]), str(r[1]), str(r[2]), '"' + r[3].replace('"','""') + '"']))
        else:
            print("slug\tmd_path\tfound\tproposed")
            for r in rows:
                print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}")

if __name__ == "__main__":
    main()