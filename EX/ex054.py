# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
ano_nascimento = [int(input(f'Ano de nascimento da {i}ª pessoa: ')) for i, v in enumerate(range(7), 1)]
maiores = [i for i in ano_nascimento if ano_atual - i > 17]
print(f'Ao todos temos {len(maiores)} maiores de idade e {len(ano_nascimento) - len(maiores)} menores de idade!')