# Exercício Extra Python #19.2 - Transformação e Filtro com Dict Comprehension - Aula 00 até 19 - Mundo 3
# Nível: Básico/Intermediário
#
# Dado o dicionário de notas_alunos = {'Ana': 8.5, 'Bruno': 5.0, 'Carla': 9.0, 'Diego': 4.5, 'Elena': 7.5}:
# Usando Dict Comprehension ({k: v for k, v in ...}):
# 1) Crie um dicionário 'aprovados' contendo apenas os alunos com nota >= 7.0.
# 2) Crie um dicionário 'situacao' onde a chave é o nome e o valor é 'APROVADO' ou 'REPROVADO'.
#
# Exemplo de execução esperada:
#   Aprovados: {'Ana': 8.5, 'Carla': 9.0, 'Elena': 7.5}
#   Situação : {'Ana': 'APROVADO', 'Bruno': 'REPROVADO', ...}
#
# Dica: Sintaxe: {aluno: ('APROVADO' if nota >= 7 else 'REPROVADO') for aluno, nota in notas_alunos.items()}.
