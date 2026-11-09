# Exercício Extra Python #18.4 - Laboratório de Cópia Rasa ([:]) vs Cópia Profunda (copy.deepcopy) - Aula 00 até 18 - Mundo 3
# Nível: Intermediário/Avançado
#
# Crie uma lista aninhada turma_a = [['Ana', 8.5], ['Bruno', 7.0]].
# 1) Crie turma_b = turma_a[:] (cópia rasa) e altere a nota da Ana em turma_b[0][1] = 10.0.
# Mostre como turma_a foi alterada por acidente!
# 2) Repita o teste usando copy.deepcopy(turma_a) e comprove que agora as sublistas são independentes.
#
# Exemplo de execução esperada:
#   Após alterar cópia rasa -> turma_a: [['Ana', 10.0], ['Bruno', 7.0]] (VAZOU!)
#   Após alterar deepcopy   -> turma_a: [['Ana', 8.5], ['Bruno', 7.0]] (PROTEGIDA!)
#
# Dica: Em listas de listas (ou listas de objetos), [:] copia apenas a casca externa!

# Tarefa 1: Importar o módulo copy.


# Tarefa 2: Demonstrar o efeito colateral da cópia rasa [:] em listas aninhadas.


# Tarefa 3: Demonstrar o isolamento completo usando copy.deepcopy().

