# DESAFIO 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')


if algo.isnumeric():
    inteiro = int(algo)
    print(f'{inteiro} é um valor numérico da classe {type(inteiro).__name__}')

elif algo.replace('.', '').isnumeric():  # Verifica se os caracteres restantes formam um número
    decimal = float(algo)
    print(f'{decimal} é um valor numérico da classe {type(decimal).__name__}')

else:
    print(f'{algo} é um valor da classe {type(algo).__name__}')
    print(f'{algo} está somente em maiúsculas? '
		  f'{'Sim' if algo.isupper() else 'Não'}')
    print(f'{algo} está somente em minúsculas? '
		  f'{'Sim' if algo.islower() else 'Não'}')