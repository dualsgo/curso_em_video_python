# Exercício Extra Python #20.3 - Construtor de Perfil de Usuário com **kwargs - Aula 00 até 20 - Mundo 3
# Nível: Intermediário
#
# Crie uma função criar_perfil(nome: str, email: str, **extras) -> dict:
# que receba o nome e e-mail obrigatórios e qualquer quantidade de informações extras nomeadas
# (ex: cidade='São Paulo', profissao='Dev', nivel='Junior').
# A função deve juntar tudo em um único dicionário e retorná-lo.
#
# Exemplo de execução esperada:
#   criar_perfil('Ana', 'ana@email.com', cargo='Engenheira', remoto=True)
#   {'nome': 'Ana', 'email': 'ana@email.com', 'cargo': 'Engenheira', 'remoto': True}
#
# Dica: O parâmetro **kwargs captura todos os argumentos nomeados extras em um dicionário!
