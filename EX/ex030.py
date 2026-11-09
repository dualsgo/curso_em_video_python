# DESAFIO 030: Crie um programa que leia um número inteiro e mostre na tela se
# ele é PAR ou ÍMPAR.

numero = int(input("Digite um número inteiro: "))
print(f'{numero} é ímpar!' if numero % 2 else f'{numero} é par!')