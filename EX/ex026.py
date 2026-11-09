# DESAFIO 026: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite um frase qualquer: ').strip()
sem_acento = frase.lower().replace('á', 'a').replace('à', 'a').replace('â', 'a').replace('ã', 'a')
qtde_a = sem_acento.lower().count('a')
primeira = sem_acento.lower().find('a') + 1
ultima = sem_acento.lower().rfind('a') + 1

print(f'Na frase "{frase}" temos:')
print(f'{'Letras A:':<20}{qtde_a:>15}\n{'Primeira aparição:':<20}'
	  f'{primeira:>15}°\n{'Última aparição:':<20}{ultima:>15}°')