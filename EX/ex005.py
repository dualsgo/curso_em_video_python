# DESAFIO 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite o número que deseja analisar: '))
antecessor = numero - 1
sucessor = numero + 1

print(f'Antecessor{antecessor:^5}>{numero:^10}>{sucessor:^5}Sucessor')