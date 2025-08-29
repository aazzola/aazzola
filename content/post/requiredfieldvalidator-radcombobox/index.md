---
title: "Simulating a RequiredFieldValidator with RadComboBox"
type: post
draft: false
date: 2010-10-22T00:00:00
categories: ["Programming", "ASP.NET", "Telerik"]
tags: ["RadComboBox", "ASP.NET", "CustomValidator", "Validation"]
---

Telerik’s <a href="http://www.telerik.com/products/aspnet-ajax/combobox.aspx" target="_blank" rel="noopener">RadComboBox</a> does not behave like a traditional <a href="https://learn.microsoft.com/en-us/dotnet/api/system.web.ui.webcontrols.dropdownlist" target="_blank" rel="noopener">DropDownList</a>. Instead of a **RequiredFieldValidator**, you should use a <a href="https://learn.microsoft.com/en-us/dotnet/api/system.web.ui.webcontrols.customvalidator" target="_blank" rel="noopener">CustomValidator</a>. Here’s an implementation.

## Step 1: Markup

```aspx
<asp:Label ID="lblExample" runat="server" AssociatedControlID="rcbExample"
    Text="Example" />
<telerik:RadComboBox ID="rcbExample" runat="server" />
<asp:CustomValidator ID="cvlExample" runat="server" ControlToValidate="rcbExample"
    Text="*" ClientValidationFunction="cvlExampleValidate"
    OnServerValidate="cvlExample_ServerValidate" />
```

## Step 2: Client-side validation

```js
function cvlExampleValidate(source, args) {
    args.IsValid = radComboValidate("<%= rcbExample.ClientID %>");
}

function radComboValidate(controlName) {
    var combo = $find(controlName);
    var text = combo.get_text();

    if (text.length < 1) return false;
    var node = combo.findItemByText(text);
    if (node) {
        var value = node.get_value();
        return value.length > 0;
    }
    return false;
}
```

## Step 3: Server-side validation

```csharp
protected void cvlStatus_ServerValidate(object source, ServerValidateEventArgs args)
{
    args.IsValid = rcbStatus.SelectedValue.Length > 0;
}
```

> **Note (2025):** This article is from 2010. Telerik’s RadControls have evolved significantly since then; check the current [Telerik UI for ASP.NET AJAX documentation](https://docs.telerik.com/devtools/aspnet-ajax/) for modern practices.