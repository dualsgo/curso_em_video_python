# Exercício Extra Python #19.5 - Catálogo de Filmes Aninhado com Busca e Ordenação por Nota - Aula 00 até 19 - Mundo 3
# Nível: Avançado
#
# Crie um dicionário aninhado com 4 filmes, onde a chave é o título e o valor é outro dicionário
# com {'ano': ..., 'genero': ..., 'nota': ...}.
# 1) Permita ao usuário buscar um gênero e liste todos os filmes daquele gênero.
# 2) Exiba o ranking dos filmes ordenados da maior nota para a menor.
#
# Exemplo de execução esperada:
#   Ranking por Nota:
#   1º Interestelar (2014) - Nota: 9.5
#   2º Matrix (1999)       - Nota: 9.2
#
# Dica: Em um dicionário aninhado, item[0] é a chave externa (título) e item[1]['nota'] acessa a nota interna!

# Tarefa 1: Criar o dicionário aninhado com 4 filmes.


# Tarefa 2: Ler um gênero e filtrar percorrendo filmes.items().


# Tarefa 3: Ordenar usando sorted(filmes.items(), key=lambda item: item[1]['nota'], reverse=True).

