---
title: "Handle Multiple Columns as One with Dynamic Data"
type: post
draft: false
date: 2008-11-02T00:00:00
---
# Handle Multiple Columns as One with Dynamic Data

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2008-11-02 15:50
\[<a href="index.html" target="_self" title="Permalink to Handle Multiple Columns as One with Dynamic Data">Permalink</a>\]

I need to schedule some tasks with ASP .NET and save a "Start date" and an "Interval", stored respectively as date (<a href="http://msdn.microsoft.com/en-us/library/system.datetime.aspx" target="_blank">DateTime</a>) and long (<a href="http://msdn.microsoft.com/en-us/library/system.datetime.aspx" target="_blank">TimeSpan.Ticks</a>) in my database.

Editing ticks values is not exactly what I define good UX, so I binded the proper <a href="http://msdn.microsoft.com/en-us/library/system.datetime.aspx" target="_blank">MetaColumn</a>, to the proper <a href="http://msdn.microsoft.com/en-us/library/system.web.dynamicdata.metacolumn.uihint.aspx" target="_blank">UIHint</a>. After a few tests, I noticed how my GUI was - working, but not easy to understand as I was expecting.

I decided to deeply customize the <a href="http://msdn.microsoft.com/en-us/library/system.web.dynamicdata.fieldtemplateusercontrol.aspx" target="_blank">FieldTemplateUserControl</a> of Dynamic Data, to display and save multiple Columns I needed (Start Date, Start Time, Occours - Daily, Weekly, Monthly.., etc...). The solution is really simple, but there are few points you may need to bear in mind:

## How to retrieve values (Schedule_EditField.ascx.cs)

:

    protected override void OnDataBinding(EventArgs e)
      {
        base.OnDataBinding(e);
        DateTime? startFrom = (DateTime?)Eval("StartFrom");
        long? timeIntervalTicks = (long?)Eval("TimeInterval");
        DateTime? lastExecution = (DateTime?)Eval("LastExecution");
      }

## How to store values

    protected override void ExtractValues(IOrderedDictionary dictionary)
      {
        dictionary["StartFrom"] = …; //logic here
        dictionary["TimeInterval"] = …;  //logic here
      }

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Handle%20Multiple%20Columns%20as%20One%20with%20Dynamic%20Data&amp;url=http%3a%2f%2fandreaazzola.com%2fmultiple-columns-dynamic-data%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fmultiple-columns-dynamic-data%2f" target="_blank" title="Share it on Facebook">Facebook</a>
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