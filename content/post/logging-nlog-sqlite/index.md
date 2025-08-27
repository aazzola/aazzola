---
title: "Logging with NLog and SQLite"
type: post
draft: false
date: 2014-05-06T00:00:00
---
# Logging with NLog and SQLite

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2014-05-06 14:29
\[<a href="index.html" target="_self" title="Permalink to Logging with NLog and SQLite">Permalink</a>\]

Introductory image

This article explains how to achieve a portable and elegant *logging* solution with NLog and SQLite, the solution targets the .NET platform and only requires a few configurations.

## NLog

NLog is a free and lightweight logging library, supports .NET, Silverlight and Windows Phone <http://nlog-project.org/>. It is an excellent option for a wide range of scenarios: from simple day-to-day utilities, to critical production services. It also enables your application to have multiple and diverse targets, both files, databases, output consoles, networks, email and so on are supported.

**Setup**

Package Manager Console:

    PM> Install-Package NLog

NuGet browser:

NLog on NuGet packet manager

## SQLite

[SQLite](http://www.sqlite.org/) is a simple *database engine*, it became famous in the mobile world because of its qualities: a server deamon is not required nor any particular configuration. The database is usually represented by a simple file (usually .db3), read and writes are handled by platform-specific libraries, which usually are available for free.

**Setup**

The most famous interface for .NET is *System.Data.SQLite*

Package Manager Console

    PM> Install-Package System.Data.SQLite

NuGet browser

SQlite on NuGet packet manager

## The NLog configuration file

This is optional, but warmly suggested: have a separate file for *NLog* configurations. Suppose someone screws up the configurations, wouldn't be safer to have just the logging part of your application failing? Separation of concerns, when possibile, is a good thing.

**Setup**

Package Manager Console

    PM> Install-Package NLog.Config

NuGet browser

NLog Configuration on NuGet packet manager

## Get them to work together

1.  **Get the SQLite database ready**, use [SQLite Database Browser](http://sourceforge.net/projects/sqlitebrowser/) or your client of choice to create the database, then execute the following T-SQL statement to create the *Log* table:

         CREATE TABLE Log (Timestamp TEXT, Loglevel TEXT, Logger TEXT,
          Callsite TEXT, Message TEXT)

2.  **Connect your App to the database**, change the NLog configuration as follows:

          <?xml version="1.0" encoding="utf-8" ?>
          <nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             throwExceptions="false">
           <targets>
             <target name="db" xsi:type="Database"
                 dbProvider="System.Data.SQLite" keepConnection="false"
                 connectionString="Data Source=${basedir}\Log.db3;Version=3;"
                 commandText="INSERT into Log(Timestamp, Loglevel, Logger, Callsite, Message)
                  values(@Timestamp, @Loglevel, @Logger, @Callsite, @Message)">

             </target>
           </targets>
           <rules>
             <logger name="*" minlevel="Warn" writeTo="db" />
         </rules>
         </nlog>

3.  **Start logging**

        class Program {
         static Logger log = LogManager.GetCurrentClassLogger();

         static void Main(string[] args)
         {
             log.Info("Logging like a boss");
         }
        }

## Done!

You can review the source code and download the sample project here:
<a href="https://github.com/aazzola/nlog-sqlite/" target="_blank">https://github.com/aazzola/nlog-sqlite/</a>

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Logging%20with%20NLog%20and%20SQLite&amp;url=http%3a%2f%2fandreaazzola.com%2flogging-nlog-sqlite%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2flogging-nlog-sqlite%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

![](/images/39cebc4727e83b50df6dc01c90b776912d049d54.jpg)

For the latest versions of the packages and visual studio 2013 update 3 you need to set the commandType="Text" in the target tag or you will get a method not supported error message.

*~Edgar*

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