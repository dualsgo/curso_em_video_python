# Exercício Extra Python #19.4 - Mesclagem e Atualização de Estoque (.update e soma de chaves) - Aula 00 até 19 - Mundo 3
# Nível: Intermediário/Avançado
#
# Dadas duas filiais com seus estoques:
# matriz = {'Teclado': 10, 'Mouse': 25, 'Monitor': 5}
# filial = {'Mouse': 15, 'Monitor': 8, 'Headset': 12}
# Crie um terceiro dicionário 'estoque_total' que some as quantidades dos produtos que existem em ambas
# e mantenha os produtos exclusivos de cada uma.
#
# Exemplo de execução esperada:
#   Estoque Consolidado: {'Teclado': 10, 'Mouse': 40, 'Monitor': 13, 'Headset': 12}
#
# Dica: Se usássemos apenas .update(), o valor de 'Mouse' seria sobrescrito por 15 em vez de somar 25 + 15 = 40!
