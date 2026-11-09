# DESAFIO 034: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? R$ '))
com_aumento = salario * (1.1 if salario > 1250 else 1.15)

print(f'{'ATUAL:':<6}{'R$':>4}{salario:>8.2f}')
print(f'{'NOVO:':<6}{'R$':>4}{com_aumento:>8.2f}')