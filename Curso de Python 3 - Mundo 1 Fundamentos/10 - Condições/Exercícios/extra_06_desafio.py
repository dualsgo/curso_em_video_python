# Exercício Extra Python #10.6 - Guardião de Estado de um Objeto Conta (Pré-POO) - Aula 00 até 10 - Mundo 1
# Nível: Desafio Pré-POO
#
# Em POO, os métodos de um objeto protegem seus atributos contra estados inválidos (Encapsulamento).
# Simule uma conta com saldo_atual = 500.0 e status_conta = 'ATIVA' (ou 'BLOQUEADA').
# Leia o valor de um saque e valide todas as regras antes de autorizar:
# 1) A conta deve estar 'ATIVA'
# 2) O valor do saque deve ser maior que zero
# 3) O valor não pode ultrapassar o saldo_atual
#
# Exemplo de execução esperada:
#   Saldo: R$ 500.00 | Status: ATIVA | Valor do saque: R$ 600.00
#   [RECUSADO] Saldo insuficiente! Faltam R$ 100.00.
#
# Dica: Em uma classe ContaBancaria, essa lógica ficará dentro do método sacar(self, valor).

# Tarefa 1: Definir saldo_atual = 500.0 e ler o status da conta e o valor do saque.


# Tarefa 2: Criar as validações condicionais protegendo o saldo de ficar negativo.


# Tarefa 3: Exibir o novo saldo caso aprovado ou o motivo exato do bloqueio.

