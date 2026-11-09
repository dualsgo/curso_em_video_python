# Aula 24 - Manipulação de Arquivos e Persistência de Dados
# Referência prática de operações de arquivo em Python

import json

# 1. Escrita de arquivo de texto (modo 'w')
with open('relatorio.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('--- RELATÓRIO DO SISTEMA ---\n')
    arquivo.write('Usuário: Administrador\n')
    arquivo.write('Status: OK\n')

# 2. Append (modo 'a')
with open('relatorio.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Atualização: Novo registro inserido.\n')

# 3. Leitura linha a linha (modo 'r')
with open('relatorio.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# 4. Persistência de dados complexos com JSON
clientes = [
    {'id': 1, 'nome': 'Beatriz', 'saldo': 2500.0},
    {'id': 2, 'nome': 'Fernando', 'saldo': 3800.5}
]

with open('clientes.json', 'w', encoding='utf-8') as f_json:
    json.dump(clientes, f_json, indent=4, ensure_ascii=False)

with open('clientes.json', 'r', encoding='utf-8') as f_json:
    dados_lidos = json.load(f_json)
    print(f'Total de clientes carregados do JSON: {len(dados_lidos)}')
