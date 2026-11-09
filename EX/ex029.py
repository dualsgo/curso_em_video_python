# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km/h acima do limite.

from random import randint
limite = 80
velocidade = randint(75, 85)
acima = velocidade - limite
multado = acima > 0
multa = acima * 10
if multado:
	print(f'VELOCIDADE: {velocidade}Km/h')
	print(f'\033[1;31mMultado em R${multa:.2f} por ultrapassar {acima}Km/h o '
		  f'limite permitido de 80Km/h\033[m')
else:
	print(f'VELOCIDADE: {velocidade}Km/h')
	print('\033[1;32mDentro do limite permitido!\033[m')