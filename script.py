#!/usr/bin/python3

from suds.client import Client
import suds
import sys
import time
import argparse

# Constants

url = 'http://legislatie.just.ro/apiws/FreeWebService.svc?wsdl'
path = 'saved_results.' + str(int(time.time())) + '.txt';

# Command-line option parsing

parser = argparse.ArgumentParser(description='Benchmark legislatie.just.ro')
parser.add_argument("-n", "--lowest", dest="from",
                    help="fetch pages from PAGE", metavar="PAGE", default=0)
parser.add_argument("-N", "--highest", dest="to",
                    help="fetch pages up to PAGE", metavar="PAGE", default=1000)

args = vars(parser.parse_args())

# Script

print("==== create client")
client = Client(url)
print(client)

print("==== get token")
token = client.service.GetToken()
print(token)

print("==== do search")
search_model = client.factory.create('SearchModel')

print("==== saving results to {0}\n".format(path))

with open(path, 'w') as f:
    n = int(args['from'])
    N = int(args['to'])
    for i in range(n, N):
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
