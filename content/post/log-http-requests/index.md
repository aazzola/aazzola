---
title: "How to Log HTTP Requests with PHP"
type: post
draft: false
date: 2010-05-27T00:00:00
categories: ["Programming", "PHP", "Web"]
tags: ["HTTP", "logging", "PHP", "SOAP", "Salesforce"]
---

> **Note (2025):** This post was written in 2010. The sample uses `ereg`, which has been **deprecated** in PHP 5.3 and removed as of PHP 7. Use `preg_match` or other modern approaches for production code. The article remains here for archival and historical interest.

Sometimes you need to understand **precisely** how the <a href="https://en.wikipedia.org/wiki/Http#Client_request" target="_blank" rel="noopener">HTTP request</a> is submitted to the **server**. If you're working with <a href="https://www.salesforce.com/" target="_blank" rel="noopener">Salesforce.com</a>, you probably don't have easy or intuitive tools to understand how a message is **serialized** and sent by the runtime to the **server**.

I've put together this little script that allows you to log all <a href="https://en.wikipedia.org/wiki/Http#Client_request" target="_blank" rel="noopener">HTTP request</a>s to a file. It becomes much easier to verify the output sent to a <a href="https://en.wikipedia.org/wiki/Web_service" target="_blank" rel="noopener">web service</a>.

```php
<?php
    $myFile = "requestslog.txt";
    $fh = fopen($myFile, 'a') or die("can't open file");
    fwrite($fh, "\n\n--------------------------------------\n");
    foreach($_SERVER as $h => $v) {
        if (preg_match('/^HTTP_(.+)/', $h, $hp)) {
            fwrite($fh, "$h = $v\n");
        }
    }
    fwrite($fh, "\r\n");
    fwrite($fh, file_get_contents('php://input'));
    fclose($fh);
    echo "<html><head /><body><iframe src=\"$myFile\" style=\"height:100%; width:100%;\"></iframe></body></html>";
?>
```

This applies to all requests that travel with the <a href="https://en.wikipedia.org/wiki/Http" target="_blank" rel="noopener">HTTP protocol</a>, even <a href="https://en.wikipedia.org/wiki/SOAP" target="_blank" rel="noopener">SOAP</a>, for instance.