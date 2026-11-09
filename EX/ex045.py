# DESAFIO 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(jokenpo)
jogador = jokenpo[int(input('[0] PEDRA [1] PAPEL [2] TESOURA'))]

vencedor = ((jogador == 'PAPEL' and computador == 'PEDRA') or
			(jogador == 'PEDRA' and computador == 'TESOURA') or
			(jogador == 'TESOURA' and computador == 'PAPEL'))

print(f'{'JOGADOR':^10}{'|':^10}{'COMPUTADOR':^10}')
print(f'{jogador:^10}{'X':^10}{computador:^10}')

if jogador == computador:
	print(f'{"DEU EMPATE!":^30}')
elif vencedor:
	print(f'{"JOGADOR VENCE!":^30}')
else:
	print(f'{"COMPUTADOR VENCE!":^30}')