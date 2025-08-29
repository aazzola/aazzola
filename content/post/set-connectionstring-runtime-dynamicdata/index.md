---
title: "Set the ConnectionString at Runtime with DynamicData"
type: post
draft: false
date: 2008-06-16T00:00:00
categories: ["Programming", "ASP.NET", "Dynamic Data"]
tags: ["ConnectionString", "Dynamic Data", "Global.asax", "RegisterRoutes", "ContextConfiguration"]
---

> **Note (2025):** This article dates back to 2008 and refers to **ASP.NET Dynamic Data**, which is legacy today. Concepts can still be useful historically, but for modern .NET consider newer frameworks and data‑binding approaches.

The following snippet customizes the `.NET` **ConnectionString** at runtime in a **Dynamic Data** application.

Edit `Global.asax` and modify the `RegisterRoutes(RouteCollection routes)` method. Instead of:

```csharp
model.RegisterContext(typeof(XYZDataContext), new ContextConfiguration() { ScaffoldAllTables = true });
```

Use:

```csharp
model.RegisterContext(
    () => new XYZDataContext(connectionString),
    new ContextConfiguration { ScaffoldAllTables = true }
);
```

Where `connectionString` is your string value. You can customize the `RegisterRoutes` parameter collection without compromising application functionality.