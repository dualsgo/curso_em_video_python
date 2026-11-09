# DESAFIO 044: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
valor = float(input('Valor da compra R$ '))
pagamento = int(input('[1] DINHEIRO/PIX/DÉBITO/CRÉDITO [2] PARCELADO '))

if pagamento == 1:
	pagamento = int(input('[1] DINHEIRO [2] PIX [3] CRÉDITO/DÉBITO '))
	desconto = .1 if pagamento == 1 else .05
	print('-'* 35)
	print(f'Você receberá um desconto de 10%!')
	print('-'* 35)
	print(f'{'COMPRA ':.<20}{' R$':.>5}{valor:>10.2f}')
	print(f'{'DESCONTO ':.<20}{' R$':.>5}{valor * .1:>10.2f}')
	print('-'* 35)
	print(f'{'TOTAL ':.<20}{' R$':.>5}{valor - valor * .1:>10.2f}')

else:
	parcelas = int(input('QUANTIDADE DE PARCELAS: '))
	if parcelas == 2:
		print('-' * 35)
		print(f'{'COMPRA ':.<20}{' R$':.>5}{valor:>10.2f}')
		print(f'{'PARCELAS ':.<15}{f' {parcelas}X R$':.>10}'
			  f'{valor / parcelas:>10.2f}')
		print('-' * 35)
		print(f'{'TOTAL ':.<20}{' R$':.>5}{valor:>10.2f}')
	else:
		print('-' * 35)
		print(f'{'COMPRA ':.<20}{' R$':.>5}{valor:>10.2f}')
		print(f'{'JUROS ':.<20}{' R$':.>5}{valor*.2:>10.2f}')
		print(f'{'PARCELAS ':.<15}{f' {parcelas}X R$':.>10}'
			  f'{(valor*1.2) / parcelas:>10.2f}')
		print('-' * 35)
		print(f'{'TOTAL ':.<20}{' R$':.>5}{valor*1.2:>10.2f}')