# Exercício Extra Python #21.6 - Fábrica de Funções com Estado Interno (Closure Pré-POO) - Aula 00 até 21 - Mundo 3
# Nível: Desafio Pré-POO
#
# Antes das Classes, usavam-se Closures (funções que retornam funções) para guardar estado.
# Crie uma função criar_contador(inicio: int = 0) que tenha uma variável interna 'valor = inicio'
# e retorne uma função interna incrementar(passo: int = 1) que some 'passo' ao 'valor' (usando nonlocal)
# e retorne o novo total.
#
# Exemplo de execução esperada:
#   c1 = criar_contador(10)
#   c1() -> 11 | c1(5) -> 16
#
# Dica: Uma Closure que guarda estado é a irmã gêmea funcional de um Objeto em POO!
