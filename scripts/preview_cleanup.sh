#!/bin/bash
set -e
echo "CANDIDATES:"
echo "--- category folder ---"
find content/category -mindepth 1 -print 2>/dev/null || true
echo "--- root *.md (eccetto README e _index*) ---"
find content -maxdepth 1 -type f -name "*.md" ! -name "README.md" ! -name "_index*" -print
echo "--- __index.disabled.md ---"
find content -type f -name "__index.disabled.md" -print
echo "--- index.md.tmp ---"
find content -type f -name "index.md.tmp" -print
echo "--- feed/ ---"
find content/feed -print 2>/dev/null || true
echo "--- login/ ---"
find content/login -print 2>/dev/null || true
echo "--- duplicate -2.md at root ---"
find content -maxdepth 1 -type f -name "*-2.md" -print
echo "--- stray posts folder under post/ ---"
find content/post/posts -print 2>/dev/null || true
echo "--- OPTIONAL: media import folder (resource under post/) ---"
find content/post/resource -print 2>/dev/null || true
echo "--- TOTALS ---"
c1=$(find content/category -mindepth 1 -print 2>/dev/null | wc -l | tr -d ' ')
c2=$(find content -maxdepth 1 -type f -name "*.md" ! -name "README.md" ! -name "_index*" -print | wc -l | tr -d ' ')
c3=$(find content -type f -name "__index.disabled.md" -print | wc -l | tr -d ' ')
c4=$(find content -type f -name "index.md.tmp" -print | wc -l | tr -d ' ')
c5=$(find content/feed -print 2>/dev/null | wc -l | tr -d ' ')
c6=$(find content/login -print 2>/dev/null | wc -l | tr -d ' ')
c7=$(find content -maxdepth 1 -type f -name "*-2.md" -print | wc -l | tr -d ' ')
c8=$(find content/post/posts -print 2>/dev/null | wc -l | tr -d ' ')
c9=$(find content/post/resource -print 2>/dev/null | wc -l | tr -d ' ')
echo "category/*: $c1"
echo "root *.md (except README,_index*): $c2"
echo "__index.disabled.md: $c3"
echo "index.md.tmp: $c4"
echo "feed/: $c5"
echo "login/: $c6"
echo "root *-2.md: $c7"
echo "post/posts: $c8"
echo "post/resource (optional): $c9"
