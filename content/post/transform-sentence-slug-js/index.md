---
title: "Turn Sentences into Slugs with JavaScript"
type: post
draft: false
date: 2010-10-20T00:00:00
categories: ["Programming", "JavaScript", "SEO"]
tags: ["slug", "URL", "JavaScript", "jQuery"]
---

This simple script converts a *text string* into a valid <a href="https://en.wikipedia.org/wiki/Slug_%28web_publishing%29" target="_blank" rel="noopener" title="Definition of URL slug">URL slug</a>. It mixes <a href="https://jquery.com" target="_blank" rel="noopener">jQuery</a> with standard JavaScript, and can be easily adapted to pure JS.

```html
<!-- Example input element -->
<input id="controlId" type="text" />
```

```js
// Handles typing
$(document).ready(function () {
  // If the Title is specified, avoid overwrite
  if ($('#controlId').val().length === 0) {
    $('#controlId').on('keypress', function () {
      $('#controlId').val(slugify($('#controlId').val().toLowerCase()));
    });
  }
});

// Replacements
function slugify(text) {
  text = text.replace(/[^-a-zA-Z0-9,&\s]+/g, '');
  text = text.replace(/-/g, '_');
  text = text.replace(/\s/g, '-');
  return text;
}
```

> **Note (2025):** For modern projects you may also want to normalize accents (`é → e`), trim repeated separators, and prefer `input` event instead of `keypress`. This post keeps the original 2010 logic.