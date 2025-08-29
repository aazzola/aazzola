---
title: "Search Email Inbox with C#"
type: post
draft: false
date: 2014-03-27T00:00:00
categories: ["Programming", "C#", "Email"]
tags: ["IMAP", "AE.NET.Mail", "Gmail", "Regex", "WebClient", "ASP.NET"]
---

> **Note (2025):** This post dates back to 2014 and uses password‑based IMAP access for Gmail. Modern Gmail/Google Workspace typically requires **OAuth 2.0** and app passwords/“less secure apps” are disabled. The example is kept for archival purposes; adapt authentication accordingly in new projects.

A few years ago I helped manage a <a href="https://magmaglobalgroove.com" target="_blank" rel="noopener" title="Visit MaGmA Global Radio">radio</a> and I needed a tool—an *ASP.NET* web page—for the periodical download of promo mixes. They were linked in emails recognizable by a few keywords.

The following is the stripped‑down **C# snippet** from the tool; it demonstrates how to perform both *search inside the email's subject and body* and the download, using the <a href="https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol" target="_blank" rel="noopener" title="IMAP on Wikipedia">IMAP</a> protocol:

```csharp
using (ImapClient ic = new ImapClient(
    "imap.gmail.com",
    "gmail@gmail.com",
    "mypassword",
    ImapClient.AuthMethods.Login,
    993,
    true))
{
    ic.SelectMailbox("INBOX");
    MailMessage[] mm = ic.GetMessages(0, 100, false); // latest 100 messages

    foreach (MailMessage m in mm)
    {
        if (m.From.Address == "foo@bar.com" || m.Body.ToLower().Contains("episode"))
        {
            Regex regx = new Regex(
                @"(http|https)://([\w+?\.\w+])+([a-zA-Z0-9\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\'\,]*)?",
                RegexOptions.IgnoreCase);
            MatchCollection matches = regx.Matches(m.Body);

            Response.ClearContent();
            Response.ContentType = "audio/mpeg3";
            Response.AddHeader("Content-Disposition", "attachment; filename=Episode.mp3");

            using (WebClient wc = new WebClient())
            {
                Response.BinaryWrite(wc.DownloadData(matches[0].Value));
            }

            Response.End();
        }
    }
}
```

The script was based on the **AE.NET.Mail** library, which <a href="http://andy.edinborough.org/" target="_blank" rel="noopener" title="Andy Edinborough's website">Andy Edinborough</a> made free to use and is available on <a href="https://github.com/andyedinborough/aenetmail" target="_blank" rel="noopener" title="C# POP/IMAP Mail Client on GitHub">GitHub</a>.