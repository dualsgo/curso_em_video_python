# Exercício Extra Python #20.4 - Evitando a Armadilha do Parâmetro Padrão Mutável (lista=None) - Aula 00 até 20 - Mundo 3
# Nível: Intermediário/Avançado
#
# Crie uma função registrar_log(mensagem: str, historico: list = None) -> list:
# Se 'historico' não for passado (for None), crie uma nova lista vazia dentro da função.
# Adicione a mensagem à lista e retorne-a.
# Demonstre que chamar registrar_log('Erro 1') e depois registrar_log('Erro 2') sem segundo argumento
# cria duas listas separadas e não acumula indevidamente!
#
# Exemplo de execução esperada:
#   Chamada 1 isolada: ['Erro 1']
#   Chamada 2 isolada: ['Erro 2']
#   Chamada passando lista existente: ['Erro 1', 'Erro 3']
#
# Dica: Revisite a seção sobre Parâmetros Padrão Mutáveis adicionada em funcoes.ipynb!
