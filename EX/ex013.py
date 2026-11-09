# DESAFIO 013: Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário atual: R$ '))
aumento = 0.15
print('='*30)
print(f'{'SALÁRIO ATUAL':<15}{'| R$':^3}{salario:>8.2f}')
print(f'{'AUMENTO DE 15%':<15}{'| R$':^3}{salario * aumento:>8.2f}')
print('='*30)
print(f'{'NOVO SALÁRIO':<15}{'| R$':^3}{salario + (salario * aumento):>8.2f}')