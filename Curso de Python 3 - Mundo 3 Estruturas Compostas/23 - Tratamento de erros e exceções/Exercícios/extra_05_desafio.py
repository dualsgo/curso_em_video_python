# Exercício Extra Python #23.5 - Sua Primeira Classe Completa: Produto em Estoque (Desafio POO 1) - Aula 00 até 23 - Mundo 3
# Nível: Avançado / Ponte POO
#
# Baseado na seção 'Ponte para POO' do notebook erros.ipynb, crie uma classe chamada Produto:
# - No método __init__(self, nome: str, preco: float, estoque: int = 0), inicialize os 3 atributos.
# - Crie o método repor(self, qtd: int) que soma ao estoque (levantando ValueError se qtd <= 0).
# - Crie o método vender(self, qtd: int) que desconta do estoque (se houver saldo suficiente).
# - Crie o método exibir_etiqueta(self) que imprime nome, preço, estoque e valor total parado.
#
# Exemplo de execução esperada:
#   p1 = Produto('Notebook', 3500.0, 5)
#   p1.vender(2) -> Venda realizada! Estoque restante: 3
#   p1.exibir_etiqueta() -> Notebook | R$ 3500.00 | 3 un. (Total: R$ 10500.00)
#
# Dica: Lembre-se: 'self' sempre é o primeiro parâmetro dos métodos e refere-se ao próprio objeto que chamou o método!

# Tarefa 1: Declarar class Produto: com __init__, repor, vender e exibir_etiqueta.


# Tarefa 2: Instanciar 2 produtos diferentes (p1 e p2).


# Tarefa 3: Chamar os métodos de cada objeto dentro de um bloco try/except.

