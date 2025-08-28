---
title: "Submit di un Form tramite POST JavaScript"
type: it
draft: false
date: 2009-07-07T00:00:00
---
# Submit di un Form tramite POST JavaScript

[Andrea Azzola](../../index.html "Back to the Home Page")


Posted on
2009-07-07 12:07
\[<a href="index.html" target="_self" title="Permalink to Submit di un Form tramite POST JavaScript">Permalink</a>\]

Secondo le specifiche <a href="http://www.w3.org/TR/html401/" target="_blank" title="HTML 4.0 specifications by W3C reccomendation">HTML 4.0</a>:

- Se il metodo é "GET", lo user agent prende il valore dell'azione, vi concatena un '?' ed il data set del form, mediante il content-type *application/x-www-form-urlencoded*. Quindi lo user agent inoltra la richiesta includendo questo URI. In questo modalitá, i dati del form sono vincolati a codici ASCII.
- Se il metodo é "POST", lo user agent effettua un submit HTTP POST utilizzando il valore dell'*action* e un messaggio creato in accordo con il content type specificato nell'attributo *enctype*.

## Quali sono i vantaggi dei POST JavaScript?

- Effettuare redirect diversi all'action
- Veicolare dati senza refresh di UI per l'end user
- Evitare l'abuso di query string e 'bellificare' gli URL

## Effettuare un submit POST

Copia-incolla il seguente codice nella sezione <a href="https://it.wikipedia.org/wiki/Elemento_HTML" target="_blank" title="Sezione HEAD su Wikipedia">HEAD</a> della pagina <a href="https://it.wikipedia.org/wiki/Html" target="_blank" title="HTML on Wikipedia">HTML</a>:

    <script language="javascript">
    function post(dictionary, url, method) {
        method = method || "post"; // post (impostato a default) ppure get

        // Crea l'oggetto form
        var form = document.createElement("form");
        form.setAttribute("method", method);
        form.setAttribute("action", url);

        // Per ogni coppia chiave-valore
        for (key in dictionary) {
            //alert('key: ' + key + ', value:' + dictionary[key]); // debug
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", dictionary[key]);
            // appende il nuovo controllo creato
            form.appendChild(hiddenField);
        }

        document.body.appendChild(form); // inietta l'oggetto form nel body del DOM
        form.submit();
    }
    </script>

## Come lo uso?

Copia il seguente codice nella sezione <a href="https://it.wikipedia.org/wiki/Elemento_HTML" target="_blank" title="Sezione BODY su Wikipedia">BODY</a> della pagina HTML. Come vedi viene dichiarata una collezione di oggetti (dizionario), quindi vengono aggiunti due parametri. Puoi aggiungere quanti parametri desideri.

    <script language="javascript">
        var myDictionary = [];
        myDictionary["1stKey"] = "1stValue";
        myDictionary["2ndKey"] = "2ndValue";
    </script>

    <input type="button" value="Click me to POST"
        onclick="javascript:post(myDictionary, 'destination.html');" />
    <input type="button" value="Click me to GET"
        onclick="javascript:post(myDictionary, 'destination.html', 'get');" />

La funzione POST accetta un <a href="https://it.wikipedia.org/wiki/Array_associativo" target="_blank" title="Associative array on Wikipedia">dizionario</a>, una destinazione <a href="https://it.wikipedia.org/wiki/Url" target="_blank" title="Uniform Resource Locator on Wikipedia">URL</a>, e opzionalmente il metodo (POST o GET, case in-sensitive).

## L'alternativo jQuery.post()

Se jQuery é giá parte della tua soluzione, puoi usare la funzione **jQuery.post()** in sostituzione:

    jQuery.post( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )

che constituisce un'abbreviazione per la funzione Ajax:

    $.ajax({
      type: "POST",
      url: url,
      data: data,
      success: success,
      dataType: dataType
    });

Dunque, il codice equivalente il POST dei valori menzionati sopra in jQuery, sarebbe:

    $.post( "test.php", { 1stKey: "1stValue", 2ndKey: "2ndValue" } );

Ulteriori dettagli riguardo jQuery.post() sono disponibili <a href="http://api.jquery.com/jquery.post/" target="_blank" title="jQuery.post() wiki">a questo link</a>.

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Submit%20di%20un%20Form%20tramite%20POST%20JavaScript&amp;url=http%3a%2f%2fandreaazzola.com%2fit%2fjavascript-submit-post-form-data%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="https://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fit%2fjavascript-submit-post-form-data%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

Author's portrait

<a href="https://twitter.com/AndreaAzzola" rel="me" target="_blank" data-text="Twitter" title="Stay up to date with my tweets">My Twitter profile</a><a href="https://www.linkedin.com/in/andreaazzola" rel="me" target="_blank" data-text="LinkedIn" title="Find me on LinkedIn">My LinkedIn profile</a><a href="https://www.facebook.com/andrea.azzola" rel="me" target="_blank" data-text="Facebook" title="Get in touch with Facebook">My Facebook profile</a><a href="http://www.pinterest.com/andreaazzola" rel="me" target="_blank" data-text="Pinterest" title="I&#39;m on Pinterest!">My Pinterest profile</a><a href="https://instagram.com/andrea.azzola" rel="me" target="_blank" data-text="Instagram" title="My Instagram profile">My Instagram profile</a>

- <a href="../../about/index.html" style="font-weight:bold" data-text="About" title="Short summary">About</a>
- <a href="../../articles/index.html" style="font-weight:bold" data-text="Articles" title="Collection of all articles in this website">Articles</a>
- <a href="../../books/index.html" style="font-weight:bold" data-text="Books" title="My book recommendations">Books</a>
- <a href="../../contact/index.html" style="font-weight:bold" data-text="Contact" title="Short summary">Contact</a>
- <a href="../../feed/index.html" data-text="RSS feed" title="Subscribe to this blog">RSS feed</a>
- <a href="../../login/index.html" data-text="Login" title="Login">Login</a>

- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageEN%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageEN" class="lang-sm lang-lbl" lang="en"></a>
- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageIT%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageIT" class="lang-sm lang-lbl" lang="it"></a>

#### Newsletter

 
 

<a href="../../category/books/index.html" class="category" style="font-size:112%;">Books</a>
<a href="../../category/decision-fatigue/index.html" class="category" style="font-size:112%;">Decision Fatigue</a>
<a href="../../category/diet/index.html" class="category" style="font-size:112%;">Diet</a>
<a href="../../category/extreme-saving/index.html" class="category" style="font-size:119%;">Extreme Saving</a>
<a href="../../category/finance/index.html" class="category" style="font-size:112%;">Finance</a>
<a href="../../category/financial-independence/index.html" class="category" style="font-size:125%;">Financial Independence</a>
<a href="../../category/fitness/index.html" class="category" style="font-size:119%;">Fitness</a>
<a href="../../category/gears/index.html" class="category" style="font-size:112%;">Gears</a>
<a href="../../category/geo-arbitrage/index.html" class="category" style="font-size:112%;">Geo Arbitrage</a>
<a href="../../category/goal-setting/index.html" class="category" style="font-size:112%;">Goal Setting</a>
<a href="../../category/nutrition/index.html" class="category" style="font-size:112%;">Nutrition</a>
<a href="../../category/personal-branding/index.html" class="category" style="font-size:112%;">Personal Branding</a>
<a href="../../category/personal-development/index.html" class="category" style="font-size:150%;">Personal Development</a>
<a href="../../category/productivity/index.html" class="category" style="font-size:125%;">Productivity</a>
<a href="../../category/time-management/index.html" class="category" style="font-size:106%;">Time Management</a>