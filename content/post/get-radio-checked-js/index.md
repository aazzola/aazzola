---
title: "Get and Set Radio Controls Checked Value with JavaScript"
type: post
draft: false
date: 2009-03-20T00:00:00
categories: ["Programming", "JavaScript"]
---

Suppose you have the following **radio** controls:

```html
<input name="Book" type="radio" value="asp" checked="true">ASP .NET</input>
<input name="Book" type="radio" value="wcf">Windows Presentation Foundation</input>
<input name="Book" type="radio" value="slg">Silverlight 2.0</input>
```

**How do you get the selected value via JavaScript?**  
As you can see in the example, radio controls are declared with a **name** attribute (not an **id**). The browser treats each radio input as a different element, but the common `name` value groups them logically.

## The `getElementsByName` Method

[W3C Documentation](http://www.w3.org/TR/DOM-Level-2-HTML/html.html#ID-71555259) — This method allows you to obtain a collection of controls from the [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) by specifying the common **name** value.

Here is the code to get or set the **checked** value:

```js
function getRadio(name) {
    var radios = document.getElementsByName(name);
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            return radios[i].value;
        }
    }
    return null;
}

function setRadio(name, val) {
    var radios = document.getElementsByName(name);
    for (var i = 0; i < radios.length; i++) {
        radios[i].checked = (radios[i].value == val);
    }
}
```