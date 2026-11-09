# DESAFIO 053: Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços.

# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

normal = input('Digite uma frase: ').strip().upper().replace(' ', '')
print(f'O inverso de {normal} é {normal[-1::-1]}\nA frase digitada', 'é um palíndromo' if normal == normal[-1::-1] else 'não é uma palíndromo' )