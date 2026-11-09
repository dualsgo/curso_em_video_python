# DESAFIO 040: Crie um programa que leia duas notas de um aluno e calcule sua
# média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

media = (float(input('Primeira nota: ')) + float(input('Segunda nota: '))) / 2
print(f'Sua média ficou em {media:.2f}')
if media < 5:
	print('REPROVADO!')
elif media < 7:
	print('RECUPERÇÃO!')
else:
	print('APROVADO!')