---
title: "Handle Multiple Columns as One with Dynamic Data"
type: post
draft: false
date: 2008-11-02T00:00:00
categories: ["Programming", "ASP.NET", "Dynamic Data"]
tags: ["ASP.NET", "Dynamic Data", "FieldTemplateUserControl", "UIHint", "MetaColumn"]
---

Sometimes you need to schedule tasks in **ASP.NET** and save both a *Start Date* and an *Interval*, stored respectively as <a href="https://learn.microsoft.com/en-us/dotnet/api/system.datetime" target="_blank" rel="noopener">DateTime</a> and <a href="https://learn.microsoft.com/en-us/dotnet/api/system.timespan.ticks" target="_blank" rel="noopener">TimeSpan.Ticks</a> in your database.

Editing raw tick values is not exactly good UX, so I bound the proper <a href="https://learn.microsoft.com/en-us/dotnet/api/system.web.dynamicdata.metacolumn.uihint" target="_blank" rel="noopener">MetaColumn</a> to the proper <a href="https://learn.microsoft.com/en-us/dotnet/api/system.web.dynamicdata.fieldtemplateusercontrol" target="_blank" rel="noopener">UIHint</a>. After some tests, I noticed the GUI was functional but not as intuitive as expected.

The solution was to customize the <a href="https://learn.microsoft.com/en-us/dotnet/api/system.web.dynamicdata.fieldtemplateusercontrol" target="_blank" rel="noopener">FieldTemplateUserControl</a> of Dynamic Data, to display and save multiple columns I needed (Start Date, Start Time, Occurs – Daily, Weekly, Monthly, etc.).

## How to retrieve values (Schedule_EditField.ascx.cs)

```csharp
protected override void OnDataBinding(EventArgs e)
{
    base.OnDataBinding(e);
    DateTime? startFrom = (DateTime?)Eval("StartFrom");
    long? timeIntervalTicks = (long?)Eval("TimeInterval");
    DateTime? lastExecution = (DateTime?)Eval("LastExecution");
}
```

## How to store values

```csharp
protected override void ExtractValues(IOrderedDictionary dictionary)
{
    dictionary["StartFrom"] = …; // logic here
    dictionary["TimeInterval"] = …;  // logic here
}
```

> **Note (2025):** This article dates back to 2008 and refers to ASP.NET Dynamic Data, a framework that is no longer mainstream. Concepts may still be useful historically, but for modern .NET development you should look at more recent frameworks (e.g. ASP.NET MVC, Blazor, or modern data‑binding approaches).