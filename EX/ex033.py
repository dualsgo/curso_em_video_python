# DESAFIO 033: Faça um programa que leia três números e mostre qual
# é o maior e qual é o menor.
maior = menor = valor = int(input('Digite o primeiro valor: '))
for i in range(2):
	valor = int(input(f'Digite o {'segundo' if i == 0 else 'terceiro'} valor: '))
	if valor > maior:
		maior = valor
	elif valor < menor:
		menor = valor
print(f'{'Maior:':<6}{maior:>3}')
print(f'{'Menor:':<6}{menor:>3}')