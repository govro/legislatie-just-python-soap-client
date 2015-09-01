# Exemple de folosire pentru API-ul http://legislatie.just.ro/

API-ul este unul [SOAP](https://en.wikipedia.org/wiki/SOAP). Cele două exemple
au fost scrise în Python 3 și cu ajutorul bibliotecii [SUDS](https://fedorahosted.org/suds).

Documentația se găsește [aici](http://legislatie.just.ro/ServiciulWebLegislatie.htm).

Pentru a rula exemplele:

```
pip3 install suds-jurko
python3 script.py
```

## `client.py`

Client simplu care abstractizează întreaga arhitectură SOAP.

## `server.py`

Un server de Flask cu un formular și interfața de afișare a rezultatelor.

## `script.py`

Întoarce ultimele 10 legi apărute pe portal.

## `script2.py`

Caută legile din 2014 care conțin în titlu cuvântul `medici`.
