# DESAFIO 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o nome da pessoa: ').strip().title()
condicional = nome.split()
print('Tem SILVA!' if 'Silva' in condicional else 'Não tem SILVA!')