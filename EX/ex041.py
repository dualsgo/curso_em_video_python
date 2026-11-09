# DESAFIO 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER


from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = ano_atual - ano_nascimento

categoria = (f'MIRIM' if idade < 10 else
             f'INFANTIL' if idade < 15 else
             f'JÚNIOR' if idade < 20 else
			 f'SÊNIOR' if idade < 25 else 'MASTER')

print(f'O atleta tem {idade} anos. Sua categoria será {categoria}')