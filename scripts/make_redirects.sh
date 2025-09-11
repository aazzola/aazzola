#!/usr/bin/env bash
set -euo pipefail
csv="${1:-redirects.csv}"
out="static"
tail -n +2 "$csv" | while IFS=, read -r old new; do
  [ -z "${old:-}" ] && continue
  p="${old#/}"
  if [[ "$p" == *.html ]]; then
    outpath="$out/$p"
  else
    outpath="$out/$p/index.html"
  fi
  mkdir -p "$(dirname "$outpath")"
  cat > "$outpath" <<EOF
<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=$new"><link rel="canonical" href="$new"><title>Redirecting...</title><a href="$new">Redirect</a>
EOF
done
echo "done"
