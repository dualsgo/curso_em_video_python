# Exercício Extra Python #20.5 - Conversor Universal de Moedas com Tabela de Cotações Nomeada - Aula 00 até 20 - Mundo 3
# Nível: Avançado
#
# Crie uma função converter_moeda(valor_brl: float, moeda_destino: str = 'USD', **cotacoes_customizadas) -> float:
# A função deve ter cotações padrão internas ({'USD': 5.0, 'EUR': 5.5, 'GBP': 6.3}),
# mas permitir que o usuário sobrescreva ou adicione novas moedas via **cotacoes_customizadas.
#
# Exemplo de execução esperada:
#   converter_moeda(100, 'USD') -> 20.00
#   converter_moeda(100, 'ARS', ARS=0.006) -> 16666.67
#
# Dica: Combinar valores padrão com **kwargs é um padrão muito usado em bibliotecas profissionais do Python.

# Tarefa 1: Criar o dicionário de cotações padrão dentro da função.


# Tarefa 2: Atualizar com cotacoes_customizadas usando .update().


# Tarefa 3: Retornar o valor convertido (ou None se a moeda não existir).

