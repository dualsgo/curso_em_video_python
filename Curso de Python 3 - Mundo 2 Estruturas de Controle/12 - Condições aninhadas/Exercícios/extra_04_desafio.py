# Exercício Extra Python #12.4 - Simulador de Frete Internacional por Peso e Região - Aula 00 até 12 - Mundo 1
# Nível: Intermediário/Avançado
#
# Leia o peso de uma encomenda (kg) e o continente de destino (1-América, 2-Europa, 3-Ásia).
# Se o peso for <= 0 ou > 50 kg, recuse o envio.
# Caso contrário, dentro de cada continente, aplique uma taxa diferente para pacotes leves (<= 5kg)
# e pesados (> 5kg).
#
# Exemplo de execução esperada:
#   Peso: 8.0 kg | Destino: 2 (Europa)
#   Envio autorizado! Custo total do frete internacional: R$ 320.00
#
# Dica: Aninhar a validação de peso por fora evita repetir a mesma checagem em cada continente.
