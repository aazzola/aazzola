---
title: "Future Count with Apex Code"
type: post
draft: false
date: 2011-07-14T00:00:00
categories: ["Programming", "Salesforce"]
---

A simple snippet for counting `@future` calls in a 24‑hour timespan, useful for monitoring peaks and acting accordingly.

**Please note**: supports up to 50,000 future calls in a 24h timespan.

```apex
public with sharing class AsyncApexJobUtils {
    public static integer futureCount() {
        integer c = [select count() from AsyncApexJob
            where JobType='Future'
            and CreatedDate >= :Datetime.now().addDays(-1) limit 50000];
        system.debug('#futureCount: ' + c);
        return c;
    }
}
```