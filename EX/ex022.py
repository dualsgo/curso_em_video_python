# DESAFIO 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo. (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Digite o nome da pessoa: ').strip()
maiusculas = nome.upper()
minusculas = nome.lower()
lista = nome.split()
tamanho_nome = len(''.join(lista))
primeiro_nome = lista[0]
tamanho_primeiro_nome = len(lista[0])


print(f'Analisando o nome "{nome}":')
print(f'Em MAIÚSCULAS: {maiusculas}')
print(f'Em MINÚSCULAS: {minusculas}')
print(f'Quantidade de letras nome completo: {tamanho_nome} letras')
print(f'Quantidade de letras primeiro nome: {primeiro_nome} - '
	  f'{tamanho_primeiro_nome} letras')