---
title: "MavensMate unable to reach GitHub on Windows"
type: post
draft: false
date: 2014-04-06T00:00:00
---
# MavensMate unable to reach GitHub on Windows

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2014-04-06 09:22
\[<a href="index.html" target="_self" title="Permalink to MavensMate unable to reach GitHub on Windows">Permalink</a>\]

<a href="http://mavensmate.com/" target="_blank" title="Mavens Mate page">MavensMate</a> is a great plugin for the Force.com platform, built on the <a href="http://www.sublimetext.com/" target="_blank" title="Sublime Text page">Sublime Text IDE</a>. It is provided by the community (with <a href="http://www.joe-ferraro.com/" target="_blank" title="Joe Ferraro personal website">Joe Ferraro</a> as the creator and main contributor) as a free alternative to the well known <a href="https://wiki.developerforce.com/page/Force.com_IDE" target="_blank" title="Force.com IDE official page">Force.com IDE</a> shipped by *Salesforce.com*.

Now, if you install the plugin on a Microsoft Windows 7 o 8 workstation, under certain conditions (usually proxy or firewalling, however not my case) you may get the following error:

Installation of Sublime Text plugin failed. This is likely due to the installer being unable to reach GitHub. If you are behind a firewall or using a proxy, you should configure git accordingly (google: git config --global https.proxy) and ensure your HTTPS/HTTPS_PROXY environment variable(s) are set properly. Otherwise, please log an issue on the MavensMate GitHub project.

 

 

There's already an <a href="https://github.com/joeferraro/MavensMate/issues/113" target="_blank" title="MavensMate issue">issue</a> on GitHub for this, and a useful workaround by *Joe Ferraro* himself.
These are the lines that worked for me:

1.  Fire up the shell/bash and move to the MavensMate plugin directory (replace the *username* and *root* if needed)

        cd "C:\Users\username\AppData\Roaming\Sublime Text 3\Packages"

2.  Launch the following script

        git clone --recursive http://github.com/joeferraro/MavensMate-SublimeText.git MavensMate
        cd MavensMate
        git submodule init
        git submodule update

Supposedly, when you'll run *Sublime Text* again, *MavensMate* will be there.
But you're not done yet, remeber to configure the workspace through the menu *MavensMate - Setting*.

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=MavensMate%20unable%20to%20reach%20GitHub%20on%20Windows&amp;url=http%3a%2f%2fandreaazzola.com%2fmavensmate-unable-github-windows%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fmavensmate-unable-github-windows%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

![](/images/39cebc4727e83b50df6dc01c90b776912d049d54.jpg)

I've always had problems with installing MM, and any time it tried to auto updated I had to rehash a new way to try to get things at least stable. This solution was perfect, and so easy. Thank you!

*~gougs06*

![](/images/39cebc4727e83b50df6dc01c90b776912d049d54.jpg)

Thank you so much! This worked :)

*~Hari*

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment2&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment2" class="action">Post a new comment</a>

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