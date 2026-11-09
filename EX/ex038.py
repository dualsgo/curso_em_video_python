# DESAFIO 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
if primeiro > segundo:
	maior = primeiro
	print(f'O maior é... ')
elif primeiro < segundo:
	maior = segundo
	print(f'O maior é... ')
else:
	maior = 'São iguais'
print(maior)