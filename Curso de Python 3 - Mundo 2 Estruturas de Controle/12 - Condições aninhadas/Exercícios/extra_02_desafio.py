# Exercício Extra Python #12.2 - Sistema de Triagem Hospitalar (Protocolo de Manchester) - Aula 00 até 12 - Mundo 1
# Nível: Básico/Intermediário
#
# Leia a temperatura corporal (float), se há falta de ar ('S'/'N') e o nível de dor (0 a 10).
# Classifique a pulseira de atendimento:
# - VERMELHA (Emergência): falta de ar == 'S' OU temperatura >= 40.0 OU dor >= 9
# - AMARELA (Urgente): temperatura >= 38.5 OU dor >= 6
# - VERDE (Pouco Urgente): temperatura >= 37.5 OU dor >= 3
# - AZUL (Não Urgente): demais casos.
#
# Exemplo de execução esperada:
#   Temperatura: 38.8 | Falta de ar: N | Dor: 4
#   Classificação: PULSEIRA AMARELA (Atendimento Urgente)
#
# Dica: Em triagens, sempre verificamos os casos críticos primeiro no topo do if!
