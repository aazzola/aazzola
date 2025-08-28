---
title: "Simulating a RequiredFieldValidator when using a RadComboBox"
type: post
draft: false
date: 2010-10-22T00:00:00
---
# Simulating a RequiredFieldValidator when using a RadComboBox

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2010-10-22 13:44
\[<a href="index.html" target="_self" title="Permalink to Simulating a RequiredFieldValidator when using a RadComboBox">Permalink</a>\]

Telerik's <a href="http://www.telerik.com/products/aspnet-ajax/combobox.aspx" target="_blank">RadComboBox</a> does not behave like a traditional <a href="https://msdn.microsoft.com/en-us/library/system.web.ui.webcontrols.dropdownlist.aspx" target="_blank">DropDownList</a>. You may consider to use a <a href="https://msdn.microsoft.com/en-us/library/system.web.ui.webcontrols.customvalidator.aspx" target="_blank">CustomValidator</a> instead, here is the code:

## Step 1: Markup

    <asp:Label ID="lblExample" runat="server" AssociatedControlID="rcbExample"
        Text="Example" />
    <telerik:RadComboBox ID="rcbExample" runat="server" />
    <asp:CustomValidator ID="cvlExample" runat="server" ControlToValidate="rcbExample"
        Text="*" ClientValidationFunction="cvlExampleValidate"
        OnServerValidate="cvlExample_ServerValidate" />

## Step 2: Client-side validation:

    function cvlExampleValidate(source, args) {
        args.IsValid = radComboValidate("<%= rcbExample.ClientID %>");
    }

    function radComboValidate(controlName) {
        var combo = $find(controlName);
        var text = combo.get_text();

        if (text.length < 1)
            return false;
        else {
            var node = combo.findItemByText(text);
            if (node) {
                var value = node.get_value();

                if (value.length > 0)
                    return true;
            }
            else
                return false;
        }
    }

## Step 3: Server-side valitation:

    protected void cvlStatus_ServerValidate(object source, ServerValidateEventArgs args)
    {
        args.IsValid = rcbStatus.SelectedValue.Length > 0;
    }

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Simulating%20a%20RequiredFieldValidator%20when%20using%20a%20RadComboBox&amp;url=http%3a%2f%2fandreaazzola.com%2frequiredfieldvalidator-radcombobox%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="https://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2frequiredfieldvalidator-radcombobox%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

![](/images/39cebc4727e83b50df6dc01c90b776912d049d54.jpg)

Thanks, this was useful.

*~Tom*

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