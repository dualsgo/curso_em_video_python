# Exercício Extra Python #10.3 - Roteador de Comandos com match / case (Python 3.10+) - Aula 00 até 10 - Mundo 1
# Nível: Intermediário
#
# Leia uma sigla de operação financeira ('PIX', 'TED', 'DOC', 'BOLETO').
# Use a estrutura match / case para informar o tempo de compensação:
# - 'PIX': Instantâneo (24h)
# - 'TED' | 'DOC': Mesmo dia útil (até 17h)
# - 'BOLETO': Até 3 dias úteis
# - Qualquer outro (case _): Operação desconhecida
#
# Exemplo de execução esperada:
#   Digite a modalidade: ted
#   Prazo de compensação: Mesmo dia útil (até 17h).
#
# Dica: O case _: funciona como o else padrão do match/case.
