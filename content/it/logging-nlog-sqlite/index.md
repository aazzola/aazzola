---
title: "Logging con NLog e SQLite"
type: post
draft: false
date: 2014-05-06T00:00:00
categories: ["Programmazione", ".NET", "Logging"]
tags: ["NLog", "SQLite", "logging", "configurazione", "C#"]
---

Questo articolo spiega come ottenere una soluzione di logging portabile ed elegante grazie all'uso di **NLog** e **SQLite**, su piattaforma .NET e con poche configurazioni.

## NLog

[NLog](http://nlog-project.org/) è una libreria di logging leggera e gratuita che supporta l'ecosistema .NET (Silverlight, Windows Phone, ecc.). Costituisce un'opzione eccellente per un ampio range di scenari: dalle semplici utilities quotidiane a servizi critici di produzione. Consente di avere multipli target, siano essi file, database, console, rete o email.

**Installazione**

Package Manager:

```powershell
PM> Install-Package NLog
```

## SQLite

[SQLite](http://www.sqlite.org/) è un *motore di database* semplice e leggero, molto diffuso soprattutto in ambito mobile. Non richiede alcun demone server né configurazioni particolari. Il database è un singolo file (estensione `.db3`), mentre lettura e scrittura vengono gestite da librerie specifiche per piattaforma, generalmente open source.

**Setup**

L'interfaccia .NET più comune è *System.Data.SQLite*.

Package Manager Console:

```powershell
PM> Install-Package System.Data.SQLite
```

## File di configurazione NLog

È opzionale ma consigliato usare un file separato per le configurazioni di NLog. In questo modo, eventuali errori nel logging non compromettono l’intera applicazione (*separation of concerns*).

**Installazione**

```powershell
PM> Install-Package NLog.Config
```

## Eseguire NLog e SQLite insieme

1. **Predisponi il database SQLite**: usa il [SQLite Database Browser](http://sourceforge.net/projects/sqlitebrowser/) o un altro client a scelta per creare il database, quindi esegui lo statement SQL seguente per creare la tabella dei log:

   ```sql
   CREATE TABLE Log (
     Timestamp TEXT,
     Loglevel TEXT,
     Logger TEXT,
     Callsite TEXT,
     Message TEXT
   )
   ```

2. **Configura NLog per scrivere sul database**:

   ```xml
   <?xml version="1.0" encoding="utf-8" ?>
   <nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         throwExceptions="false">
     <targets>
       <target name="db" xsi:type="Database"
               dbProvider="System.Data.SQLite" keepConnection="false"
               connectionString="Data Source=${basedir}\Log.db3;Version=3;"
               commandText="INSERT INTO Log(Timestamp, Loglevel, Logger, Callsite, Message)
                            VALUES(@Timestamp, @Loglevel, @Logger, @Callsite, @Message)">
       </target>
     </targets>
     <rules>
       <logger name="*" minlevel="Warn" writeTo="db" />
     </rules>
   </nlog>
   ```

3. **Avvia il logging in C#**:

   ```csharp
   class Program {
     static Logger log = LogManager.GetCurrentClassLogger();

     static void Main(string[] args) {
         log.Info("Logging like a boss");
     }
   }
   ```

## Conclusione

Puoi trovare il codice sorgente e un progetto di esempio qui: [https://github.com/aazzola/nlog-sqlite/](https://github.com/aazzola/nlog-sqlite/){:target="_blank"}

> **Nota (2025):** Per le versioni più recenti dei pacchetti e di Visual Studio (dalla 2013 Update 3 in avanti), è necessario aggiungere `commandType="Text"` nel tag `target`, altrimenti si ottiene un errore *method not supported*.