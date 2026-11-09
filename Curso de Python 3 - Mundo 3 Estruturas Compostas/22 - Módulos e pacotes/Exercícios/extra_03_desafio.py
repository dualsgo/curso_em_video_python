# Exercício Extra Python #22.3 - Validador de Dados de Entrada Reutilizável (CPF, E-mail e Telefone) - Aula 00 até 22 - Mundo 3
# Nível: Intermediário
#
# Construa 3 funções de validação booleana (retornam True ou False) prontas para serem importadas:
# 1) validar_email(email: str) -> bool (deve ter '@' e '.' após o '@')
# 2) validar_cpf_formato(cpf: str) -> bool (após remover '.' e '-', deve ter 11 dígitos numéricos)
# 3) validar_telefone(tel: str) -> bool (deve ter 10 ou 11 dígitos numéricos)
#
# Exemplo de execução esperada:
#   validar_email('contato@site.com') -> True
#   validar_cpf_formato('123.456.789-01') -> True
#
# Dica: Em POO, essas funções costumam virar métodos estáticos (@staticmethod) de validação!
