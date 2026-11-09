# DESAFIO 043: Desenvolva uma lógica que leia o peso e a
# altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = round(peso / (altura ** 2), 1)
categoria = ('Abaixo do peso' if imc < 18.5 else 'Peso ideal' if imc < 25 else 'Sobrepeso' if imc < 30 else 'Obesidade' if imc < 40 else 'Obesidade mórbida')
print(f'{'IMC':^10}|{'CATEGORIA':^20}\n{'-'*30}\n{imc:^10.1f}|{categoria:^20}')