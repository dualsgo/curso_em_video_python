# DESAFIO 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Carteira: R$ '))

print(f'Você possui R${carteira:.2f}')

dolar = 3.27

print(f'Você pode comprar U${carteira / dolar:.2f}')