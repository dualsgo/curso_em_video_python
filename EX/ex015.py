# DESAFIO 015: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

qtde_dias = int(input('Quantidade de dias alugados: '))
km_percorrido = float(input('Quantidade de km percorrido: '))

valor_km = km_percorrido * 0.15
valor_diaria = qtde_dias * 60

valor_final = valor_km + valor_diaria

print(f'{'NOTA FISCAL':^30}')
print('=' * 30)
print(f'{'DIAS':<5} {qtde_dias:^7} | R$ {valor_diaria:>10.2f}')
print(f'{'KM':<5} {km_percorrido:^7.2f} | R$ {valor_km:>10.2f}')
print('=' * 30)
print(f'{'TOTAL':<12}  | R$ {valor_final:>10.2f}')