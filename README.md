# Exemple de folosire pentru API-ul http://legislatie.just.ro/

API-ul este unul [SOAP](https://en.wikipedia.org/wiki/SOAP). Cele două exemple
au fost scrise în Python 3 și cu ajutorul bibliotecii [SUDS](https://fedorahosted.org/suds).

Documentația se găsește [aici](http://legislatie.just.ro/ServiciulWebLegislatie.htm).

Pentru a rula exemplele:

```
pip3 install -r requirements.txt
python3 script.py
```

## `client.py`

Client simplu care abstractizează întreaga arhitectură SOAP.

## `server.py`

Un server de Flask cu un formular și interfața de afișare a rezultatelor.

## `script.py`

Întoarce primele 10 legi.

## `script2.py`

Caută legile din 2014 care conțin în titlu cuvântul `medici`.

## `master.py`

Spawn processes of `script.py` and start downloading the entire database.
