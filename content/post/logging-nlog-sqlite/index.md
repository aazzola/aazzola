---
title: "Logging with NLog and SQLite"
type: post
draft: false
date: 2014-05-06T00:00:00
categories: ["Programming", ".NET", "Logging"]
tags: ["NLog", "SQLite", "C#", "Logging", "NuGet"]
---

<p align="center"><img src="/images/nlogsqlite_love-1.png" loading="lazy" alt=""></p>
<p align="center"><img src="/images/nlogsqlite_nlog-1.png" loading="lazy" alt=""></p>
<p align="center"><img src="/images/nlogsqlite_sqlite-1.png" loading="lazy" alt=""></p>

This article explains how to achieve a portable and elegant *logging* solution with **NLog** and **SQLite** on the .NET platform with a few configurations.

## NLog

NLog is a free, lightweight logging library for .NET. It supports many targets (files, databases, console, network, email, and more). <a href="https://nlog-project.org/" target="_blank" rel="noopener">nlog-project.org</a>

**Install (NuGet Package Manager Console)**

```powershell
PM> Install-Package NLog
```

## SQLite

<a href="https://www.sqlite.org/" target="_blank" rel="noopener">SQLite</a> is a simple embedded database engine. No separate server daemon is required; the database is a single file (e.g., `.db3`).

**Install (NuGet Package Manager Console)**

```powershell
PM> Install-Package System.Data.SQLite
```

## NLog configuration file

Keeping NLog configuration in a separate file is recommended so a misconfiguration affects only logging and not the whole app.

**Install config scaffold**

```powershell
PM> Install-Package NLog.Config
```

## Get them to work together

1. **Create the SQLite database** (e.g., with <a href="https://sqlitebrowser.org/" target="_blank" rel="noopener">DB Browser for SQLite</a>) and the `Log` table:

```sql
CREATE TABLE Log (
  Timestamp TEXT,
  Loglevel  TEXT,
  Logger    TEXT,
  Callsite  TEXT,
  Message   TEXT
);
```

2. **Point NLog to SQLite** by adding a database target in `NLog.config`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      throwExceptions="false">
  <targets>
    <target name="db" xsi:type="Database"
            dbProvider="System.Data.SQLite"
            keepConnection="false"
            connectionString="Data Source=${basedir}\Log.db3;Version=3;"
            commandText="INSERT INTO Log(Timestamp, Loglevel, Logger, Callsite, Message)
                          VALUES(@Timestamp, @Loglevel, @Logger, @Callsite, @Message)" />
  </targets>
  <rules>
    <logger name="*" minlevel="Warn" writeTo="db" />
  </rules>
</nlog>
```

> If you’re using newer package versions or providers, check the official docs for any changes to `dbProvider` or connection string formats.

3. **Start logging**

```csharp
using NLog;

class Program
{
    private static readonly Logger log = LogManager.GetCurrentClassLogger();

    static void Main(string[] args)
    {
        log.Info("Logging like a boss");
    }
}
```

## Source code

Sample project: <a href="https://github.com/aazzola/nlog-sqlite/" target="_blank" rel="noopener">github.com/aazzola/nlog-sqlite</a>