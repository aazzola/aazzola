---
title: "Check the MetaModel Existence while Running a Dynamic Data Application"
type: post
draft: false
date: 2008-06-18T00:00:00
categories: ["Programming", "ASP.NET"]
---

In the web application that I'm developing using Dynamic Data, I set the DataContext at runtime. The application might bind different contexts depending on many variables. I usually test it on two different browsers, and, because of the session, I need to pass the same procedure twice. The second time, the DataContext is already set, so I don't need to register the context anymore. The simple condition I use:

```cs
if (System.Web.DynamicData.MetaModel.Default == null)
{
    // Register context and routes
    ...
}
```

Otherwise I would get this exception:

```
[ArgumentException: L'elemento è già stato aggiunto. 
Chiave nel dizionario: 'MyAppDataContext'. 
Chiave aggiunta: 'MyAppDataContext']
```

Meaning: *The item is already present. Key in dictionary 'MyAppDataContext', Key added 'MyAppDataContext'.*
```