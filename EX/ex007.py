# DESAFIO 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_um = float(input('Primeira nota: '))
nota_dois = float(input('Segunda nota: '))

media = (nota_um + nota_dois) / 2

print(f'{'BOLETIM':^20}')
print(f'{'NOTA 1':<10}{nota_um:>10}')
print(f'{'NOTA 2':<10}{nota_dois:>10}')
print(f'{'='*20}')
print(f'{'MÉDIA':<10}{media:>10.1f}')