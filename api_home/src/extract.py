##url = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202602/variaveis/4099?localidades=N3[26]&classificacao=2[all]"

##response = requests.get(url) #obter status resposta da requisição
##data = response.json() #transformar a resposta em json

##print(data)

"""import requests

url = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202602/variaveis/4096%7C4099%7C12466?localidades=N3[26]&classificacao=2[all]"

response = requests.get(url)
data = response.json()

print(data)"""

import requests

params = {
            "variavel": [4096, 4099, 12466],
            "classificacao": [6794, 4, 5]
            }

class Extract():
    def __init__(self, params):
        self.params = params

    def extract_data(self):
        for variavel in self.params["variavel"]:
            for classificacao in self.params["classificacao"]:
                url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202602/variaveis/{variavel}?localidades=N3[26]&classificacao=2[{classificacao}]"
                response = requests.get(url)
                data = response.json()
                print(data)

