#!/usr/bin/env python3
import sys, os, re, csv, shutil
def safe_name(basename):
    m = re.match(r'^resource\?id=([A-Za-z0-9\-]+)(.*)$', basename)
    if m:
        guid = m.group(1)
        rest = m.group(2)
        ext = os.path.splitext(rest)[1].lower() if rest else ""
        if ext not in [".jpg",".jpeg",".png",".gif",".webp",".svg",".bmp",".ico"]:
            ext = ext if ext in [".jpg",".jpeg",".png",".gif",".webp",".svg",".bmp",".ico"] else os.path.splitext(basename)[1].lower()
            if ext == "": ext = ".jpg"
        return f"resource-{guid}{ext}"
    b = basename.replace("?", "_").replace("=", "-")
    return b
def main():
    if len(sys.argv) < 3:
        print("usage: normalize_static_images.py STATIC_IMAGES_DIR MAPPING_CSV")
        sys.exit(1)
    img_dir = os.path.abspath(sys.argv[1])
    map_csv = os.path.abspath(sys.argv[2])
    os.makedirs(img_dir, exist_ok=True)
    rows = []
    if os.path.exists(map_csv):
        with open(map_csv, newline="") as f:
            r = csv.reader(f)
            header = next(r, None)
            for row in r:
                if len(row) >= 2:
                    rows.append([row[0], row[1]])
    renames = {}
    for fn in os.listdir(img_dir):
        src_path = os.path.join(img_dir, fn)
        if not os.path.isfile(src_path): continue
        new_name = safe_name(fn)
        if new_name != fn:
            dst_path = os.path.join(img_dir, new_name)
            i = 1
            base, ext = os.path.splitext(new_name)
            while os.path.exists(dst_path):
                dst_path = os.path.join(img_dir, f"{base}-{i}{ext}")
                i += 1
            os.replace(src_path, dst_path)
            renames[fn] = os.path.basename(dst_path)
    if rows:
        for r in rows:
            old = r[1]
            base = os.path.basename(old)
            if base in renames:
                r[1] = renames[base]
    with open(map_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_rel_path_in_mirror","dest_basename_in_static_images"])
        for r in rows:
            w.writerow(r)
    print(f"renamed_files={len(renames)}")
