# DESAFIO 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = input('Digite o seu nome completo: ').strip().title()
nome_dividido = nome_completo.split()
primeiro_nome, ultimo_nome = nome_dividido[0], nome_dividido[-1]

print(f'{'Você digitou:':<15}{nome_completo:>{len(nome_completo)}}')
print(f'{'Primeiro nome:':<15}{primeiro_nome:.<{len(nome_completo)}}')
print(f'{'Último nome:':<15}{ultimo_nome:.>{len(nome_completo)}}')