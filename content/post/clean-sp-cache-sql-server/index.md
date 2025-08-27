---
title: "Clean Up Stored Procedures Cache with SQL Server"
type: post
draft: false
date: 2009-03-06T00:00:00
categories: ["Programming", "SQL Server"]
---

When deploying a stored procedure, cleaning up the database's cache can help apply changes immediately. Have a look at the following code:

```sql
-- Cleans up db's cache
DECLARE @dbID INTEGER
SET @dbID = (SELECT dbid FROM master.dbo.sysdatabases WHERE name = 'DBNameHere')
DBCC FLUSHPROCINDB (@dbID)
```

The [DBCC FLUSHPROCINDB](http://msdn.microsoft.com/en-us/library/cc297250.aspx) command allows specifying a particular database id, and then clears all the plans from it.