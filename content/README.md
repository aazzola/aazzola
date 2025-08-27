---
title: "Readme"
date: 2025-08-19T16:25:18
draft: false
---
This folder contains:
- `filters/clean.lua` — Pandoc Lua filter to strip attributes, flatten Div/Span, and parse simple Raw HTML.
- `scripts/clean_post.py` — regex-based second pass to tidy leftovers.

## Recommended conversion pipeline

1) Convert HTML → Markdown with Pandoc **using the Lua filter**:
```bash
pandoc -f html-native_divs-native_spans -t gfm --wrap=preserve --strip-comments \
  --lua-filter=filters/clean.lua \
  -o out.md in.html
```

2) Optional: run the Python post-processor to remove trivial leftovers:
```bash
python scripts/clean_post.py out.md out.cleaned.md
```

3) Add Hugo front matter at the top of each file and drop into `content/`.