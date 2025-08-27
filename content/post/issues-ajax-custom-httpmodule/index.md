---
title: "Issues With AJAX and a Custom HttpModule"
type: post
draft: false
date: 2005-06-18T00:00:00
---
# Issues With AJAX and a Custom HttpModule

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2005-06-18 17:32
\[<a href="index.html" target="_self" title="Permalink to Issues With AJAX and a Custom HttpModule">Permalink</a>\]

My web app needs to catch every non-existent path as a search string, because I'm implementing an HttpModule that handle URLs in a SEO friendly way:

      http://contoso.com/search-string

But the AJAX script module (a.k.a. "ScriptModule") decides to quit on me. So I add the following module:

``` xml
<add name="ScriptModule"
    type="System.Web.Handlers.ScriptModule, System.Web.Extensions, ..." />
<add name="MyModule" type="MyModule"/>
```

Then Internet Explorer (js debug enabled) decides it was the right time for firing fire some fancy javascript errors, like "AJAX Framework failed to load....". No problem, back to fixer mode... and this snippet is the final, working piece of snippet art:

``` cs
using...

public class MyModule : IHttpModule
{
  public MyModule()
  {
  }

  private void Application_OnAfterProcess(Object source, EventArgs e)
  {
    HttpApplication application = (HttpApplication)source;
    HttpContext context = application.Context;

    if (context.Request.Headers["x-microsoftajax"] == null)
    {
      if ((!System.IO.File.Exists(application.Request.PhysicalPath)) &&
        (!application.Request.Url.ToString().Contains(".axd")) &&
        (!application.Request.Url.ToString().Contains(".asmx")))
        {
          string newUrl = "~/Search.aspx?q="
            + context.Server.UrlEncode(application.Request.Url.Segments.Last());
          ...
          context.RewritePath(newUrl);
        }
     }
  }

  #region IHttpModule Members

  void IHttpModule.Init(HttpApplication context)
  {
    context.PostResolveRequestCache +=
        (new EventHandler(this.Application_OnAfterProcess));
   }
}
```

Basically it intervenes at a specific part of the Request handle (AfterProcess) and just if a certain header is found then excludes the AJAX web services from the search, so they can be dealt with in the classic fashion.

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Issues%20With%20AJAX%20and%20a%20Custom%20HttpModule&amp;url=http%3a%2f%2fandreaazzola.com%2fissues-ajax-custom-httpmodule%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fissues-ajax-custom-httpmodule%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

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