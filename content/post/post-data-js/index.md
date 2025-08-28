---
title: "POST data with JavaScript"
type: post
draft: false
date: 2009-07-07T00:00:00
---
# POST data with JavaScript

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2009-07-07 12:07
\[<a href="index.html" target="_self" title="Permalink to POST data with JavaScript">Permalink</a>\]

**The <a href="http://www.w3.org/TR/html401/" target="_blank" title="HTML 4.0 specifications by W3C reccomendation">HTML 4.0 specs</a>**

- If the method is "get" - -, the user agent takes the value of action, appends a ? to it, then appends the form data set, encoded using the application/x-www-form-urlencoded content type. The user agent then traverses the link to this URI. In this scenario, form data are restricted to ASCII codes.
- If the method is "post" --, the user agent conducts an HTTP post transaction using the value of the action attribute and a message created according to the content type specified by the enctype attribute.

**What are the benefits of performing POSTs via JavaScript?**

- Perform redirects programmatically
- Post data without annoying the user
- Avoid the misuse of query string and beautify URLs

## The 'post' function

Copy and paste the following code in the <a href="https://en.wikipedia.org/wiki/HTML_element" target="_blank" title="HEAD section on Wikipedia">HEAD</a> section of your <a href="https://en.wikipedia.org/wiki/Html" target="_blank" title="HTML on Wikipedia">HTML</a> page

    <script language="javascript">
    function post(dictionary, url, method) {
        method = method || "post"; // post (set to default) or get

        // Create the form object
        var form = document.createElement("form");
        form.setAttribute("method", method);
        form.setAttribute("action", url);

        // For each key-value pair
        for (key in dictionary) {
            //alert('key: ' + key + ', value:' + dictionary[key]); // debug
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", dictionary[key]);
            // append the newly created control to the form
            form.appendChild(hiddenField);
        }

        document.body.appendChild(form); // inject the form object into the body section
        form.submit();
    }
    </script>

**How do I use it?**
Copy the following code in the <a href="https://en.wikipedia.org/wiki/Body_text#Document_elements" target="_blank" title="BODY section on Wikipedia">BODY</a> section of your HTML page.
As you can see a dictionary object is declared as first, then two parameters are added.
You can add as many parameters as you need.

    <script language="javascript">
        var myDictionary = [];
        myDictionary["1stKey"] = "1stValue";
        myDictionary["2ndKey"] = "2ndValue";
    </script>

    <input type="button" value="Click me to POST"
        onclick="javascript:post(myDictionary, 'destination.html');" />
    <input type="button" value="Click me to GET"
        onclick="javascript:post(myDictionary, 'destination.html', 'get');" />

The post function accepts a <a href="https://en.wikipedia.org/wiki/Associative_array" target="_blank" title="Associative array on Wikipedia">dictionary</a> object, a destination <a href="https://en.wikipedia.org/wiki/Url" target="_blank" title="Uniform Resource Locator on Wikipedia">URL</a>, and optionally, the method (post or get, case in-sensitive).

## The jQuery.post() alternative

If *jQuery* is already part of your solution, you may want to try the *jQuery.post()* approach instead:

    jQuery.post( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )

which is a shorthand for the Ajax function:

    $.ajax({
      type: "POST",
      url: url,
      data: data,
      success: success,
      dataType: dataType
    });

So, the equivalent *jQuery* code for *POST*ing the above-mentioned values would be:

    $.post( "test.php", { 1stKey: "1stValue", 2ndKey: "2ndValue" } );

Further details about *jQuery.post()* function can be found <a href="http://api.jquery.com/jquery.post/" target="_blank" title="jQuery.post() wiki">here</a>

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=POST%20data%20with%20JavaScript&amp;url=http%3a%2f%2fandreaazzola.com%2fpost-data-js%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="https://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fpost-data-js%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

Author's portrait

<a href="https://twitter.com/AndreaAzzola" rel="me" target="_blank" data-text="Twitter" title="Stay up to date with my tweets">My Twitter profile</a><a href="https://www.linkedin.com/in/andreaazzola" rel="me" target="_blank" data-text="LinkedIn" title="Find me on LinkedIn">My LinkedIn profile</a><a href="https://www.facebook.com/andrea.azzola" rel="me" target="_blank" data-text="Facebook" title="Get in touch with Facebook">My Facebook profile</a><a href="http://www.pinterest.com/andreaazzola" rel="me" target="_blank" data-text="Pinterest" title="I&#39;m on Pinterest!">My Pinterest profile</a><a href="https://instagram.com/andrea.azzola" rel="me" target="_blank" data-text="Instagram" title="My Instagram profile">My Instagram profile</a>

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