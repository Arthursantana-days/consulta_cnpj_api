
import requests

cnpj = '05061448000139'
url = f'https://api.opencnpj.org/{cnpj}'
res = requests.get(url)
dados = res.json()


print(f'CNPJ: {dados["cnpj"]}')
print(f'E-mail: {dados["email"]}')
print('Razão social: ', dados["razao_social"])
print(f'Nome fantasia: {dados["nome_fantasia"]}')
print(f'Situação cadastral: {dados["situacao_cadastral"]}')
