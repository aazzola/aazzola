---
title: "Allow the Upload of Large Files with ASP.NET"
type: post
draft: false
date: 2008-06-24T00:00:00
categories: ["Programming", "ASP.NET"]
tags: ["upload", "large files", "Web.config", "httpRuntime"]
---

When working with ASP.NET you may need to increase the default limit for file uploads. By editing the **Web.config** file you can allow larger payloads.

Example configuration:

```xml
<configuration>
  <system.web>
    <httpRuntime
      executionTimeout="240"
      maxRequestLength="16384"
      useFullyQualifiedRedirectUrl="false"
      minFreeThreads="8"
      minLocalRequestFreeThreads="4"
      appRequestQueueLimit="100"
      enableVersionHeader="true" />
  </system.web>
</configuration>
```

This configuration allows the upload of files up to **16 MB**.

> **Note (2025):** The default settings and limits may have changed in more recent versions of ASP.NET/.NET. Check the [Microsoft documentation](https://learn.microsoft.com/aspnet/core/) for updated guidance.