# DESAFIO 018: Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Informe um ângulo qualquer: '))
casas_decimais = int(input('Em quantas casas decimais deseja os resultados? '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'Para um ângulo de {angulo}°')
print(f'O seno é {seno:.{casas_decimais}f}\n'
	f'O cosseno é {cosseno:.{casas_decimais}f}\n'
	f'A tangente é {tangente:.{casas_decimais}f}')