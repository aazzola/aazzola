---
title: "Eseguire ASP.NET vNext su Mac OS con Kulture e Omnisharp"
type: it
draft: false
date: 2014-12-20T00:00:00
---
# Eseguire ASP.NET vNext su Mac OS con Kulture e Omnisharp

[Andrea Azzola](../../index.html "Back to the Home Page")


Posted on
2014-12-20 07:15
\[<a href="index.html" target="_self" title="Permalink to Eseguire ASP.NET vNext su Mac OS con Kulture e Omnisharp">Permalink</a>\]

L'articolo descrive **come eseguire ASP.NET vNext** con sistema operativo *Mac OS X*. La procedura richiede alcuni passaggi é necessario un pizzico di pazienza, fortunatamente OS X include il software prerequisito *Ruby* alla versione 2.0 su Mavericks e Yosemite, 1.8.7 su Mountain Lion, Lion e Snow Leopard.

## Sublime Text

Un *text editor avanzato* molto diffuso per Mac OS X é **<a href="http://www.sublimetext.com/" target="_blank" title="Sito ufficiale di Sublime Text">Sublime Text</a>**, personalmente lo uso in Windows, per sviluppare soluzioni <a href="https://andreaazzola.com/category/salesforcecom" target="_blank" title="Salesforce.com posts">Salesforce.com</a> o piú semplicemente prendere note e redarre questo articolo in HTML. Altri editor dichiarati supportati—nel momento in cui scrivo—sono:

- Atom - <a href="https://atom.io/" target="_blank" title="Atom editor">https://atom.io/</a>
- Emacs - <a href="http://www.gnu.org/software/emacs/" target="_blank" title="Emacs editor">http://www.gnu.org/software/emacs/</a>
- Brackets - <a href="https://brackets.io/" target="_blank" title="Brackets editor">http://brackets.io/</a>
- Vim - <a href="http://www.vim.org/" target="_blank" title="Vim editor">http://www.vim.org/</a>

## Homebrew

<a href="https://brew.sh/" target="_blank">Homebrew</a> é un *package manager* open source per Mac OS X, per funzionare necessita di *git* e di *ruby*. Per verificarne l'installazione é sufficiente aprire il terminale e lanciare il comando `brew doctor`. Se l'esito é `command not found` significa che brew, non é installato; possiamo provvedere con il seguente comando:`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## KVM, Mono and KRE

Il **K Version Manager**—abbreviato KVM—é un tool che consente di installare diverse versioni del **runtime ASP.NET vNext** nonché di scegliere quale usare. Per installare KVM—e Mono, eseguire il comando `brew tap aspnet/k`.

Quest'operazione eseguirá il *tap*—la referenziazione—dei repo di ASP.NET vNext, eseguire poi `brew install kvm` per la vera installazione dell pacchetto KVM; implicitamente installerá anche l'ultima versione del K Runtime Environment—o KRE.

## OmniSharp e Kulture

Un prerequisito per questo step é <a href="https://sublime.wbond.net/installation" target="_blank" title="Installazione Package Control">l'installazione del Package Control</a>, si prega di fare riferimento al link per i dettagli. Installare i due seguenti pacchetti:

**Kulture**, abilita il sistema di *build* di ASP.NET vNext in Sublime Text. Per installarlo, selezionare `CTRL+SHIFT+P` da Sublime, quindi digitare `Install Package`, poi `Kulture`, infine selezionarlo e premere `Invio`:

**OmniSharp** é la piattaforma che abilita allo sviluppo *C# cross-platform* per l'IDE che abbiamo scelto. OmniSharp collega in Mac OS X tutte le "tubature" necessarie all'IDE per funzionare in modo appropriato con .NET.

Omnisharp supporta *Mac OS X*, *Linux* e *Windows*. Omnisharp apporta inoltre funzionalitá interessanti come l'*auto-complete*, l'*evidenziazione di errori semantici/sintattici*, il *build/rebuild/clean della soluzione*, etc..

Per installare, seguire la medesima precedura ma digitare `OmniSharp` come nome del pacchetto:

## Hello World

Per verificare il successo dell'operazione:

1.  Clonare il repo <a href="https://github.com/aspnet/Home" target="_blank" title="ASP.NET vNext">Home</a>: `git clone https://github.com/aspnet/Home`
2.  Navigare la cartella `/samples/HelloWeb/`
3.  Eseguire `kpm restore` per il ripristino delle dipendenze—potrebbe richiedere un pó
4.  Eseguire `k kestrel`, aka il *web server* Mono
5.  Aprire il broweser all'indirizzo `http://localhost:5004`

E questo é quanto!

<embed src="../andrea-hugo-starter/static/5c2915260a1b98af29944694257d137cd3803b03.shtml" title="ASP.NET vNext HelloWeb" class="image-center" />

## Riferimenti

- Pagina ufficiale <a href="http://www.omnisharp.net/" target="_blank" title="Sito ufficiale OmniSharp">OmniSharp</a>
- Pagina GitHub "<a href="https://github.com/aspnet/home#getting-started" target="_blank" title="Quickstart ASP.NET vNext">Getting Started</a> on ASP.NET"

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Eseguire%20ASP.NET%20vNext%20su%20Mac%20OS%20con%20Kulture%20e%20Omnisharp&amp;url=http%3a%2f%2fandreaazzola.com%2fit%2faspnet-vnext-mac-os-omnisharp-kulture%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="https://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fit%2faspnet-vnext-mac-os-omnisharp-kulture%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

Author's portrait

<a href="https://twitter.com/AndreaAzzola" rel="me" target="_blank" data-text="Twitter" title="Stay up to date with my tweets">My Twitter profile</a><a href="https://www.linkedin.com/in/andreaazzola" rel="me" target="_blank" data-text="LinkedIn" title="Find me on LinkedIn">My LinkedIn profile</a><a href="https://www.facebook.com/andrea.azzola" rel="me" target="_blank" data-text="Facebook" title="Get in touch with Facebook">My Facebook profile</a><a href="http://www.pinterest.com/andreaazzola" rel="me" target="_blank" data-text="Pinterest" title="I&#39;m on Pinterest!">My Pinterest profile</a><a href="https://instagram.com/andrea.azzola" rel="me" target="_blank" data-text="Instagram" title="My Instagram profile">My Instagram profile</a>

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