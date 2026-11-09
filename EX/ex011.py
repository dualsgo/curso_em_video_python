# DESAFIO 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura

litro_tinta = 2
quantidade = area / litro_tinta
print(f'Para pintar sua parede de {largura}m por {altura}m\nQue possui uma '
	  f'área de {area:.2f}m²\nSerão necessários {quantidade:.2f}L de tinta.')