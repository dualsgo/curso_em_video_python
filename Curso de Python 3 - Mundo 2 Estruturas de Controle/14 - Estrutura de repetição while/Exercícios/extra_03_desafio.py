# Exercício Extra Python #14.3 - Conjectura de Collatz (Sequência 3n + 1) - Aula 00 até 14 - Mundo 1
# Nível: Intermediário
#
# Leia um número inteiro positivo N maior que 1.
# Enquanto N for diferente de 1, aplique a regra de Collatz:
# - Se N for par, divida-o por 2 (N = N // 2).
# - Se N for ímpar, multiplique por 3 e some 1 (N = 3 * N + 1).
# Mostre todos os números gerados na sequência e quantos passos levou para chegar a 1.
#
# Exemplo de execução esperada:
#   Digite N: 6
#   6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (Total de 8 passos)
#
# Dica: Use divisão inteira // 2 para que os números da sequência continuem sendo int e não float.
