# Exercício Extra Python #21.1 - Pipeline Funcional com lambda, map() e filter() - Aula 00 até 21 - Mundo 3
# Nível: Básico
#
# Dada a lista de salários brutos = [1800.0, 3200.0, 1500.0, 4500.0, 2100.0, 6000.0]:
# 1) Use filter() com lambda para separar apenas os salários acima de R$ 2.500,00.
# 2) Use map() com lambda sobre a lista filtrada para descontar 15% de imposto (multiplicar por 0.85).
# Converta o resultado para list() e exiba.
#
# Exemplo de execução esperada:
#   Salários > 2500 (brutos)  : [3200.0, 4500.0, 6000.0]
#   Após desconto de 15% (map): [2720.0, 3825.0, 5100.0]
#
# Dica: Lembre-se que map() e filter() retornam iteradores, então usamos list() para visualizar os valores.

# Tarefa 1: Definir a lista de salários.


# Tarefa 2: Aplicar list(filter(lambda s: s > 2500, salarios)).


# Tarefa 3: Aplicar list(map(lambda s: round(s * 0.85, 2), filtrados)) e exibir.

