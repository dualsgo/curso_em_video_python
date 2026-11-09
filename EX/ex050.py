# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
from random import randint
nmbrs = [randint(0, 999) for i in range(6)]
soma = [i for i in nmbrs if i % 2 == 0]
print(list(i for i in soma), end=' - ')
print(f'A soma entre os {len(soma)} números pares digitados é {sum(soma)}')

s = p = 0
for i in range(6):
	n = int(input('Digite um valor: '))
	if n % 2 == 0:
		s += i
		p += 1
print(f'A soma entre os {p} números pares digitados é {s}')