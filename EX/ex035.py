# DESAFIO 035: Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o valor da reta A '))
b = float(input('Digite o valor da reta B '))
c = float(input('Digite o valor da reta C '))

print(f'{'LADO A':<10}{a:>5}')
print(f'{'LADO B':<10}{b:>5}')
print(f'{'LADO C':<10}{c:>5}')


# a soma de cada dois lados deve ser sempre maior que a medida do terceiro lado
print(f'Formam' if a + b > c and a + c > + b and b + c > a else 'Não '
																 'formam',
	  'um triangulo!')