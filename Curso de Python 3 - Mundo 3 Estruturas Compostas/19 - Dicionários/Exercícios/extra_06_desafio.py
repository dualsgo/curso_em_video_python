# Exercício Extra Python #19.6 - Dicionário como Protótipo de Objeto Bancário (Pré-POO) - Aula 00 até 19 - Mundo 3
# Nível: Desafio Pré-POO
#
# Em Python, todo objeto guarda seus atributos internamente em um dicionário (__dict__).
# Represente uma conta bancária como um dicionário:
# conta = {'titular': 'Douglas', 'saldo': 1000.0, 'limite': 500.0, 'historico': []}
# Simule 2 depósitos e 1 saque atualizando o 'saldo' e registrando cada operação na lista 'historico'.
# No final, exiba os atributos e o extrato de 'historico'.
#
# Exemplo de execução esperada:
#   Titular: Douglas | Saldo Atual: R$ 1150.00
#   Histórico: ['+R$ 300.00', '+R$ 100.00', '-R$ 250.00']
#
# Dica: Quando você criar uma classe Conta em POO, self.titular e self.saldo serão exatamente essas chaves!

# Tarefa 1: Criar o dicionário conta com as 4 chaves.


# Tarefa 2: Realizar operações validando se o saque não ultrapassa (saldo + limite).


# Tarefa 3: Adicionar strings descritivas em conta['historico'].append(...) e exibir o resumo.

