# Exercício Extra Python #22.4 - Inspetor Dinâmico de Módulos com dir(), getattr() e callable() - Aula 00 até 22 - Mundo 3
# Nível: Intermediário/Avançado
#
# Importe um módulo nativo do Python (ex: 'string' ou 'math').
# Percorra todos os nomes retornados por dir(modulo), ignore os que começam com '_'
# e separe em duas listas usando getattr(modulo, nome) e callable(obj):
# 1) Lista de Constantes/Atributos (não chamáveis)
# 2) Lista de Funções/Métodos (chamáveis - callable)
#
# Exemplo de execução esperada:
#   Módulo 'math' -> Constantes (5): ['e', 'inf', 'nan', 'pi', 'tau']
#   Módulo 'math' -> Funções (60): ['acos', 'acosh', 'asin', ...]
#
# Dica: A função built-in callable(obj) retorna True se o objeto for uma função/classe e False se for um dado/constante!
