---
title: "How to run ASP.NET vNext on Mac OS with Kulture and OmniSharp"
type: post
draft: false
date: 2014-12-20T00:00:00
---

*Note: This article was originally written in 2014. ASP.NET vNext and KVM/KRE were early projects that later evolved into .NET Core and the modern .NET SDK. Instructions are kept for historical purposes.*

The article will describe **how to run ASP.NET vNext** on **Mac OS X**. The process, requires multiple configurations and therefore some patience. Luckily, OS X already includes one of the pre-requirements, **Ruby**, 2.0 on Mavericks and Yosemite, 1.8.7 on Mountain Lion, Lion, and Snow Leopard.

## Sublime Text

One very popular IDE or *advanced text editor* for Mac OS X is **[Sublime Text](http://www.sublimetext.com/)**. I use it on both OS X and Windows, for developing [Salesforce.com](http://andreaazzola.com/category/salesforcecom) applications, to take notes or authoring this very article in pure HTML, and I'm very happy with it. Other supported IDEs—at the moment of writing—are:

- Atom - <https://atom.io/>
- Emacs - <http://www.gnu.org/software/emacs/>
- Brackets - <http://brackets.io/>
- Vim - <http://www.vim.org/>

## Homebrew

[Homebrew](http://brew.sh/) is an open source package manager for Mac OS X, it leverages mostly on *git* and *ruby*. If you're not sure to have it installed, just open the *Terminal* and issue the command `brew doctor`. If the response is `command not found` well, it's not installed, so run the following command: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` (Current Homebrew installation uses `bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)

## KVM, Mono and KRE

The **K Version Manager**—KVM—is a tool for installing different versions of the **ASP.NET vNext runtime** and switch between them. To install the KVM and Mono, run the command `brew tap aspnet/k`, this will only *tap*—reference—ASP.NET vNext repos, therefore launch `brew install kvm` to install the KVM package. This, will also install the latest K Runtime Environment—KRE.

## OmniSharp and Kulture

A prerequisite for this step is the [setup of Package Control](https://sublime.wbond.net/installation), please refer to the link for more details. Then, proceed to install the two following packages:

**Kulture**, is a Sublime Text package for ASP.NET vNext that brings the build system into the Sublime. To install it, press `CTRL+SHIFT+P`, then type `Install Package`, then `Kulture`, select it and press `Return`.

**OmniSharp** is a platform for enabling *C# cross-platform .NET development* for the IDE of your choice. In other words, *OmniSharp* plugs all the plumbing needed by the “Mac OS X based” IDE to behave like a proper .NET IDE. It supports both *Mac OS X*, *Linux* and *Windows*, and brings very useful features like *Auto Completion*, *Syntax/Semantic error highlighting*, *Build/ReBuild/Clean solution*, etc.

To install, follow the same procedure but type `OmniSharp` for the package name this time.

## Hello World

Let's check out the new setup:

1. Clone the [Home](https://github.com/aspnet/Home) repository: `git clone https://github.com/aspnet/Home`
2. Browse the `/samples/HelloWeb/` folder
3. Run `kpm restore` to restore dependencies, this may take a while
4. Run `k kestrel`, aka the Mono *web server*
5. Navigate you app at `http://localhost:5004`

And that should be it!

## References

- [OmniSharp](http://www.omnisharp.net/) official page
- [Getting Started](https://github.com/aspnet/home#getting-started) on ASP.NET GitHub page