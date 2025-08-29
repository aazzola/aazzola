---
title: "Get Size of Tables with SQL Server"
type: post
draft: false
date: 2013-10-16T00:00:00
categories: ["Programming", "SQL Server", "Database"]
tags: ["T-SQL", "DMVs", "sys.dm_db_partition_stats", "space usage"]
---

A snippet for getting the size for all tables in a **SQL Server** database that might prove useful to:

- understand where most of your data is going
- find database bottlenecks
- free up disk space
- reduce maintenance cost

```sql
WITH table_space_usage (schema_name, table_name, used, reserved, ind_rows, tbl_rows) AS (
  SELECT
    s.name,
    o.name,
    p.used_page_count * 8,      -- KB
    p.reserved_page_count * 8,  -- KB
    p.row_count,
    CASE WHEN i.index_id IN (0,1) THEN p.row_count ELSE 0 END
  FROM sys.dm_db_partition_stats AS p
  INNER JOIN sys.objects  AS o ON o.object_id = p.object_id
  INNER JOIN sys.schemas  AS s ON s.schema_id = o.schema_id
  LEFT  OUTER JOIN sys.indexes AS i ON i.object_id = p.object_id AND i.index_id = p.index_id
  WHERE o.type_desc = 'USER_TABLE' AND o.is_ms_shipped = 0
)
SELECT
  t.schema_name,
  t.table_name,
  SUM(t.used)     AS used_in_kb,
  SUM(t.reserved) AS reserved_in_kb,
  SUM(t.tbl_rows) AS rows
FROM table_space_usage AS t
GROUP BY t.schema_name, t.table_name
ORDER BY used_in_kb DESC;
```