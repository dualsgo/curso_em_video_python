# DESAFIO 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço do produto R$ '))
print(f'{'='*30}')
print(f'{'PREÇO ORIGINAL':<15}{'R$':>5}{preco:>10.2f}')
print(f'{'DESCONTO 5%':<15}{'R$':>5}{preco * .05:>10.2f}')
print(f'{'-'*30}')
print(f'{'VALOR FINAL':<15}{'R$':>5}{preco - (preco * .05):>10.2f}')
print(f'{'='*30}')