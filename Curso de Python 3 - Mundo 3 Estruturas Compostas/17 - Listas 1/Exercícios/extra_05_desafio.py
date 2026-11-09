# Exercício Extra Python #17.5 - Rotacionador de Lista para Esquerda e Direita (Slicing) - Aula 00 até 17 - Mundo 3
# Nível: Avançado
#
# Dada a lista elementos = [10, 20, 30, 40, 50, 60], leia um número K de posições (ex: 2).
# Usando fatiamento de listas, gere e exiba:
# 1) A lista rotacionada K posições para a ESQUERDA (ex: [30, 40, 50, 60, 10, 20])
# 2) A lista rotacionada K posições para a DIREITA (ex: [50, 60, 10, 20, 30, 40])
#
# Exemplo de execução esperada:
#   Original : [10, 20, 30, 40, 50, 60] | K = 2
#   Esquerda : [30, 40, 50, 60, 10, 20]
#   Direita  : [50, 60, 10, 20, 30, 40]
#
# Dica: Usar k %= len(lista) evita problemas caso o usuário digite uma rotação maior que o tamanho da lista!
