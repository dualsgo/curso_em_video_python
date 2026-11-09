# DESAFIO 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
alunos = list()
for i in range(1, 5):
	alunos.append(input(f'Digite o nome do {i}° aluno: '))

shuffle(alunos)

print('A ordem de apresentação será a seguinte:')
for i, p in enumerate(alunos, 1):
	print(f'{i}° - {p}')