---
title: "Manage and format Dates with JavaScript"
type: post
draft: false
date: 2013-11-14T00:00:00
categories: ["Programming", "JavaScript"]
tags: ["date", "format", "UTC", "Moment.js"]
---

> **Update (2025):** This article was written in 2013. It still offers useful basics, but a few notes:
> - `Date.getMonth()` is **zero‑based** (January = 0). `Date.getDay()` returns the **weekday** (0–6), not the day of month. There is **no** `setDay()` or `setUTCDay()` method in JavaScript.
> - <a href="https://momentjs.com/" target="_blank" rel="noopener">Moment.js</a> is in **maintenance mode**; modern alternatives include <a href="https://moment.github.io/luxon/" target="_blank" rel="noopener">Luxon</a>, <a href="https://date-fns.org/" target="_blank" rel="noopener">date‑fns</a>, and native 
`Intl.DateTimeFormat`. Consider these for new projects.

JavaScript has a **`Date` object** you can use to handle dates. Supported constructors are:

```js
new Date()
new Date(msSinceUnixEpoch)
new Date(year, month, day, hour, minute, second, millisecond)
new Date(year, month, day)
```

There are built‑in methods to extract or set date parts (local time):

```js
.getDate()        // 1–31
.getDay()         // 0–6 (Sun–Sat)
.getFullYear()
.getHours()
.getMinutes()
.getSeconds()
.getMilliseconds()

.setDate(n)
.setFullYear(y)
.setHours(h)
.setMinutes(m)
.setSeconds(s)
.setMilliseconds(ms)
```

And their **UTC** variants:

```js
.getUTCDate()
.getUTCDay()
.getUTCFullYear()
.getUTCHours()
.getUTCMinutes()
.getUTCSeconds()
.getUTCMilliseconds()

.setUTCDate(n)
.setUTCFullYear(y)
.setUTCHours(h)
.setUTCMinutes(m)
.setUTCSeconds(s)
.setUTCMilliseconds(ms)
```

### Formatting options

1) **Manual formatting** by combining getters:

```js
const d = new Date();
const yyyy = d.getFullYear();
const mm = String(d.getMonth() + 1).padStart(2, "0");
const dd = String(d.getDate()).padStart(2, "0");
const out = `${yyyy}-${mm}-${dd}`; // e.g. 2025-08-28
```

2) **A dedicated library** such as **Moment.js** (legacy), **Luxon**, or **date‑fns**:

```js
// date-fns example
import { format } from "date-fns";
format(new Date(1970, 0, 1), "MMMM do yyyy, h:mm:ss a");
```

For UTC/time‑zones and rich formatting in the platform, consider `Intl.DateTimeFormat`:

```js
new Intl.DateTimeFormat("en-GB", { dateStyle: "long", timeStyle: "medium", timeZone: "UTC" }).format(new Date());
```