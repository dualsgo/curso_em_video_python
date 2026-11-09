# Exercício Python #126 - Polimorfismo com Sistema de Pagamentos - Aula 25
# Crie uma superclasse FormaDePagamento com o método processar_pagamento(valor).
# Crie três subclasses que implementam comportamentos polimórficos diferentes para o mesmo método:
# 1 - PagamentoCartao: aplica taxa de 3% e exibe autorização na operadora.
# 2 - PagamentoBoleto: gera código de barras e adiciona R$ 1,50 de taxa bancária.
# 3 - PagamentoPix: aplica 5% de desconto promocional e gera QRCode fictício.
# Itere por uma lista de pagamentos diferentes executando processar_pagamento() polimorficamente.
