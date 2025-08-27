---
title: "Call async methods with C#"
type: post
draft: false
date: 2009-10-15T00:00:00
categories: ["Programming", "C#"]
---

*Note: This article was originally written in 2009 and may be obsolete due to C# technology improvements.*

This article shows how to delegate work to an asynchronous thread in C#, allowing for code execution and app responsiveness. You might go a step further by implementing error notifications, polling, or waiting for the procedure to complete at a certain point.

Suppose you have the following method:

```cs
public void UploadFile(string path)
{
    try
    {
        //... uploads some file to the server
    }
    catch(Exception ex)
    {
        // ... handle errors
    }
}
```

And you are implementing it as a web service: you are asked to give an immediate response and upload the file *asynchronously*, as the user won't need the upload immediately.

### Declare a method delegate

```cs
public delegate void UploadFileDelegate(string path);
```

### Invoke it asynchronously

```cs
[WebMethod]
public bool GetFile(string path)
{
    try
    {
        UploadFileDelegate uid = UploadFile;
        IAsyncResult rsl = uid.BeginInvoke(path, null, null);
        return true;
    }
    catch(Exception ex)
    {
        return false;
    }
}
```

The *BeginInvoke* method starts the thread but allows the code to continue executing without waiting for an immediate return.