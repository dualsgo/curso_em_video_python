# DESAFIO 017: Faça um programa que leia:
# o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print(f'CATETO OPOSTO - {cateto_oposto}')
print(f'CATETO ADJACENTE - {cateto_adjacente}')
print(f'HIPOTENUSA - {hipotenusa:.2f}')