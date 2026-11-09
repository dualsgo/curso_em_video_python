# DESAFIO 037: Escreva um programa em Python que leia um número
# inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))
menu = int(input('Escolha uma das opções:\n[1] BIN [2] OCT [3] HEX '))

convertido = (f'{numero:b}' if menu == 1 else
             f'{numero:o}' if menu == 2 else
             f'{numero:x}' if menu == 3 else 'Opção inválida!')

print(f'O número {numero} convertido fica: {convertido}')