# Exercício Python #124 - Encapsulamento em Conta de Banco Digital - Aula 25
# Crie uma classe ContaBancaria com titular público, mas com __numero_conta e __saldo estritamente privados.
# Crie métodos getter e setter protegidos (ou @property):
# - depositar(valor): valida se o valor é positivo antes de somar.
# - sacar(valor): valida se o valor é positivo e se há saldo suficiente.
# - consultar_saldo(): retorna o saldo formatado.
# Tente acessar __saldo diretamente por fora da classe para comprovar que o atributo está encapsulado.
