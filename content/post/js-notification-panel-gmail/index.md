---
title: "JavaScript Auto-collapsing Notification Panel"
type: post
draft: false
date: 2009-05-29T00:00:00
---
# JavaScript Auto-collapsing Notification Panel

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2009-05-29 16:33
\[<a href="index.html" target="_self" title="Permalink to JavaScript Auto-collapsing Notification Panel">Permalink</a>\]

In almost all web applications comes the moment when it becomes necessary to show some notifications to the user. Fairly widespread practice even when elegance was unimportant and web pages didn't show great dynamic qualities, was the use of the method *alert()* from JavaScript.

Nowadays, the practice of interacting with the <a href="http://en.wikipedia.org/wiki/Document_Object_Model" target="_blank" title="Document Object Model">DOM</a> is a widespread, so you'd be able to write some functions in a more elegant, advanced and enjoyable way for the user.

This code behaviour you'll find below was made famous by Google mailing client <a href="http://en.wikipedia.org/wiki/Gmail" target="_blank" title="Gmail">Gmail</a>, is nothing exceptional and can be managed with a few simple lines of code:

    Hello World!!!
    (<a OnClick=\"document.getElementById('notification').style.display='none';\">close</a>)

    function closeDiv() {
    document.getElementById('notification').style.display = 'none';
    }

    <input type="button" value="Hide" onclick="window.setTimeout(closeDiv, 5000);" />

You can use CSSs to make your DIV appear like a popup, in addiction, using a graphic library like <a href="http://jquery.com" target="_blank" title="jQuery">jQuery</a> you can easily introduce more advanced text effects.

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=JavaScript%20Auto-collapsing%20Notification%20Panel&amp;url=http%3a%2f%2fandreaazzola.com%2fjs-notification-panel-gmail%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fjs-notification-panel-gmail%2f" target="_blank" title="Share it on Facebook">Facebook</a>
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