---
title: "Eseguire ASP.NET vNext su Mac OS con Kulture e Omnisharp"
type: post
draft: false
date: 2014-12-20T00:00:00
categories: ["Programming", "ASP.NET", "MacOS"]
tags: ["ASP.NET vNext", "Kulture", "OmniSharp", "Homebrew", "Sublime Text"]
---

<p align="center"><img src="/images/aspnet_sublime_pkgmng_kulture-1.png" loading="lazy" alt=""></p>
<p align="center"><img src="/images/aspnet_sublime_pkgmng_omnisharp-1.png" loading="lazy" alt=""></p>
L'articolo descrive **come eseguire ASP.NET vNext** con sistema operativo *Mac OS X*. La procedura richiede alcuni passaggi e un po’ di pazienza. Fortunatamente OS X include già il prerequisito *Ruby*: versione 2.0 su Mavericks/Yosemite, 1.8.7 su Mountain Lion, Lion e Snow Leopard.

## Sublime Text

Un *text editor avanzato* molto diffuso per Mac OS X è **[Sublime Text](http://www.sublimetext.com/){:target="_blank"}**. Personalmente lo uso anche in Windows per sviluppare soluzioni [Salesforce.com](https://andreaazzola.com/category/salesforcecom){:target="_blank"} o per prendere note e redigere articoli in HTML. Altri editor supportati all’epoca della scrittura erano:

- [Atom](https://atom.io/){:target="_blank"}
- [Emacs](http://www.gnu.org/software/emacs/){:target="_blank"}
- [Brackets](https://brackets.io/){:target="_blank"}
- [Vim](http://www.vim.org/){:target="_blank"}

## Homebrew

[Homebrew](https://brew.sh/){:target="_blank"} è un *package manager* open source per Mac OS X. Per funzionare necessita di *git* e *ruby*. Per verificarne l'installazione aprire il terminale e lanciare `brew doctor`. Se l’esito è `command not found`, significa che brew non è installato. Si può provvedere con il comando:

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## KVM, Mono e KRE

Il **K Version Manager (KVM)** è un tool che consente di installare diverse versioni del **runtime ASP.NET vNext** e scegliere quale usare. Per installare KVM (e Mono), eseguire:

```bash
brew tap aspnet/k
brew install kvm
```

Questo installerà anche l'ultima versione del **K Runtime Environment (KRE)**.

## OmniSharp e Kulture

Un prerequisito è l’[installazione del Package Control](https://sublime.wbond.net/installation){:target="_blank"}. Una volta attivo, installare i due pacchetti:

- **Kulture**, che abilita il sistema di *build* ASP.NET vNext in Sublime Text. Da Sublime: `CTRL+SHIFT+P` → `Install Package` → cercare `Kulture` → Invio.
- **OmniSharp**, piattaforma che abilita lo sviluppo *C# cross‑platform* negli IDE. Offre funzionalità come *auto-complete*, evidenziazione di errori semantici/sintattici, *build/rebuild/clean* della soluzione.

OmniSharp supporta Mac OS X, Linux e Windows.

## Hello World

Per verificare il successo dell'operazione:

1. Clonare il repo [Home](https://github.com/aspnet/Home){:target="_blank"}:  
   ```bash
   git clone https://github.com/aspnet/Home
   ```
2. Navigare nella cartella `/samples/HelloWeb/`
3. Eseguire `kpm restore` per ripristinare le dipendenze
4. Avviare il server: `k kestrel`
5. Aprire il browser su `http://localhost:5004`

## Riferimenti

- [OmniSharp – sito ufficiale](http://www.omnisharp.net/){:target="_blank"}
- [Getting Started on ASP.NET (GitHub)](https://github.com/aspnet/home#getting-started){:target="_blank"}

> **Nota (2025):** Questa guida si riferisce a strumenti ora obsoleti (ASP.NET vNext e KVM). Le informazioni hanno valore storico.