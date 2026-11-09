# DESAFIO 039: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'Você jovem, está completando {idade} anos em {ano_atual}.')

if idade == 18:
	print(f'Você está na idade exata para se alistar! Procure uma junta '
		  f'militar.')
else:
	if idade < 18:
		print(f'Você ainda não possui a idade exigida. Seu alistamento deverá '
		f'ocorrer no ano de {ano_nascimento + 18}. Faltam '
		f'{18 - idade} anos!')
	else:
		print(f'Você já passou da idade exigida. A época do seu alistamento '
		f'ocorreu no ano de {ano_nascimento + 18}. Se passaram '
		f'{idade - 18} anos!')