# Exercício Python #070 - Estatísticas em produtos - Aula 00 até 15 - Mundo 2
#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

"""
Essa verificação é necessária porque, na primeira iteração (quando contador é igual a 1), você não tem um valor anterior para comparar.

if contador == 1:
    produto_mais_barato = nome
    valor_produto_mais_barato = valor
else:
    if valor < valor_produto_mais_barato:
        produto_mais_barato = nome
        valor_produto_mais_barato = valor

No entanto, você pode simplificar isso utilizando uma técnica comumente chamada de "sentinela". Nesse caso, você inicializa valor_produto_mais_barato com um valor que representa infinito, indicado por float('inf'). Como nenhum preço real será maior que infinito, na primeira iteração, qualquer preço será menor que esse valor "infinito". Isso elimina a necessidade de verificar se contador é igual a 1.

valor_produto_mais_barato = float('inf')  # Inicializa com infinito

while True:
    # ... (restante do código)

    if valor < valor_produto_mais_barato:
        # Atualiza o produto mais barato se o valor atual for menor
        produto_mais_barato = nome
        valor_produto_mais_barato = valor
"""
