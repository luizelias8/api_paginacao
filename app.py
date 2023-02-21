# https://www.youtube.com/watch?v=Vx6pmmRqCxI

import requests

pular_indice = 0

while True:

    api_url = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={pular_indice}&$orderby=Data%20desc&$format=json'

    requisicao = requests.get(api_url)

    dados = requisicao.json()['value']

    if len(dados) == 0:
        break

    print(dados)
    print('*'*50)

    pular_indice += 10000