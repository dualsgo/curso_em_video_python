# DESAFIO 024: Crie um programa que leia o nome de uma cidade diga se
# ela começa ou não com o nome "SANTO".

cidade = input('Digite sua cidade: ').strip().title()
primeiro_nome = cidade.split()[0]
print('O primeiro nome É Santo 'if primeiro_nome == 'Santo' else 'O primeiro nome NÃO é Santo')