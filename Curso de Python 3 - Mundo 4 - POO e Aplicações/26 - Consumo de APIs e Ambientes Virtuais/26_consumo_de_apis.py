# Aula 26 - Consumo de APIs REST com Python e Boas Práticas
# Demonstração com a biblioteca requests

import requests

def consultar_cep(cep: str):
    """Consulta dados de endereço usando a API pública ViaCEP."""
    cep_limpo = cep.replace('-', '').strip()
    url = f'https://viacep.com.br/ws/{cep_limpo}/json/'

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if 'erro' in dados:
                print(f'CEP {cep} não foi encontrado.')
            else:
                print(f'Logradouro: {dados.get("logradouro")}')
                print(f'Bairro: {dados.get("bairro")}')
                print(f'Cidade/UF: {dados.get("localidade")}/{dados.get("uf")}')
        else:
            print(f'Erro na consulta: Status HTTP {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro de conexão: {e}')


if __name__ == '__main__':
    # Teste de consulta de CEP da Praça da Sé, São Paulo:
    consultar_cep('01001-000')
