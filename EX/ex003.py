# DESAFIO 003: Crie um programa que leia dois números e mostre a soma entre
# eles.

print(f'{' CALCULADORA ':=^30}')
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
soma = primeiro_numero + segundo_numero
print(f'{' RESULTADO ':=^30}')
print(f'{primeiro_numero:>30}\n+{segundo_numero:>29}\n{'-' * 30}\n{soma:>30}')