# DESAFIO 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
alunos = list()
for i in range(4):
	alunos.append(input('Digite o nome do aluno: '))

escolhido = choice(alunos)

print(f'O aluno escolhido para apagar o quadro foi: {escolhido}')