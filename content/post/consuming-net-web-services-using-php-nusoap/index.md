---
title: "Consuming .NET Webservices Using PHP and NuSoap"
type: post
draft: false
date: 2007-10-23T00:00:00
categories: ["Programming", "PHP", ".NET"]
---

In my scenario a .NET webservice offers particular encrypting capabilities. I need to consume the webservice with PHP by sending my plain string to get an encrypted one in return. The .NET webservice is working properly. I found the [NuSoap](http://sourceforge.net/projects/nusoap/) library, and adopted it.

Here the inclusion:

```php
require_once('lib/nusoap.php');
```

And here the code:

```php
// requires web service's specifications aka wsdl
// $parameters:
// requires following the array 'notation'
// array('parameters' => (array('text' => 'Hello World!!!')));
// that equals to Hello World!!!
// $proxy (->host, ->port, ->username, ->password)
// optional, uses a proxy server

function consume_webservice($wsdl, $method, $parameters, $debug = false, $proxy = null)
{
    if ($proxy != null)
        $proxy->host = $proxy->port = $proxy->username = $proxy->password = false;

    $client = new soapclient($wsdl, true, $proxy->host, $proxy->port,
        $proxy->username, $proxy->password);
    $err = $client->getError();

    if ($err)
        echo 'Constructor error' . $err;

    $result = $client->call($method, $parameters);

    // check for a fault
    if ($client->fault)
    {
        echo 'Fault';
        print_r($result);
    }
    else
    {
        // check for errors
        $err = $client->getError();

        if ($err)
            echo 'Error' . $err;
    }

    if ($debug)
    {
        echo 'Request' . htmlspecialchars($client->request, ENT_QUOTES);
        echo 'Response' . htmlspecialchars($client->response, ENT_QUOTES);
        echo 'Debug' . htmlspecialchars($client->debug_str, ENT_QUOTES);
    }

    return $result;
}
```

This approach works only with [SOAP](http://en.wikipedia.org/wiki/SOAP) webservices. Please note that .NET web services include all response content into a "*parameters*" section by design.