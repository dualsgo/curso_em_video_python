# Exercício Extra Python #21.5 - Criando seu Primeiro Decorator de Medição / Auditoria (@auditar) - Aula 00 até 21 - Mundo 3
# Nível: Avançado
#
# Crie um decorator chamado @auditar que receba uma função, imprima '[AUDITORIA] Chamando função <nome>'
# antes de executá-la, execute a função original repassando *args e **kwargs,
# e imprima '[AUDITORIA] Retorno obtido: <resultado>' antes de devolver o valor.
# Aplique @auditar sobre uma função calcular_bonus(salario, percentual).
#
# Exemplo de execução esperada:
#   [AUDITORIA] Chamando função 'calcular_bonus'...
#   [AUDITORIA] Retorno obtido: 450.0
#
# Dica: Entender como @auditar envolve uma função fará você dominar @property e @classmethod em POO instantaneamente!
