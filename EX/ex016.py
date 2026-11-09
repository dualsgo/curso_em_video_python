# DESAFIO 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

numero = float(input('Digite um número Real qualquer... '))

parte_fracionaria = numero % 1
parte_inteira = numero // 1

print(f'Você digitou o número {numero}\nA parte inteira é '
	  f'{parte_inteira:.0f}\nA '
	  f'parte fracionária é {parte_fracionaria}')