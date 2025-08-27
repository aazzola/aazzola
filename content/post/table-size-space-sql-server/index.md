---
title: "Get Size of Tables with SQL Server"
type: post
draft: false
date: 2013-10-16T00:00:00
---
# Get Size of Tables with SQL Server

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2013-10-16 11:07
\[<a href="index.html" target="_self" title="Permalink to Get Size of Tables with SQL Server">Permalink</a>\]

A snippet for getting the size for all tables in a *SQL Server* database that might prove useful for:

- Get a better understanding where most of your data is going
- Find database bottlenecks
- Free up disk space
- Reducing maintenance cost

    WITH table_space_usage (schema_name, table_name, used, reserved, ind_rows, tbl_rows)
    AS (SELECT s.Name, o.Name, p.used_page_count * 8, p.reserved_page_count * 8, p.row_count,
      CASE WHEN i.index_id in ( 0, 1 ) THEN p.row_count ELSE 0 END
      FROM sys.dm_db_partition_stats p
      INNER JOIN sys.objects as o ON o.object_id = p.object_id
      INNER JOIN sys.schemas as s ON s.schema_id = o.schema_id
      LEFT OUTER JOIN sys.indexes as i on i.object_id = p.object_id
        and i.index_id = p.index_id
      WHERE o.type_desc = 'USER_TABLE' and o.is_ms_shipped = 0
    )

    SELECT t.schema_name, t.table_name, sum(t.used) as used_in_kb,
      sum(t.reserved) as reserved_in_kb, sum(t.tbl_rows) as rows
    FROM table_space_usage as t
    GROUP BY t.schema_name , t.table_name
    ORDER BY used_in_kb desc

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Get%20Size%20of%20Tables%20with%20SQL%20Server&amp;url=http%3a%2f%2fandreaazzola.com%2ftable-size-space-sql-server%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2ftable-size-space-sql-server%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

Author's portrait

<a href="http://twitter.com/AndreaAzzola" rel="me" target="_blank" data-text="Twitter" title="Stay up to date with my tweets">My Twitter profile</a><a href="http://www.linkedin.com/in/andreaazzola" rel="me" target="_blank" data-text="LinkedIn" title="Find me on LinkedIn">My LinkedIn profile</a><a href="http://www.facebook.com/andrea.azzola" rel="me" target="_blank" data-text="Facebook" title="Get in touch with Facebook">My Facebook profile</a><a href="http://www.pinterest.com/andreaazzola" rel="me" target="_blank" data-text="Pinterest" title="I&#39;m on Pinterest!">My Pinterest profile</a><a href="http://instagram.com/andrea.azzola" rel="me" target="_blank" data-text="Instagram" title="My Instagram profile">My Instagram profile</a>

- <a href="../about/index.html" style="font-weight:bold" data-text="About" title="Short summary">About</a>
- <a href="../articles/index.html" style="font-weight:bold" data-text="Articles" title="Collection of all articles in this website">Articles</a>
- <a href="../books/index.html" style="font-weight:bold" data-text="Books" title="My book recommendations">Books</a>
- <a href="../contact/index.html" style="font-weight:bold" data-text="Contact" title="Short summary">Contact</a>
- <a href="../feed/index.html" data-text="RSS feed" title="Subscribe to this blog">RSS feed</a>
- <a href="../login/index.html" data-text="Login" title="Login">Login</a>

- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageEN%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageEN" class="lang-sm lang-lbl" lang="en"></a>
- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageIT%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageIT" class="lang-sm lang-lbl" lang="it"></a>

#### Newsletter

 
 

<a href="../category/books/index.html" class="category" style="font-size:112%;">Books</a>
<a href="../category/decision-fatigue/index.html" class="category" style="font-size:112%;">Decision Fatigue</a>
<a href="../category/diet/index.html" class="category" style="font-size:112%;">Diet</a>
<a href="../category/extreme-saving/index.html" class="category" style="font-size:119%;">Extreme Saving</a>
<a href="../category/finance/index.html" class="category" style="font-size:112%;">Finance</a>
<a href="../category/financial-independence/index.html" class="category" style="font-size:125%;">Financial Independence</a>
<a href="../category/fitness/index.html" class="category" style="font-size:119%;">Fitness</a>
<a href="../category/gears/index.html" class="category" style="font-size:112%;">Gears</a>
<a href="../category/geo-arbitrage/index.html" class="category" style="font-size:112%;">Geo Arbitrage</a>
<a href="../category/goal-setting/index.html" class="category" style="font-size:112%;">Goal Setting</a>
<a href="../category/nutrition/index.html" class="category" style="font-size:112%;">Nutrition</a>
<a href="../category/personal-branding/index.html" class="category" style="font-size:112%;">Personal Branding</a>
<a href="../category/personal-development/index.html" class="category" style="font-size:150%;">Personal Development</a>
<a href="../category/productivity/index.html" class="category" style="font-size:125%;">Productivity</a>
<a href="../category/time-management/index.html" class="category" style="font-size:106%;">Time Management</a>