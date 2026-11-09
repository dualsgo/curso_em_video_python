# DESAFIO 032: Faça um programa que leia um ano qualquer e mostre se ele é
# bissexto.

# É um número divisível por 4, mas não é divisível por 100.
from random import randint
from datetime import datetime
digitado = randint(1582, 2024)
ano_atual = datetime.today().year
ano = digitado if digitado else ano_atual
bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

print(f'{ano} {'é bissexto' if bissexto else 'não é bissexto'}')