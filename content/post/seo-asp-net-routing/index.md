---
title: "Improve ASP.NET SEO by using System.Web.Routing"
type: post
draft: false
date: 2010-01-18T00:00:00
categories: ["SEO", "ASP.NET", "Programming"]
tags: ["System.Web.Routing", "SEO", "ASP.NET", "URL Routing"]
---

This page is specific to Microsoft Visual Studio 2008/.NET Framework 3.5 or higher.

## SEO and ASP.NET

"*As an [Internet marketing](http://en.wikipedia.org/wiki/Internet_marketing) strategy, SEO considers how search engines work and what people search for. Optimizing a website primarily involves editing its content and [HTML](http://en.wikipedia.org/wiki/HTML) [indexing activities](http://en.wikipedia.org/wiki/Web_crawler) of search engines.*" — [wikipedia.org](https://en.wikipedia.org/wiki/Search_engine_optimization)

## Search Engine Friendly URLs vs "Dirty" URLs

Example:

- **SEF URL**: `http://AndreaAzzola.com/seo-asp-net-routing`  
- **RAW URL**: `http://AndreaAzzola.com/Post.aspx?id=cd171f7c-560d-4a62-8d65-16b87419a58c`

**SEFs are better to write, remember, understand, and maintain.** In the example above you can immediately understand what the resource is about, while the RAW version is difficult to read and almost impossible to remember.

## Implementation

ASP.NET offers a resource called **System.Web.Routing**. It supports routes, translating both the pattern you define and the context parameters into intelligible requests. In the following example you will find:

1. How to enable routing in your web application
2. A class that handles routes by implementing `IRouteHandler`
3. How to initialize routes when your application starts
4. How to pass values in a clean and robust manner

### 1. File Web.config

```xml
<system.web>
    <add name="RoutingModule" type="System.Web.Routing.UrlRoutingModule" />
</system.web>
```

### 2. File Global.asax

```csharp
public class EnhancedRouteHandler : IRouteHandler
{
    string _pageURL;

    public EnhancedRouteHandler(string pageURL)
    {
        _pageURL = pageURL;
    }

    public IHttpHandler GetHttpHandler(RequestContext requestContext)
    {
        IRoutePage page =
            BuildManager.CreateInstanceFromVirtualPath(_pageURL,
                typeof(IRoutePage)) as IRoutePage;
        page.Parameters = requestContext.RouteData.Values;
        return page;
    }
}
```

### 3. File Global.asax

```csharp
protected void Application_Start(object sender, EventArgs e)
{
    RegisterRoutes(RouteTable.Routes);
}

public static void RegisterRoutes(RouteCollection routes)
{
    routes.Add(new Route(string.Empty,
        new EnhancedRouteHandler("~/Default.aspx")));
    routes.Add(new Route("post/{slug}",
        new EnhancedRouteHandler("~/Post.aspx")));
    routes.Add(new Route("twitter-mutuality",
        new EnhancedRouteHandler("~/Apps/Mutuality.aspx")));
    routes.Add(new Route("{*catchall}",
        new EnhancedRouteHandler("~/Error.aspx")));
}
```

### 4. File App_Code/IRoutePage.cs

```csharp
using System.Web;
using System.Web.Routing;

public interface IRoutePage : IHttpHandler
{
    RouteValueDictionary Parameters { get; set; }
}
```

By using this code you are obliged to inherit in each page you want to route to, and you should implement the `Parameters` field as well. However, it doesn’t require you to expose inappropriate query strings or sessions that would damage the aesthetics of your code. This won’t cover all possible cases, but it helps with most of them.

## In Conclusion

In recent years we have witnessed a turnaround in the development of web applications, especially since technology made it possible to enlarge the catchment area. Just think about mobile and netbook growth: this has helped to promote a simple and functional web at the expense of a powerful but less usable one.

**SEFs** are an important way to catch the user’s attention. For example, when you look at a Google results page, do you prefer to click the clean URL or the dirty one? Not all clean URLs are the most attractive, but in most cases you will choose the simple one, which can give an important point for your SEO score.