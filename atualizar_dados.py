import requests
import json

def extrair_dados():
    # Busca deputados e salva em JSON para o front-end consumir
    url = "https://dadosabertos.camara.leg.br/api/v2/deputados?itens=1000&ordem=ASC&ordenarPor=nome"
    response = requests.get(url)
    if response.status_code == 200:
        with open('dados_deputados.json', 'w', encoding='utf-8') as f:
            json.dump(response.json()['dados'], f, ensure_ascii=False)
        print("Dados atualizados com sucesso!")

if __name__ == "__main__":
    extrair_dados()