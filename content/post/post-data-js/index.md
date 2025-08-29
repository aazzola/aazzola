---
title: "POST data with JavaScript"
type: post
draft: false
date: 2009-07-07T00:00:00
categories: ["Programming", "JavaScript", "Web"]
tags: ["POST", "forms", "AJAX", "jQuery"]
---

> **Note (2025):** This article dates back to 2009. The examples remain useful, though modern apps often prefer `fetch()`/XHR or form submissions driven by frameworks. The classic form‑build approach below still works universally.

**HTML 4.0** (W3C) defines how browsers submit forms:

- **GET**: append query string to the action URL (`application/x-www-form-urlencoded`).
- **POST**: send a request body to the action URL, using the content type indicated by `enctype`.

## Programmatic POST helper

Add this in your page head:

```html
<script>
function post(dictionary, url, method) {
  method = (method || "post").toLowerCase();
  var form = document.createElement("form");
  form.setAttribute("method", method);
  form.setAttribute("action", url);
  for (var key in dictionary) {
    if (!Object.prototype.hasOwnProperty.call(dictionary, key)) continue;
    var hidden = document.createElement("input");
    hidden.type = "hidden";
    hidden.name = key;
    hidden.value = dictionary[key];
    form.appendChild(hidden);
  }
  document.body.appendChild(form);
  form.submit();
}
</script>
```

Usage in the body:

```html
<script>
  var myDictionary = {};
  myDictionary["1stKey"] = "1stValue";
  myDictionary["2ndKey"] = "2ndValue";
</script>

<input type="button" value="Click me to POST"
       onclick="post(myDictionary, 'destination.html');" />
<input type="button" value="Click me to GET"
       onclick="post(myDictionary, 'destination.html', 'get');" />
```

The helper accepts a key/value dictionary, a destination URL, and an optional method (`post` or `get`).

## jQuery.post alternative

If you already use jQuery, you can leverage its shorthand:

```js
jQuery.post(url, data, success, dataType);
// or
$.ajax({ type: "POST", url, data, success, dataType });

$.post("test.php", { "1stKey": "1stValue", "2ndKey": "2ndValue" });
```

Further details: <a href="https://api.jquery.com/jQuery.post/" target="_blank" rel="noopener">jQuery.post()</a>