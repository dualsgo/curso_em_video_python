# Exercício Extra Python #14.4 - Cálculo de Raiz Quadrada pelo Método de Newton (Aproximação) - Aula 00 até 14 - Mundo 1
# Nível: Intermediário/Avançado
#
# Leia um número positivo X e calcule sua raiz quadrada aproximada sem usar ** ou math.sqrt.
# Comece com um palpite inicial p = X / 2.
# Enquanto a diferença absoluta abs(p * p - X) for maior que 0.0001:
# atualize o palpite pela fórmula: p = (p + X / p) / 2.
#
# Exemplo de execução esperada:
#   Calcular raiz de: 25
#   Iteração 1: 7.25000 | Iteração 2: 5.34914 | ... | Raiz aproximada: 5.00000
#
# Dica: Esse é o algoritmo clássico que calculadoras usam internamente para extrair raízes!
