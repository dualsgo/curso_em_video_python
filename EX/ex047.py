# DESAFIO 047: Crie um programa que mostre na tela
# todos os números pares que estão no intervalo entre 1 e 50.

lista = [n for n in range(1, 51)]
pares = [i for i in lista if i % 2 == 0]

for i in range(2, 51, 2):
	print(i, end=' ')