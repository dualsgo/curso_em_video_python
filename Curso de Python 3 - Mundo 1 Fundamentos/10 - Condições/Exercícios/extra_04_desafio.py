# Exercício Extra Python #10.4 - Detector de Ano Bissexto e Validador de Data Simples - Aula 00 até 10 - Mundo 1
# Nível: Intermediário/Avançado
#
# Leia um dia (1 a 31), um mês (1 a 12) e um ano.
# Verifique se a data existe no calendário considerando a quantidade real de dias de cada mês
# (meses 4, 6, 9, 11 têm 30 dias; mês 2 tem 29 dias se o ano for bissexto ou 28 se não for; demais têm 31).
#
# Exemplo de execução esperada:
#   Dia: 29 | Mês: 2 | Ano: 2025
#   Data inválida! 2025 não é bissexto, portanto fevereiro tem apenas 28 dias.
#
# Dica: Verifique primeiro se o mês está entre 1 e 12 antes de validar o dia.

# Tarefa 1: Ler dia, mês e ano como inteiros.


# Tarefa 2: Calcular se o ano é bissexto: (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0).


# Tarefa 3: Determinar o máximo de dias do mês informado e validar se 1 <= dia <= max_dias.

