---
title: "MavensMate unable to reach GitHub on Windows"
type: post
draft: false
date: 2014-04-06T00:00:00
categories: ["Programming", "Salesforce", "Windows"]
tags: ["MavensMate", "Sublime Text", "Git", "Proxy", "Firewall"]
---

<p align="center"><img src="/images/resource-91ae0ec9-5a5f-4046-882e-0724d7875675.png" loading="lazy" alt=""></p>
<a href="http://mavensmate.com/" target="_blank" rel="noopener">MavensMate</a> was a popular community plugin for the **Force.com** platform, built on the <a href="http://www.sublimetext.com/" target="_blank" rel="noopener">Sublime Text</a> IDE (created and maintained by <a href="http://www.joe-ferraro.com/" target="_blank" rel="noopener">Joe Ferraro</a>) as a free alternative to the official Force.com IDE.

Under certain conditions on Windows 7/8 (often proxy/firewall configurations), installation could fail with an error similar to:

```
Installation of Sublime Text plugin failed. This is likely due to the installer being unable to reach GitHub. If you are behind a firewall or using a proxy, you should configure git accordingly (google: git config --global https.proxy) and ensure your HTTPS/HTTPS_PROXY environment variable(s) are set properly. Otherwise, please log an issue on the MavensMate GitHub project.
```

There is an existing GitHub <a href="https://github.com/joeferraro/MavensMate/issues/113" target="_blank" rel="noopener">issue</a> with a workaround suggested by Joe Ferraro. The steps that worked for me were:

1. Open **Command Prompt** and move to the Sublime Text *Packages* directory (adjust `username` if needed):

```bat
cd "C:\Users\username\AppData\Roaming\Sublime Text 3\Packages"
```

2. Clone the plugin and initialize submodules manually:

```bat
git clone --recursive http://github.com/joeferraro/MavensMate-SublimeText.git MavensMate
cd MavensMate
git submodule init
git submodule update
```

After restarting **Sublime Text**, the plugin should be available. Remember to configure your workspace via **MavensMate → Settings**.