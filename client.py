from suds.client import Client


class LegislatieJustClient:
    def __init__(self):
        self.url = 'http://legislatie.just.ro/apiws/FreeWebService.svc?wsdl'
        self.client = Client(self.url)
        self.token = self.client.service.GetToken()

    def search(self, params):
        search_model = self.client.factory.create('SearchModel')
        search_model.NumarPagina = params.get('NumarPagina', 0)
        search_model.RezultatePagina = params.get('RezultatePagina', 0)

        if 'SearchAn' in params:
            search_model.SearchAn = params['SearchAn']

        if 'SearchTitlu' in params:
            search_model.SearchTitlu = params['SearchTitlu']

        if 'SearchNumar' in params:
            search_model.SearchNumar = params['SearchNumar']

        if 'SearchText' in params:
            search_model.SearchText = params['SearchText']

        return self.client.service.Search(search_model, self.token).Legi

if __name__ == '__main__':
    client = LegislatieJustClient()
    results = client.search()

    for law in results.Legi:
        print("{0}\n{1}\n\n".format(law.Titlu, law.DataVigoare))
