# Exercício Extra Python #17.6 - Histórico de Transações Independente com .copy() (Pré-POO) - Aula 00 até 17 - Mundo 3
# Nível: Desafio Pré-POO
#
# Em POO, quando um objeto retorna uma lista interna (ex: extrato bancário), devemos retornar uma CÓPIA
# para evitar que código externo bagunce os dados internos do objeto.
# Crie extrato_interno = [100.0, -20.0, 50.0]. Gere extrato_para_exibicao = extrato_interno.copy(),
# ordene e remova negativos apenas na cópia, e comprove que extrato_interno permaneceu intacto na ordem original.
#
# Exemplo de execução esperada:
#   Extrato filtrado/ordenado (cópia): [50.0, 100.0]
#   Extrato original no banco (intacto): [100.0, -20.0, 50.0]
#
# Dica: Se fizéssemos apenas extrato_exibicao = extrato_interno, qualquer alteração apagaria os dados reais da conta!
