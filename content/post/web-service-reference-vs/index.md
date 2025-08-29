---
title: "Import Web Service References in .NET"
type: post
draft: false
date: 2010-06-09T00:00:00
categories: ["Programming", ".NET", "Web Services"]
tags: ["wsdl.exe", "Visual Studio", "proxy classes", "WSDL", "SDK"]
---

> **Note (2025):** This post refers to .NET Framework 2.0 era tools such as **wsdl.exe**. Modern .NET projects generally use `Connected Services` in Visual Studio or `dotnet svcutil`. The example is preserved for historical reference.

You may need to consume <a href="https://en.wikipedia.org/wiki/Web_service" target="_blank" rel="noopener">Web services</a> from client applications. <a href="https://visualstudio.microsoft.com/" target="_blank" rel="noopener">Visual Studio</a> provides tools for generating proxy classes, which in some cases may be insufficient. In those cases, the `wsdl.exe` tool is an alternative.

## The wsdl.exe tool

You can use the <a href="https://en.wikipedia.org/wiki/Cmd" target="_blank" rel="noopener">command prompt</a> tool **wsdl.exe**, included within the <a href="https://www.microsoft.com/en-us/download/details.aspx?id=19988" target="_blank" rel="noopener" title="NET Framework 2.0 SDK">.NET Framework 2.0 SDK</a>. This tool accepts the path to a <a href="https://en.wikipedia.org/wiki/Web_Services_Description_Language" target="_blank" rel="noopener">WSDL</a> file and generates the proxy class automatically.

## Example

```bat
"C:\Program Files\Microsoft SDKs\Windows\v6.0A\bin\wsdl.exe" ^
  "C:\ServiceTest.wsdl" /n:MyNameSpace.MyServices /o:"C:\ServiceTest.cs" /l:CS
```

In this example:

- The path of the WSDL is specified
- `/n` sets the target namespace of the proxy class
- `/o` specifies the output file path
- `/l` sets the target language (here: C#)

A complete list of options is available in the [official MSDN documentation](https://msdn.microsoft.com/en-gb/library/7h3ystb6%28v=VS.80%29.aspx).

⚠️ If you generate multiple files related to classes in the same namespace, remember that some objects may be declared multiple times; these duplicates must be removed manually.

## Related articles

- [Testing a Web service with a proxy class](http://articles.techrepublic.com.com/5100-10878_11-5755966.html){:target="_blank" rel="noopener"}