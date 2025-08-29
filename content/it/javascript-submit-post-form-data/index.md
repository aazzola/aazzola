---
title: "Submit di un Form tramite POST JavaScript"
type: post
draft: false
date: 2009-07-07T00:00:00
categories: ["Programmazione", "JavaScript", "Web Development"]
tags: ["form", "submit", "post", "get", "jquery"]
---

Secondo le specifiche [HTML 4.0](http://www.w3.org/TR/html401/){:target="_blank" rel="noopener"}:

- Se il metodo è **GET**, lo user agent prende il valore dell'azione, vi concatena un `?` e il data set del form, mediante il content-type *application/x-www-form-urlencoded*. In questo caso i dati del form sono vincolati a codici ASCII.
- Se il metodo è **POST**, lo user agent effettua un submit HTTP POST utilizzando il valore dell’*action* e un messaggio creato in accordo con il content type specificato nell'attributo *enctype*.

## Vantaggi dei POST JavaScript

- Effettuare redirect diversi all'action
- Veicolare dati senza refresh della UI
- Evitare query string troppo lunghe e URL poco leggibili

## Esempio di submit POST

Inserire il seguente codice nella sezione `<head>` della pagina HTML:

```html
<script>
function post(dictionary, url, method) {
    method = method || "post"; // default: POST

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", url);

    for (var key in dictionary) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", dictionary[key]);
        form.appendChild(hiddenField);
    }

    document.body.appendChild(form);
    form.submit();
}
</script>
```

### Utilizzo

Nella sezione `<body>` della pagina HTML:

```html
<script>
    var myDictionary = [];
    myDictionary["1stKey"] = "1stValue";
    myDictionary["2ndKey"] = "2ndValue";
</script>

<input type="button" value="Click me to POST"
    onclick="post(myDictionary, 'destination.html');" />
<input type="button" value="Click me to GET"
    onclick="post(myDictionary, 'destination.html', 'get');" />
```

La funzione `post` accetta un [dizionario](https://it.wikipedia.org/wiki/Array_associativo){:target="_blank" rel="noopener"}, una destinazione URL, e opzionalmente il metodo (POST o GET, case-insensitive).

## Alternativa con jQuery.post()

Se jQuery è già incluso nella soluzione, è possibile usare la funzione `jQuery.post()`:

```javascript
$.post( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )
```

che rappresenta un'abbreviazione per la funzione `$.ajax`:

```javascript
$.ajax({
  type: "POST",
  url: url,
  data: data,
  success: success,
  dataType: dataType
});
```

### Esempio con jQuery

```javascript
$.post("test.php", { 1stKey: "1stValue", 2ndKey: "2ndValue" });
```

Ulteriori dettagli su [`jQuery.post()`](http://api.jquery.com/jquery.post/){:target="_blank" rel="noopener"}.