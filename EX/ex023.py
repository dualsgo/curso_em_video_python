# DESAFIO 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.

numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000

print(f'{'MILHAR':^10}{'CENTENAS':^10}{'DEZENAS':^10}{'UNIDADES':^10}')
print(f'{milhar:^10}{centena:^10}{dezena:^10}{unidade:^10}')