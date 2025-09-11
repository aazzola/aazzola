#!/usr/bin/env python3
import sys,os,re
BANNED = [
    "andreaazzola_website200x200.png","andreaazzola_website200x200-1.png",
    "facebook.svg","facebook-1.svg","instagram.svg","instagram-1.svg",
    "linkedin.svg","linkedin-1.svg","pinterest.svg","pinterest-1.svg",
    "twitter.svg","twitter-1.svg","favicon.png","favicon-1.png"
]
pat = re.compile(r'<p align="center"><img src="/images/([^"]+)"[^>]*></p>\s*\n?', re.IGNORECASE)
def clean_text(s):
    def repl(m):
        base = m.group(1).lower()
        return "" if any(base.endswith(b.lower()) for b in BANNED) else m.group(0)
    return pat.sub(repl, s)
def main():
    if len(sys.argv)<2:
        print("usage: cleanup_banned_images.py CONTENT_DIR"); sys.exit(1)
    root = os.path.abspath(sys.argv[1]); changed=0; scanned=0
    for r,_,files in os.walk(root):
        for fn in files:
            if not fn.lower().endswith(".md"): continue
            p=os.path.join(r,fn); scanned+=1
            with open(p,"r",encoding="utf-8",errors="ignore") as f: s=f.read()
            ns=clean_text(s)
            if ns!=s:
                with open(p,"w",encoding="utf-8") as f: f.write(ns)
                changed+=1
    print(f"scanned_md={scanned}")
    print(f"cleaned_md={changed}")
if __name__=="__main__":
    main()
