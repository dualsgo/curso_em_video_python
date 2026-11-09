# DESAFIO 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('-' * 40)
print(f'{'Simulador de financiamento':^50}')
print('-' * 40)

valor = float(input(f'Valor do imóvel: R$ '))
salario = float(input(f'Valor do salário: R$ '))
prazo = int(input(f'Prazo em anos: '))
print('-' * 40)
parcela = valor / (prazo * 12)
print(f'{'Valor do imóvel:':<25}{'R$':>3}{f'{valor:.2f}':>12}')
print(f'{'Salário comprador:':<25}{'R$':>3}{f'{salario:.2f}':>12}')
print('-' * 40)
print(f'{'Valor máximo da parcela:':<25}{'R$':>3}{f'{salario * .3:.2f}':>12}')
print(f'{'Valor parcelas mensais:':<25}{'R$':>3}{f'{parcela:.2f}':>12}')
print('-' * 40)
print(f'Empréstimo {'negado!' if parcela > (salario * .3) else 'aprovado!'}')