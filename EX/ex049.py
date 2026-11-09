# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Digite a tabuada que deseja visualizar: '))
for i in range(1, 11):
	print(f'{tabuada:2}{'x':^3}{i:2}{'=':^3}{i*tabuada:2}')