---
title: "Improve ASP.NET SEO by using System.Web.Routing"
type: post
draft: false
date: 2010-01-18T00:00:00
---
# Improve ASP.NET SEO by using System.Web.Routing

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2010-01-18 20:57
\[<a href="index.html" target="_self" title="Permalink to Improve ASP.NET SEO by using System.Web.Routing">Permalink</a>\]

This page is specific to Microsoft Visual Studio 2008/.NET Framework 3.5 or higher

## SEO and ASP.NET

"*As an [Internet marketing](http://en.wikipedia.org/wiki/Internet_marketing "Internet marketing") strategy, SEO considers how search engines work and what people search for. Optimizing a website primarily involves editing its content and [HTML](http://en.wikipedia.org/wiki/HTML "HTML") [indexing activities](http://en.wikipedia.org/wiki/Web_crawler "Web crawler") of search engines.*" \[source: <a href="http://en.wikipedia.org/wiki/Search_engine_optimization" id="d5rp" title="wikipedia.org">wikipedia.org</a>\]

## Search Engine Friendly URLs vs "Dirty" URLs

Current URL will be taken as example

- SEF URL
  : http://AndreaAzzola.com/seo-asp-net-routing
- RAW URL
  : http://AndreaAzzola.com/Post.aspx?id=cd171f7c-560d-4a62-8d65-16b87419a58c

**SEFs are better to write, remember, understand and mantain**. In the example above you can understand immediatly what the resource is about but the RAW version is difficult to read and almost impossible to rember.

## Implementation

ASP.NET offers a great resource called 'System.Web.Routing', it support routes. Routes translates both the pattern you define and the context parameters, into an intelligible request. In the following example you will find:

1.  How to enable routing on your web application
2.  A class that handle routes by implementing IRouteHandler
3.  How to initialize routes when your application starts
4.  How to pass values in a clean and robust manner

### \#1 File Web.config

``` xml
<system.web>
        ...
        <add name="RoutingModule" type="System.Web.Routing.UrlRoutingModule" />
</system.web>
```

### \#2 File Global.asax

``` cs
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

### \#3 File Global.asax

``` cs
protected void Application_Start(object sender, EventArgs e)
{
    RegisterRoutes(RouteTable.Routes);
}

public static void RegisterRoutes(RouteCollection routes)
{
    routes.Add(new Route(string.Empty,
        new EnhancedRouteHandler("~/Default.aspx"))); // nothing after domain name
    routes.Add(new Route("post/{slug}",
        new EnhancedRouteHandler("~/Post.aspx"))); // post followed by his slug
    routes.Add(new Route("twitter-mutuality",
        new EnhancedRouteHandler("~/Apps/Mutuality.aspx"))); // a fixed path
    routes.Add(new Route("{*catchall}",
        new EnhancedRouteHandler("~/Error.aspx"))); // catchall
}
```

The catchall part works whenever the engine does not find a suitable resource or route for the request, this behaviour is extremely helpful expecially when dealing with 404 error or moved resources.

### \#4 File App_Code\IRoutePage.cs

``` cs
using System.Web;
using System.Web.Routing;

public interface IRoutePage : IHttpHandler
{
    RouteValueDictionary Parameters { get; set; }
}
```

By using this code you are obliged to inherit in each page you want to route to, and you should implement the Parameters field as well, however it doesn't require you to expose unappropriate querystrings or dangerous sessions that would damage the aesthetics of your code :D. Be aware, this won't cover all the possible test cases, but it would help with the most of them.

## In Conclusion

In recent years we have witnessed a turnaround in the development of web-applications, especially since the technology made it possible to enlarge the catchment area, just think about mobile, MID/Netbook sales growth, disadvantage people... this has helped to promote a web simple and functional at the expense of a powerful web, but less usable.

SEFs are an important way to catch the guest's attention, please consider for example the Google' results page, search anything you want, and think about the link you'll choose, the clean one, or the dirty one? Not all clean URLs are the most attractives yet, but there are a good changes you will choose the simple one, this would mean an important point for your SEO score.

Categories:
<a href="../category/seo.html" class="tag">SEO</a>

Share on:
<a href="https://twitter.com/intent/tweet?text=Improve%20ASP.NET%20SEO%20by%20using%20System.Web.Routing&amp;url=http%3a%2f%2fandreaazzola.com%2fseo-asp-net-routing%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fseo-asp-net-routing%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

![](/images/39cebc4727e83b50df6dc01c90b776912d049d54.jpg)

Really useful article! Minimal blog graphic! ;)

*~Salvatore*

Author's portrait

<a href="http://twitter.com/AndreaAzzola" rel="me" target="_blank" data-text="Twitter" title="Stay up to date with my tweets">My Twitter profile</a><a href="http://www.linkedin.com/in/andreaazzola" rel="me" target="_blank" data-text="LinkedIn" title="Find me on LinkedIn">My LinkedIn profile</a><a href="http://www.facebook.com/andrea.azzola" rel="me" target="_blank" data-text="Facebook" title="Get in touch with Facebook">My Facebook profile</a><a href="http://www.pinterest.com/andreaazzola" rel="me" target="_blank" data-text="Pinterest" title="I&#39;m on Pinterest!">My Pinterest profile</a><a href="http://instagram.com/andrea.azzola" rel="me" target="_blank" data-text="Instagram" title="My Instagram profile">My Instagram profile</a>

- <a href="../about/index.html" style="font-weight:bold" data-text="About" title="Short summary">About</a>
- <a href="../articles/index.html" style="font-weight:bold" data-text="Articles" title="Collection of all articles in this website">Articles</a>
- <a href="../books/index.html" style="font-weight:bold" data-text="Books" title="My book recommendations">Books</a>
- <a href="../contact/index.html" style="font-weight:bold" data-text="Contact" title="Short summary">Contact</a>
- <a href="../feed/index.html" data-text="RSS feed" title="Subscribe to this blog">RSS feed</a>
- <a href="../login/index.html" data-text="Login" title="Login">Login</a>

- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageEN%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageEN" class="lang-sm lang-lbl" lang="en"></a>
- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageIT%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageIT" class="lang-sm lang-lbl" lang="it"></a>

#### Newsletter

 
 

<a href="../category/books/index.html" class="category" style="font-size:112%;">Books</a>
<a href="../category/decision-fatigue/index.html" class="category" style="font-size:112%;">Decision Fatigue</a>
<a href="../category/diet/index.html" class="category" style="font-size:112%;">Diet</a>
<a href="../category/extreme-saving/index.html" class="category" style="font-size:119%;">Extreme Saving</a>
<a href="../category/finance/index.html" class="category" style="font-size:112%;">Finance</a>
<a href="../category/financial-independence/index.html" class="category" style="font-size:125%;">Financial Independence</a>
<a href="../category/fitness/index.html" class="category" style="font-size:119%;">Fitness</a>
<a href="../category/gears/index.html" class="category" style="font-size:112%;">Gears</a>
<a href="../category/geo-arbitrage/index.html" class="category" style="font-size:112%;">Geo Arbitrage</a>
<a href="../category/goal-setting/index.html" class="category" style="font-size:112%;">Goal Setting</a>
<a href="../category/nutrition/index.html" class="category" style="font-size:112%;">Nutrition</a>
<a href="../category/personal-branding/index.html" class="category" style="font-size:112%;">Personal Branding</a>
<a href="../category/personal-development/index.html" class="category" style="font-size:150%;">Personal Development</a>
<a href="../category/productivity/index.html" class="category" style="font-size:125%;">Productivity</a>
<a href="../category/time-management/index.html" class="category" style="font-size:106%;">Time Management</a>