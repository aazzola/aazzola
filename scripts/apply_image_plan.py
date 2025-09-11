#!/usr/bin/env python3
import sys, os, re, csv, argparse, glob

BANNED_BASENAMES = {
    "andreaazzola_website200x200.png",
    "andreaazzola_website200x200-1.png",
    "facebook.svg","facebook-1.svg",
    "instagram.svg","instagram-1.svg",
    "linkedin.svg","linkedin-1.svg",
    "pinterest.svg","pinterest-1.svg",
    "twitter.svg","twitter-1.svg",
    "favicon.png","favicon-1.png"
}
GUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I)

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
                m = GUID_RE.search(src_rel)
                if m: by_guid[m.group(0).lower()] = dest_base
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
    m = re.match(r"^/?resource\?id=([A-Za-z0-9\-]+)", s)
    if m: return f"resource/{m.group(1)}"
    return s

def key_candidates(src_rel):
    k = src_rel.lstrip("/").replace("\\","/")
    out = {k}
    base = os.path.splitext(os.path.basename(k))[0].lower()
    out.add(base)
    m = GUID_RE.search(k)
    if m: out.add(m.group(0).lower())
    if "?" in k: out.add(k.split("?",1)[0])
    return list(out)

def guess_dest(src_rel, idx_rel, idx_base, idx_guid):
    for cand in key_candidates(src_rel):
        if cand in idx_rel: return "/images/" + idx_rel[cand]
        if cand in idx_base: return "/images/" + idx_base[cand]
        if cand in idx_guid: return "/images/" + idx_guid[cand]
    return None

def allow_url(url, slug):
    if not url.startswith("/images/"): return False
    base = os.path.basename(url).lower()
    if base in BANNED_BASENAMES: return False
    if "social/" in url.lower(): return False
    if slug.lower() in base: return True
    if "resource" in base: return True
    if GUID_RE.search(base): return True
    return False

def has_images_in_md(txt):
    return bool(re.search(r"!\[.*?\]\(.*?\)", txt) or re.search(r"<img\s", txt, re.IGNORECASE))

def split_front_matter(txt):
    m = re.match(r'^---\s*\n.*?\n---\s*\n', txt, flags=re.DOTALL)
    if m: return txt[:m.end()], txt[m.end():]
    return "", txt

def insert_images(md_txt, urls):
    fm, body = split_front_matter(md_txt)
    block = "\n".join([f'<p align="center"><img src="{u}" loading="lazy" alt=""></p>' for u in urls]) + "\n\n"
    if fm: return (fm + block + body).lstrip("\n")
    return (block + md_txt).lstrip("\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mirror_root")
    ap.add_argument("content_root")
    ap.add_argument("mapping_csv")
    ap.add_argument("--staging-dir", default="staging_content")
    ap.add_argument("--max-per-post", type=int, default=3)
    ap.add_argument("--only", type=str, default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--static-images", default="static/images")
    args = ap.parse_args()

    only = set([x.strip() for x in args.only.split(",") if x.strip()]) if args.only else set()
    idx_rel, idx_base, idx_guid = load_map(args.mapping_csv)
    made = 0; scanned = 0
    for root, _, files in os.walk(args.content_root):
        for fn in files:
            if fn.lower() != "index.md": continue
            p = os.path.join(root, fn)
            slug = os.path.basename(os.path.dirname(p))
            if only and slug not in only: continue
            scanned += 1
            with open(p, "r", encoding="utf-8", errors="ignore") as f: md = f.read()
            if has_images_in_md(md): continue
            html = find_mirror_html(args.mirror_root, slug)
            if not html: continue
            srcs = extract_img_srcs(html)
            urls = []
            for s in srcs:
                n = norm_src(s)
                if not n: continue
                d = guess_dest(n, idx_rel, idx_base, idx_guid)
                if d and allow_url(d, slug) and d not in urls:
                    urls.append(d)
                if len(urls) >= args.max_per_post: break
            if not urls: continue
            new_md = insert_images(md, urls)
            rel = os.path.relpath(p, args.content_root)
            out_path = os.path.join(args.staging_dir, rel)
            if not args.dry_run:
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "w", encoding="utf-8") as f: f.write(new_md)
            made += 1
    print(f"scanned_posts={scanned}")
    print(f"staged_files={made}")
    print(f"staging_dir={args.staging_dir}")

if __name__ == "__main__":
    main()
