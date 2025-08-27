#!/bin/bash
set -e
root="/Users/andrea/Downloads/andrea-hugo-starter"
cd "$root"

echo "DUPLICATES (file.md vs folder/index.md)"
count=0
for section in content/post content/it; do
  [ -d "$section" ] || continue
  for f in "$section"/*.md; do
    [ -e "$f" ] || continue
    base="$(basename "$f")"
    [ "$base" = "_index.md" ] && continue
    slug="${base%.md}"
    if [ -d "$section/$slug" ] && [ -f "$section/$slug/index.md" ]; then
      echo "DUP: $f  <->  $section/$slug/index.md"
      count=$((count+1))
    fi
  done
done
echo "Total duplicates: $count"