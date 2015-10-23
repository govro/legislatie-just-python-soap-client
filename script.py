#!/usr/bin/python3

from suds.client import Client
import suds
import time

url = 'http://legislatie.just.ro/apiws/FreeWebService.svc?wsdl'

print("==== create client")
client = Client(url)
print(client)

print("==== get token")
token = client.service.GetToken()
print(token)

print("==== do search")
search_model = client.factory.create('SearchModel')

NUM_PAGES = 1000
path = 'saved_results.' + str(int(time.time())) + '.txt';

print("==== saving results to {0}\n".format(path))

with open(path, 'w') as f:
    for i in range(NUM_PAGES):
        search_model.NumarPagina = i
        search_model.RezultatePagina = 0

        try:
            results = client.service.Search(search_model, token)
        except suds.WebFault:
            token = client.service.GetToken()
            results = client.service.Search(search_model, token)

        if len(results) == 0:
            print("==== ! empty results at page {0}\n".format(i))
        else:
            print("==== fetching {0} page\n".format(i))
            for law in results.Legi:
                f.write("{0}\n{1}\n\n".format(law.Titlu, law.DataVigoare))
