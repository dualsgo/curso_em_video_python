# Exercício Python 051: Desenvolva um programa que leia
# o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da progressão: '))
for i, v in enumerate(range(primeiro_termo, 10*razao, razao)):
	print(f'{v} ⮕ ' if i < 9 else f'{v} ⮕ FIM!', end='')