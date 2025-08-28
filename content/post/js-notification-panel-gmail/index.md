---
title: "JavaScript Auto-collapsing Notification Panel"
type: post
draft: false
date: 2009-05-29T00:00:00
categories: ["Programming", "JavaScript"]
tags: ["JavaScript", "UI", "Notification"]
---

> **Note (2025):** This article was originally written in 2009. The example code (inline `onclick`, manual `style.display` changes) reflects practices of that era. Modern JavaScript uses event listeners, unobtrusive DOM manipulation, and CSS transitions. The post is kept here as an archive and for historical interest.

In almost all web applications comes the moment when it becomes necessary to show some notifications to the user. A common practice in the past, even when elegance was unimportant and web pages didn't show much dynamic behavior, was the use of the method `alert()` from JavaScript.

Nowadays, interacting with the [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model){target="_blank" rel="noopener"} is widespread, so you can write functions in a more elegant, advanced, and enjoyable way for the user.

This behavior was made famous by [Gmail](https://en.wikipedia.org/wiki/Gmail){target="_blank" rel="noopener"}. It's nothing exceptional and can be managed with a few simple lines of code:

```html
<div id="notification">
  Hello World!!!
  (<a href="#" onclick="document.getElementById('notification').style.display='none'; return false;">close</a>)
</div>

<script>
function closeDiv() {
  document.getElementById('notification').style.display = 'none';
}
</script>

<input type="button" value="Hide" onclick="window.setTimeout(closeDiv, 5000);" />
```

You can use CSS to make your DIV appear like a popup. Additionally, using a library like [jQuery](https://jquery.com){target="_blank" rel="noopener"} you can easily introduce more advanced text effects.