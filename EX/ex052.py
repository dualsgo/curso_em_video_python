# DESAFIO 052: Faça um programa que leia um número inteiro e diga se ele é ou
# não um número primo.
from random import randint
numero = randint(1, 15)
divisores = 0
for i in range(1, numero+1):
	if numero % i == 0:
		divisores += 1
		print(f'\033[1;32m{i}\033[m ⮕ ', end='')
	else:
		print(f'\033[1;31m{i}\033[m ⮕ ', end='')
print(f'{numero}', 'é PRIMO' if divisores == 2 else f'NÃO É PRIMO', f'pois possui {divisores} divisores')