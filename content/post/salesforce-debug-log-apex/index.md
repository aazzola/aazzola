---
title: "Dealing with Salesforce Maximum Debug Log Size"
type: post
draft: false
date: 2013-07-18T00:00:00
categories: ["Salesforce", "Debugging"]
tags: ["Salesforce", "Apex", "Debug Log", "Logging"]
---

When working with *Apex code* that iterates a lot, you may encounter a truncated *log*. The error looks like this:

**MAXIMUM DEBUG LOG SIZE REACHED**

At the time of writing, the maximum allowed size for a *debug log* is **2 MB**.

The default *monitoring level* for *Apex code* includes a lot of clutter you usually don’t need (like `METHOD_ENTRY`, `METHOD_EXIT`). By common practice, you should put a *log filter* on the monitored user, or on the classes involved in the transaction by using an *override flag*.

Unfortunately, the platform does not allow fine‑tuning of log levels. The first filter is specific to your monitoring sessions; the second affects every process or user. My advice: remove any *class‑level* filter override after use.

One useful approach to extract information from a saturated result is lowering the log level. Instead of the default `DEBUG`, set the *Apex code* filter level to `INFO` and then write your debug messages into this less cluttered level:

```apex
System.debug(LoggingLevel.INFO, myVar);
```

This way, you can still capture what’s important while avoiding the 2 MB log limit.

> **Note (2025):** This article is from 2013. Salesforce log size limits and debugging practices may have changed. Check the [Salesforce Developer Documentation](https://developer.salesforce.com/docs/) for up‑to‑date information.