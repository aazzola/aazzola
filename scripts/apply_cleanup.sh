#!/bin/bash
set -e
ts=$(date +"%Y%m%d-%H%M%S")
bk="backups/cleanup-$ts"
mkdir -p "$bk"

backup_and_rm() {
  while IFS= read -r -d '' p; do
    dest="$bk/$p"
    mkdir -p "$(dirname "$dest")"
    mv "$p" "$dest"
  done
}

# category/**
find content/category -mindepth 1 -print0 2>/dev/null | backup_and_rm || true

# root *.md (exclude README,_index*)
find content -maxdepth 1 -type f -name "*.md" ! -name "README.md" ! -name "_index*" -print0 | backup_and_rm

# __index.disabled.md
find content -type f -name "__index.disabled.md" -print0 | backup_and_rm

# index.md.tmp
find content -type f -name "index.md.tmp" -print0 | backup_and_rm

# feed/
find content/feed -print0 2>/dev/null | backup_and_rm || true

# login/
find content/login -print0 2>/dev/null | backup_and_rm || true

# root *-2.md
find content -maxdepth 1 -type f -name "*-2.md" -print0 | backup_and_rm

# stray posts folder under post/
find content/post/posts -print0 2>/dev/null | backup_and_rm || true

echo "Backed up removed items to $bk"
