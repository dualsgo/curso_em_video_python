# Exercício Python 048: Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = tot = 0
for i in range(3, 500, 3):
	if i % 2:
		soma += i
		tot += 1
		print(i, end=', ')
else:
	print('Fim!')
print(f'Valores: {tot}\nSoma: {soma}')