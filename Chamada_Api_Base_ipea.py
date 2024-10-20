import requests as rq
import json
import pandas as pd

# URL da API pública -
# Feminicíos mulheres Negras  - 142
# Abrangencia - UF


url = "https://www.ipea.gov.br/atlasviolencia/api/v1/valores-series/142/3"

# Fazer a requisição GET para a API
response = rq.request("get", url)  # Requisição API metodo GET
# Converter os dados em dicionario text - metodo
retor_requi = json.loads(response.text)
df = pd.DataFrame(retor_requi)  # Transformar dic em Data Frame
print(df)

print(f"Erro na requisição: {response.status_code}")
