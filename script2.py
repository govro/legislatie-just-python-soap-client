from suds.client import Client

url = 'http://legislatie.just.ro/apiws/FreeWebService.svc?wsdl'

print("==== create client")
client = Client(url)
print(client)

print("==== get token")
token = client.service.GetToken()
print(token)

print("==== do search")
search_model = client.factory.create('SearchModel')
search_model.NumarPagina = 0
search_model.RezultatePagina = 0
search_model.SearchAn = 2014
search_model.SearchTitlu = "medici"

results = client.service.Search(search_model, token)

for law in results.Legi:
    print("{0}\n{1}\n\n".format(law.Titlu, law.DataVigoare))
