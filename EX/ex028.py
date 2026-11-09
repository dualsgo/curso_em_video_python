# Exercício Python 028: Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 1000)
tentativas = 0
while True:
	usuario = int(input('Digite um número: '))
	tentativas += 1

	print('Processando...')
	sleep(1)
	if usuario == computador:
		print(f'Acertou em {tentativas}', 'tentativas!' if tentativas > 1
		else 'tentativa!')
		break
	else:
		print('Mais baixo!' if usuario > computador else 'Mais alto!')