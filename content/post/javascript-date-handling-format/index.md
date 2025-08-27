---
title: "Manage and format Dates with JavaScript"
type: post
draft: false
date: 2013-11-14T00:00:00
---
# Manage and format Dates with JavaScript

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2013-11-14 11:39
\[<a href="index.html" target="_self" title="Permalink to Manage and format Dates with JavaScript">Permalink</a>\]

JavaScript has a ***Date* object** wich you can use to handle dates. Supported *constructors* are:

    new Date() // with current date and time
    new Date(numeric) // by adding N milliseconds to the Unix epoch time (1970-01-01T00:00:00Z)
    new Date(year, month, day, hour, minute, second, millisecond)
    new Date(year, month, day) // the time part will equal "00:00.000"

There are some built-in methods that can be used to extract or set dateparts:

    .getDate() // get the day part [1-31]
    .getDay() // get the week day [0-6]
    .getFullYear() // get the four digits year part
    .getHours() // get the hour part
    .getMinutes() // get the minutes part
    .getSeconds() // get the seconds part
    .getMilliseconds() // get the millisencond part

    .setDate() // set the day part [1-31]
    .setDay() // set the week day [0-6]
    .setFullYear() // set the four digits year part
    .setHours() // set the hour part
    .setMinutes() // set the minutes part
    .setSeconds() // set the seconds part
    .setMilliseconds() // set the millisencond part

And their <a href="http://en.wikipedia.org/wiki/Coordinated_Universal_Time" target="_blank" title="Coordinated Universal Time definition on Wikipedia">**UTC**</a> variant:

    .getDate() // get the UTC date day part [1-31]
    .getUTCDay() // get the UTC week day [0-6]
    .getUTCFullYear() // get the UTC four digits year part
    .getUTCHours() // get the UTC hour part
    .getUTCMinutes() // get the UTC minutes part
    .getUTCSeconds() // get the UTC seconds part
    .getUTCMilliseconds() // get the UTC millisecond part

    .setUTCDate() // set the UTC day part [1-31]
    .setUTCDay() // set the UTC week day [0-6]
    .setUTCFullYear() // set the UTC four digits year part
    .setUTCHours() // set the UTC hour part
    .setUTCMinutes() // set the UTC minutes part
    .setUTCSeconds() // set the UTC seconds part
    .setUTCMilliseconds() // set the UTC millisecond part

As per formatting, there are two simple options:

1\) A combo of the aforementioned methods

    var myDate = new Date();
    alert(myDate.getFullYear() + '-' + myDate.getMonth() + '-' myDate.getDay());

2\) A dedicated library like **<a href="http://momentjs.com/" target="_blank" title="A javascript date library for parsing, validating, manipulating, and formatting dates">Moment.js</a>**

    var myDate = moment(new Date(1970, 1, 1));
    myDate.format('MMMM Do YYYY, h:mm:ss a'); // displays January 1st 1970, 1:00:00 pm
    myDate.format('dddd'); // displays Thursday
    myDate.format(); // displays 1970-01-01T00:00:00+00:00

**Moment.js** also supports *validations*, *UTC*, *timespans* and [many more](http://momentjs.com/docs/ "Moment.js documentation")...

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Manage%20and%20format%20Dates%20with%20JavaScript&amp;url=http%3a%2f%2fandreaazzola.com%2fjavascript-date-handling-format%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fjavascript-date-handling-format%2f" target="_blank" title="Share it on Facebook">Facebook</a>
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