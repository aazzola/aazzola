---
title: "Logging con NLog e SQLite"
type: it
draft: false
date: 2014-05-06T00:00:00
---
# Logging con NLog e SQLite

[Andrea Azzola](../../index.html "Back to the Home Page")


Posted on
2014-05-06 14:29
\[<a href="index.html" target="_self" title="Permalink to Logging con NLog e SQLite">Permalink</a>\]

Immagine introduttiva

Questo articolo spiega come ottenere una soluzione di logging portabile ed elegante grazie all'uso di NLog e SQLite, su piattaforma .NET e grazie all'uso di poche configurazioni.

## NLog

NLog é una libreria di logging leggera e gratuita, supporta l'ecosistema .NET (Silverlight, Windows Phone etc…): <http://nlog-project.org/>. Costiusce un'opzione eccellente per un ampio range di scenari: dalle semplici utilities create nel quotidiano a servizi critici di produzione. Consente di avere multipli target, siano essi file, database, righe di comando, rete ed email.

**Installazione**

Package Manager:

    PM> Install-Package NLog

Browser NuGet:

NLog on NuGet packet manager

## SQLite

[SQLite](http://www.sqlite.org/) é semplice *motore di database*, diventato famoso nel mondo mobile grazie alle sue qualitá: per essere eseguito non richiede alcun demone server ne configurazioni particolari. Il database é tipicamente rappresentato da un singolo file (estensione .db3), mentre la lettura e la scrittura vengono gestite dalle librerie specifiche a seconda della piattaforma in cui viene eseguito, ed esse sono solitamente open source.

**Setup**

L'interfaccia .NET piú celebre é *System.Data.SQLite*

Package Manager Console

    PM> Install-Package System.Data.SQLite

NuGet browser

SQlite on NuGet packet manager

## Il file di configurazione NLog

Opzionale ma raccomandabile: l'utilizzo di un file separato per le configurazioni *NLog*. Ad esempio in caso di danneggiamento dello stesso, sarebbe desiderabile che solo la parte di logging fallisse e non l'intera applicazione. Applicare i principi della *separation of concerns*, quando possibile, é sempre un'ottima cosa.

**Installazione**

Package Manager

    PM> Install-Package NLog.Config

Browser NuGet

`NLog Configuration on NuGet packet manager`

## Eseguire NLog e SQLite in tandem

1.  **Predisponi il database SQLite**, usa il [browser di Database SQLite](http://sourceforge.net/projects/sqlitebrowser/) od un client che preferisci per creare il database, quindi esegui il seguente statement T-SQL per creare la *tabella dei Log*:

         CREATE TABLE Log (Timestamp TEXT, Loglevel TEXT, Logger TEXT,
          Callsite TEXT, Message TEXT)

2.  **Connetti l'App al database database**, e modifica la configurazione NLog come segue:

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

3.  **Inizia il logging**

        class Program {
         static Logger log = LogManager.GetCurrentClassLogger();

         static void Main(string[] args)
         {
             log.Info("Logging like a boss");
         }
        }

## Fatto!

Puoi rivedere il codice sorgente e scaricare un progetto di esempio qui:
<a href="https://github.com/aazzola/nlog-sqlite/" target="_blank">https://github.com/aazzola/nlog-sqlite/</a>

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Logging%20con%20NLog%20e%20SQLite&amp;url=http%3a%2f%2fandreaazzola.com%2fit%2flogging-nlog-sqlite%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fit%2flogging-nlog-sqlite%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

![](/images/39cebc4727e83b50df6dc01c90b776912d049d54.jpg)

For the latest versions of the packages and visual studio 2013 update 3 you need to set the commandType="Text" in the target tag or you will get a method not supported error message.

*~Edgar*

Author's portrait

<a href="http://twitter.com/AndreaAzzola" rel="me" target="_blank" data-text="Twitter" title="Stay up to date with my tweets">My Twitter profile</a><a href="http://www.linkedin.com/in/andreaazzola" rel="me" target="_blank" data-text="LinkedIn" title="Find me on LinkedIn">My LinkedIn profile</a><a href="http://www.facebook.com/andrea.azzola" rel="me" target="_blank" data-text="Facebook" title="Get in touch with Facebook">My Facebook profile</a><a href="http://www.pinterest.com/andreaazzola" rel="me" target="_blank" data-text="Pinterest" title="I&#39;m on Pinterest!">My Pinterest profile</a><a href="http://instagram.com/andrea.azzola" rel="me" target="_blank" data-text="Instagram" title="My Instagram profile">My Instagram profile</a>

- <a href="../../about/index.html" style="font-weight:bold" data-text="About" title="Short summary">About</a>
- <a href="../../articles/index.html" style="font-weight:bold" data-text="Articles" title="Collection of all articles in this website">Articles</a>
- <a href="../../books/index.html" style="font-weight:bold" data-text="Books" title="My book recommendations">Books</a>
- <a href="../../contact/index.html" style="font-weight:bold" data-text="Contact" title="Short summary">Contact</a>
- <a href="../../feed/index.html" data-text="RSS feed" title="Subscribe to this blog">RSS feed</a>
- <a href="../../login/index.html" data-text="Login" title="Login">Login</a>

- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageEN%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageEN" class="lang-sm lang-lbl" lang="en"></a>
- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageIT%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageIT" class="lang-sm lang-lbl" lang="it"></a>

#### Newsletter

 
 

<a href="../../category/books/index.html" class="category" style="font-size:112%;">Books</a>
<a href="../../category/decision-fatigue/index.html" class="category" style="font-size:112%;">Decision Fatigue</a>
<a href="../../category/diet/index.html" class="category" style="font-size:112%;">Diet</a>
<a href="../../category/extreme-saving/index.html" class="category" style="font-size:119%;">Extreme Saving</a>
<a href="../../category/finance/index.html" class="category" style="font-size:112%;">Finance</a>
<a href="../../category/financial-independence/index.html" class="category" style="font-size:125%;">Financial Independence</a>
<a href="../../category/fitness/index.html" class="category" style="font-size:119%;">Fitness</a>
<a href="../../category/gears/index.html" class="category" style="font-size:112%;">Gears</a>
<a href="../../category/geo-arbitrage/index.html" class="category" style="font-size:112%;">Geo Arbitrage</a>
<a href="../../category/goal-setting/index.html" class="category" style="font-size:112%;">Goal Setting</a>
<a href="../../category/nutrition/index.html" class="category" style="font-size:112%;">Nutrition</a>
<a href="../../category/personal-branding/index.html" class="category" style="font-size:112%;">Personal Branding</a>
<a href="../../category/personal-development/index.html" class="category" style="font-size:150%;">Personal Development</a>
<a href="../../category/productivity/index.html" class="category" style="font-size:125%;">Productivity</a>
<a href="../../category/time-management/index.html" class="category" style="font-size:106%;">Time Management</a>