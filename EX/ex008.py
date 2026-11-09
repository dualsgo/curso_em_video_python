# DESAFIO 008: Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

metros = float(input('Valor em metros: '))
print('Equivalem a...')
print(f'{'quilômetros':<15}{metros / 1000:>15}{'km':>5}')
print(f'{'hectômetros':<15}{metros / 100:>15}{'mh':>5}')
print(f'{'decâmetros':<15}{metros / 10:>15}{'dam':>5}')
print(f'{'metros':<15}{metros:>15}{'mm':>5}')
print(f'{'decímetros':<15}{metros * 10:>15.0f}{'dm':>5}')
print(f'{'centímetros':<15}{metros * 100:>15.0f}{'cm':>5}')
print(f'{'milímetros':<15}{metros * 1000:>15.0f}{'mm':>5}')