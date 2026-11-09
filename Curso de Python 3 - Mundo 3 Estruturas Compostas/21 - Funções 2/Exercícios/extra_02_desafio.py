# Exercício Extra Python #21.2 - Ordenação Personalizada de Dicionários com lambda (sorted key) - Aula 00 até 21 - Mundo 3
# Nível: Básico/Intermediário
#
# Dada uma lista de produtos:
# produtos = [{'nome': 'Monitor', 'preco': 900, 'avaliacao': 4.7},
#             {'nome': 'Mouse', 'preco': 80, 'avaliacao': 4.9},
#             {'nome': 'Teclado', 'preco': 200, 'avaliacao': 4.5}]
# Use sorted() com key=lambda p: ... para exibir:
# 1) Os produtos do mais barato para o mais caro
# 2) Os produtos da maior avaliação para a menor (reverse=True)
#
# Exemplo de execução esperada:
#   Por menor preço    : Mouse (R$ 80), Teclado (R$ 200), Monitor (R$ 900)
#   Por melhor avaliação: Mouse (4.9), Monitor (4.7), Teclado (4.5)
#
# Dica: O parâmetro key= recebe uma função que diz ao Python qual campo usar na comparação!

# Tarefa 1: Definir a lista de dicionários de produtos.


# Tarefa 2: Ordenar por preço usando sorted(produtos, key=lambda item: item['preco']).


# Tarefa 3: Ordenar por avaliação usando reverse=True e exibir ambos os rankings.

