---
title: "Issues With AJAX and a Custom HttpModule"
type: post
draft: false
date: 2005-06-18T00:00:00
categories: ["Programming", "ASP.NET", "AJAX"]
tags: ["HttpModule", "URL Rewriting", "Microsoft AJAX", "ScriptModule", "SEO"]
---

My web app needs to catch every non‑existent path as a search string, because I'm implementing an **HttpModule** that handles URLs in an SEO‑friendly way, e.g.:

```
http://contoso.com/search-string
```

But the Microsoft AJAX **ScriptModule** interfered, causing runtime errors like *"AJAX Framework failed to load…"*. The fix was to register my module **after** the ScriptModule and selectively bypass AJAX requests.

```xml
<add name="ScriptModule"
     type="System.Web.Handlers.ScriptModule, System.Web.Extensions, ..." />
<add name="MyModule" type="MyModule" />
```

```csharp
using System;
using System.Linq;
using System.Web;

public class MyModule : IHttpModule
{
  public void Init(HttpApplication context)
  {
    context.PostResolveRequestCache += Application_OnAfterProcess;
  }

  private void Application_OnAfterProcess(object source, EventArgs e)
  {
    var application = (HttpApplication)source;
    var context = application.Context;

    if (context.Request.Headers["x-microsoftajax"] == null)
    {
      if (!System.IO.File.Exists(application.Request.PhysicalPath) &&
          !application.Request.Url.ToString().Contains(".axd") &&
          !application.Request.Url.ToString().Contains(".asmx"))
      {
        string newUrl = "~/Search.aspx?q=" +
          context.Server.UrlEncode(application.Request.Url.Segments.Last());
        // other logic here…
        context.RewritePath(newUrl);
      }
    }
  }

  public void Dispose() { }
}
```

This runs at **PostResolveRequestCache** and, when the special `x-microsoftajax` header is absent, it rewrites unknown paths to your search page while letting AJAX handlers (`*.axd`, `*.asmx`) pass through normally.