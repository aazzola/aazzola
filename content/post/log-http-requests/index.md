---
title: "How to log HTTP requests with PHP"
type: post
draft: false
date: 2010-05-27T00:00:00
---
# How to log HTTP requests with PHP

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2010-05-27 18:11
\[<a href="index.html" target="_self" title="Permalink to How to log HTTP requests with PHP">Permalink</a>\]

## The Problem

Sometimes you need to understand **precisely** how the <a href="http://en.wikipedia.org/wiki/Http#Client_request" target="_blank" title="See what HTTP request means on WikiPedia">HTTP request</a> is submitted to the **server**. If you're working with [Salesforce.com](http://www.salesforce.com "Go to Salesforce.com"), you probably don't have easy or intuitive tools to understand how a message is **serialized** and sent by the runtime to the **server**.

## The Solution

I've put togheter this little script that allows you to draw all <a href="http://en.wikipedia.org/wiki/Http#Client_request" target="_blank" title="See what HTTP request means on WikiPedia">HTTP request</a>s to a file. Becomes so much easier to verify the output sent to a <a href="http://en.wikipedia.org/wiki/Web_service" target="_blank" title="See what web service means on WikiPedia">web service</a>.

    <?php
        $myFile = "requestslog.txt";
        $fh = fopen($myFile, 'a') or die("can't open file");
        fwrite($fh, "\n\n--------------------------------------
            -------------------------\n");
        foreach($_SERVER as $h=>$v)
            if(ereg('HTTP_(.+)',$h,$hp))
                fwrite($fh, "$h = $v\n");
        fwrite($fh, "\r\n");
        fwrite($fh, file_get_contents('php://input'));
        fclose($fh);
        echo "<html><head /><body><iframe src=\"$myFile\"
            style=\"height:100%; width:100%;\"></iframe></body></html>"
    ?>

This applies to all requests that travel with the <a href="http://en.wikipedia.org/wiki/Http" target="_blank" title="See what HTTP protocol means on WikiPedia">HTTP protocol</a>, even <a href="http://en.wikipedia.org/wiki/SOAP" target="_blank" title="See what SOAP means on WikiPedia">SOAP</a> for instance.

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=How%20to%20log%20HTTP%20requests%20with%20PHP&amp;url=http%3a%2f%2fandreaazzola.com%2flog-http-requests%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2flog-http-requests%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

![](/images/39cebc4727e83b50df6dc01c90b776912d049d54.jpg)

Thanks! Saved me some time coding my own solution up!

*~Php Coder*

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