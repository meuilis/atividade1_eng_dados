import requests

class Extract():
    def __init__(self):
        pass
        
    def extract_pnadc(self, variaveis, cod_estado, classificacao):
                url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202602/variaveis/{variavel}?localidades=N3[{cod_estado}]&classificacao=2[{classificacao}]"
                response = requests.get(url)
                data = response.json()
                return data

