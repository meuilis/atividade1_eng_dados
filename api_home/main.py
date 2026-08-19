from src.extract import Extract
from src.load import Load

extract = Extract()
pnadc = extract.extract_pnadc(variaveis="4099", cod_estado="26", classificacao="4")

load = Load()
load.load_json("Pernambuco", pnadc)
print(pnadc)
