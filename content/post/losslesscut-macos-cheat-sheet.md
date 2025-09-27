---
title: "LosslessCut on macOS: Fast, Lossless Trimming (Cheat Sheet + Guide)"
date: 2025-09-27
lastmod: 2025-09-27
draft: false
slug: "losslesscut-macos-cheat-sheet"
tags: ["video editing", "losslesscut", "workflow", "shortcuts", "macOS"]
categories: ["Video Editing"]
author: "Andrea Azzola"
ShowToc: true
summary: "A practical guide to trimming H.264/HEVC footage instantly—without re‑encoding—using LosslessCut on macOS. Includes a printable cheat sheet and a Resolve-friendly workflow."
---


If you shoot long takes on action cams or phones, **LosslessCut** is the fastest way to carve out selects **without re‑encoding**. This article gives you a quick mental model, a copy‑paste workflow, and a keyboard‑first **cheat sheet** for macOS.

---

## Why LosslessCut?
- **Speed:** “Normal (keyframe) cut” copies the exact video/audio packets—no transcode—so exports are instant.
- **Quality:** zero generational loss (no added compression).
- **Focus:** perfect for building *selects* folders before editing in DaVinci Resolve, Premiere, or Final Cut.

> ⚡️ **Lossless rule of thumb:** Put **In/Out** on **keyframes** and export with **Normal (keyframe) cut**. If you need frame‑accurate edges, use **Smart cut** (only tiny re‑encode around the cuts).

---

## Quick Start (3 steps)
1. **Open a clip** → jump to a **keyframe** (`⌥→` / `⌥←`) → press **I**.  
2. Move to the end keyframe → press **O**.  
3. Press **+** (Add segment). Repeat for more segments → press **E** (Export) → choose **Normal / keyframe cut**.

Set the **output folder** (e.g., `01_SELECTS/OSMO` or `01_SELECTS/PHONE`) once and reuse it.

---

## Keyboard Cheat Sheet (macOS)

### Mark & Segments
| Shortcut | Action |
|---|---|
| **I** | Set **In** |
| **O** | Set **Out** |
| **+** | **Add segment** (keeps I→O) |
| **B** | **Split** segment at playhead |
| **↵ Enter** | **Label** segment |
| **⌫ Backspace** | Remove cut/segment |

### Export (Lossless)
| Shortcut | Action |
|---|---|
| **E** | **Export** dialog |
|  | Choose **Normal (keyframe) cut** for truly lossless; **Smart cut** only when you must cut off‑keyframe |
|  | Options: **Include segments** (export only marked parts), **Merge segments** (single file) |

### Seek & Playback
| Shortcut | Action |
|---|---|
| **,** / **.** | Step **1 frame** back / forward |
| **⌥← / ⌥→** | Jump to **prev/next keyframe** *(best for lossless cuts)* |
| **← / →** | Small seek |
| **J / K / L** | Play backward / pause / play forward (tap **L** to speed up) |
| **Space** | Play / pause |
| **⌘← / ⌘→** | Jump ~1% of clip duration |

### Segment Navigation & Batch
| Shortcut | Action |
|---|---|
| **↑ / ↓** | Previous / next **segment** |
| **⇧⌥↑ / ⇧⌥↓** | Jump **and** seek to prev/next segment |
| **⇧↓ / ⇧↑** | Next / previous file |
| **⌃⇧↓ / ⌃⇧↑** | **Open** next / previous file |

> Shortcut behavior can vary slightly by version; adjust in **Settings** if needed.

---

## One‑Time Settings
- **Default export mode:** **Normal / keyframe cut**  
- **Output folder:** a dedicated `01_SELECTS/…` per device (e.g., `PHONE`, `OSMO`)  
- **Container:** keep **same as source** unless you have a reason to change  
- **Time format:** HMS (`00h00m05s`) for readable segment names  
- **Show keyframes:** helpful to land cuts precisely

---

## Filename Pattern (traceable)
Use source name + time ranges for instant provenance:

```
DJI_0123_00m10s-00m21s.mp4
iPhone_4567_02m05s-02m17s.mov
```

---

## Resolve‑Friendly Mini‑Workflow
1. **Triage in Finder:** tag Green (keeper), Red (reject), Blue (B‑roll). Avoid deleting originals yet.  
2. **LosslessCut:** carve selects on keyframes; export with **Normal cut** into `01_SELECTS/...`.  
3. **Import to DaVinci Resolve:** edit on your vertical 4K master timeline (e.g., **2160×3840 @ 25 fps**).  
4. **Deliver:** archive **ProRes 422 + PCM** master; upload **H.264 1080×1920** for socials.

> Tip: For mixed frame rates (e.g., 50 fps action cam + 24 fps phone), a **25 fps** timeline is a neat compromise (50→25 gives perfect 50% slow‑mo; 24→25 only needs a +4.17% speed change).

---

## “Why is it re‑encoding?” (Troubleshooting)
- **Cuts not on keyframes:** switch to **Smart cut** or re‑mark on keyframes.  
- **Codec/container changed:** keep the original container/streams when possible.  
- **Filters applied:** LosslessCut is designed for copy operations—avoid processing filters.  
- **Rotation confusion:** some phones store rotation in metadata. Use a rotation‑aware sort when organizing (ExifTool/ffprobe) or verify orientation in your NLE.

---

## FAQ

**Is “Smart cut” still lossless?**  
Mostly—the untouched parts remain bit‑for‑bit, but LosslessCut re‑encodes small ranges near the cut to achieve frame accuracy.

**Can I join multiple selects into one file?**  
Yes—toggle **Merge segments** in the Export dialog.

**Which formats are supported?**  
Anything ffmpeg can demux: MP4/MOV (H.264/HEVC), MPEG‑TS, MKV, etc. Stability varies by source—test with a short clip first.

**How does this compare to doing trims in Resolve?**  
NLE trims re‑encode on export unless you enable smart‑render workflows. LosslessCut gives you instant, identical‑quality selects before you ever open your NLE.

---

## Download a one‑page cheat sheet
If you prefer a condensed version for your notes app or to print, copy the **“Keyboard Cheat Sheet”** table above as Markdown, or export this page as PDF from your browser.

---

If this guide helped, feel free to link it—credit appreciated.
