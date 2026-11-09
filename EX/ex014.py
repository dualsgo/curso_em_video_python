# DESAFIO 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura_c = float(input('Digite a temperatura em °C '))
temperatura_f = (temperatura_c * 9/5) + 32


print(f'Celsius: {temperatura_c} °C\nFahrenheit: {temperatura_f} °F')