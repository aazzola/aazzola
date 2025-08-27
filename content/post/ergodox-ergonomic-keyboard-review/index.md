---
title: "ErgoDox Split Ergonomic Keyboard Review"
type: post
draft: false
date: 2014-12-09T00:00:00
categories: ["Gears", "Ergonomic"]
---

The **ErgoDox** is a DIY ergonomic keyboard, featuring a *split design*—each half, one hand. The two halves are connected with a *phone TRRS connector cable*, while the connection to the PC—or Mac or Unix—is obtained through a detachable mini USB.

## History

The project [has been initiated](https://geekhack.org/index.php?topic=22780.0) by Dominic Beauchamp—aka Dox, from which the keyboard name derives—on the GeekHack.org forum; the design has been largely inspired by the [Key64](http://www.key64.org/) project by Nestor Diaz.

The ErgoDox keyboard is licensed with GNU GPL v3, everybody can make their own modifications, with the only constraint that the original name *ErgoDox* is protected.

## The Keyboard

The keyboard itself accommodates approximately 76 keys. The size of keycaps may vary according to function and position. Keycaps can be repositioned according to preference and keys themselves—thanks to a [Teensy 2.0 AVR Microcontroller](https://www.pjrc.com/store/teensy.html)—can be remapped to accomplish different layouts—QWERTY, Dvorak, Colemak, etc.—and/or personal preferences.

The typical ErgoDox sports **Cherry MX** switches. It can, of course, mount any type of commercial Cherry MX. **ALP** switches are another option. As for keys, the most popular are [Signature Plastics PBT DSA keycaps](http://keyshop.pimpmykeyboard.com/products/full-keysets/dsa-blank-sets-1), which are characterized by their rounded shape, a low profile, nice textured surface and no legend—commonly referred to as *ninja* or *stealth*.

There are three casings for sale that I personally know about:

1. The [original case designed by Dox](http://ergodox.org/Downloads.aspx), the most refined version but also the least popular due to 3D printing costs.
2. The *acrylic case by lilster*, is the one you see in the pictures; it is made of sheets of acrylic stacked together, and it is completely transparent. On mine there's a top aluminum plate, but just for a more minimalistic/rugged look.
3. The *PVC case by Falbatech*, available both in [white](http://falbatech.pl/prestashop/index.php?id_product=9&controller=product) and [black](http://falbatech.pl/prestashop/index.php?id_product=23&controller=product), probably one of the best compromises in terms of look/price ratio right now.

## Feel

The fingers can *spread horizontally* and stay relaxed, benefiting from a more open and natural course of movement, each key within reach. This is thanks to the fact that keycaps are distributed in **columns** instead of rows. Thumbs *have their own set of keys*, and being the thumbs the most powerful and usually neglected fingers, this is a big deal—normally you would use just one and only for the spacebar. Wrists won't move much like they would on a normal keyboard—except for a few key combos—resulting in diminished/absent wrist pain over prolonged periods of use.

I definitely recommend it to a 9-to-5 computer user. It may take some effort to adapt, but it pays back with interest. Especially if you're a typist, writing a book or articles, the ErgoDox feels like the fountain pen of keyboards. *Software developers* and *gamers* might find it a little bit limiting, because of the missing function keys which many IDEs and games take advantage of. Although keys can be remapped, I do see some difficulties with more intricate patterns. It can even backfire as a collaboration deterrent—I advise keeping a normal keyboard always connected to the workstation, as a courtesy to colleagues.

## How to Buy

The *ErgoDox* can't be purchased from any official store or retailer; it must be built, unless someone is willing to sell their own, which is rare. Luckily, there are a few people that offer assembly as a service.

Electronic parts can be bought through [Massdrop](https://www.massdrop.com/r/KEP8XC). Massdrop is a company focused on *group buys*: users commit to buying a certain item, and if enough committers are reached, the group buy—aka *drop*—gets submitted to the supplier. Multiple suppliers may be involved, but Massdrop will take care of all the logistics, charge you one single payment and ship the whole package.

It should be noted that *drops*, because of their crowdsourced nature, are not always open; instead, they're based on the sum of *user requests* for the item. Typically—at the time of writing—new drops for ErgoDoxes are opened *every few months*.

But shipping costs and import taxes from the U.S. might spike the deal. A more budget-friendly alternative for **Europeans** would be [Falbatech](http://falbatech.pl), a Polish company started by two brothers; it sells pretty much all the parts, plus optional assembly.

## Ergodox Assembly

Parts:

- 1x Teensy 2.0 AVR Microcontroller
- 2 Cases (PVC/Layered acrylic/3D) and screws
- 2 PCB
- 76-80 × Cherry MX switches
- 76-80 × 1N4148W-7-F diodes (through-hole/SMD)
- 1 × MCP23018 I/O expander
- 2 × 3.5mm TRRS connectors
- 1 × TRRS cable
- 1 × USB mini B plug
- 1 × 0.1uF ceramic capacitor
- 1 × 2.2k ohm resistor
- 3 × 3mm T1 LED
- 2 × 220 ohm resistors
- 2 × USB cable Male A to Male mini B

First thing to consider is **soldering**. If you're new to this, [YouTube tutorials](https://www.youtube.com/results?search_query=smd+soldering+tutorial) are a good starting point. You'll need at minimum:

- **SMD soldering iron** with fine tip (scalpel even better)
- **Solder wire**
- **Solder wick** for cleaning excess solder or for reworks

The following resources describe the process in detail. **WhiteFireLion's video** in particular is very comprehensive.

Another great resource is the [Massdrop Assembly Instructions](https://www.massdrop.com/ext/ergodox/assembly) page.

## References

- [Massdrop](https://www.massdrop.com/r/KEP8XC) ErgoDox group buys
- [Deskthority](http://deskthority.net/wiki/ErgoDox) in-depth review
- [GeekHack.org](http://geekhack.org) community of keyboard enthusiasts
- [ErgoDox Project Page](http://ergodox.org)