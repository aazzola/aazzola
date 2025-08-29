---
title: "Using an ajax:ModalPopup Without a TargetControl"
type: post
draft: false
date: 2007-09-25T00:00:00
categories: ["ASP.NET", "AJAX"]
tags: ["ModalPopupExtender", "TargetControlID", "C#", "ASP.NET"]
---

The **ModalPopup** extender usually requires a control for firing up, set through the *TargetControlID* property. However, sometimes you may want to show and hide the panel programmatically. All you need is a fake activator, like the following:

## The Extender

```xml
<ajax:ModalPopupExtender ID="mpeInfo" runat="server" TargetControlID="divFakeActivator"
    PopupControlID="pnlInfo" CancelControlID="bttInfoClose" />
```

## The Panel

```xml
<asp:Panel ID="pnlInfo" runat="server">
    Hello World!!!
</asp:Panel>
```

## The C# code

```csharp
// Show and hide programmatically
mpeInfo.Show();
mpeInfo.Hide();
```

> **Note (2025):** This post reflects an older ASP.NET AJAX pattern. In modern frameworks you would likely manage modal dialogs through client‑side libraries (e.g., Bootstrap, React, Blazor components).