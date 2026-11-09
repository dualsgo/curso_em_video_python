# DESAFIO 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

# a soma de cada dois lados deve ser sempre maior que a medida do terceiro lado
forma_triangulo = a + b > c and a + c > b and a < b + c
tipo_triangulo = ('EQUILÁTERO' if a == b == c else 'ESCALENO' if a != b != c != a else 'ISÓSCELES')

print(f'Os lados A = {a}, B = {b} e C = {c} formam um triangulo {tipo_triangulo}!' if forma_triangulo else f'Os lados A = {a}, B = {b} e C = {c} não formam um triangulo!')