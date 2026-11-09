# Exercício Extra Python #12.6 - Máquina de Estados de um Pedido de E-commerce (Pré-POO) - Aula 00 até 12 - Mundo 1
# Nível: Desafio Pré-POO
#
# Objetos em POO frequentemente mudam de estado seguindo regras estritas (State Machine).
# Leia o estado atual de um pedido ('AGUARDANDO_PAGAMENTO', 'PAGO', 'ENVIADO', 'ENTREGUE', 'CANCELADO')
# e a ação desejada ('PAGAR', 'ENVIAR', 'ENTREGAR', 'CANCELAR').
# Valide se a transição é permitida (ex: só pode 'ENVIAR' se estiver 'PAGO'; não pode 'CANCELAR' se já foi 'ENTREGUE').
#
# Exemplo de execução esperada:
#   Estado atual: AGUARDANDO_PAGAMENTO | Ação: ENVIAR
#   [TRANSIÇÃO INVÁLIDA] Não é possível enviar um pedido que ainda não foi pago!
#
# Dica: Em POO, cada ação dessas ('pagar', 'enviar', 'cancelar') será um método da classe Pedido!
