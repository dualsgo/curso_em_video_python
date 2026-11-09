# Exercício Python 056: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media_idade = 0
nome_mais_velho = ''
idade_mais_velho = 0
mulheres_menos_vinte = 0

for i in range(1, 5):
	print(f'{i}ª PESSOA')
	nome = input('Nome: ').strip().title()
	idade = int(input('Idade: '))
	sexo = input('Sexo: ').strip().upper()

	media_idade += idade

	if i == 1:
		nome_mais_velho = nome
		idade_mais_velho = idade
	else:
		if idade > idade_mais_velho:
			nome_mais_velho = nome
			idade_mais_velho = idade

	if sexo == 'F' and idade < 20:
		mulheres_menos_vinte += 1

print(f'A média de idade das 4 pessoas é de {media_idade/4} anos')
print(f'A pessoa mais velha se chama {nome_mais_velho} e tem '
	  f'{idade_mais_velho} anos')
print(f'Ao todo temos {mulheres_menos_vinte} mulheres com menos de 20 anos')