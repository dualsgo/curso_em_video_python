# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
# Versão 1
peso = [float(input(f'Peso da {i}ª pessoa: ')) for i, v in enumerate(range(5), 1)]
print(f'O maior peso é {max(peso)}kg e o menor peso é {min(peso)}kg')

# Versão dois
maior = float(
	'-inf')  # Definie o maior como o menor número possível, assim qualquer número que digitar, por menor que seja ainda assim será maior que ele

menor = float(
	'inf')  # Aqui é semelhante, mas definimos como o maior número possível, assim qualquer número que digitar será menor que ele.

for i in range(1, 6):
	peso = int(input(f'Digite o peso da {i}ª pessoa'))

	if peso > maior:
		maior = peso
	if peso < menor:
		menor = peso

print(f'Maior: {maior}')
print(f'Menor: {menor}')