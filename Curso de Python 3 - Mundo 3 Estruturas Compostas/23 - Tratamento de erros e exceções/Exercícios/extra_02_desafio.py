# Exercício Extra Python #23.2 - Validação de Regra de Negócio Levantando Exceções com raise - Aula 00 até 23 - Mundo 3
# Nível: Básico/Intermediário
#
# Crie uma função cadastrar_idade(nome: str, idade: int) -> dict:
# - Se 'nome' estiver vazio, levante ValueError('O nome não pode ser vazio!').
# - Se 'idade' não for int, levante TypeError('A idade deve ser um número inteiro!').
# - Se 'idade' < 0 ou > 130, levante ValueError('Idade fora do limite humano (0 a 130)!').
# No programa principal, chame a função dentro de um try/except exibindo a mensagem do erro (except Exception as e:).
#
# Exemplo de execução esperada:
#   Tentando cadastrar ('', 25) -> Erro capturado: O nome não pode ser vazio!
#   Tentando cadastrar ('Ana', -5) -> Erro capturado: Idade fora do limite humano (0 a 130)!
#
# Dica: Em POO, os construtores (__init__) e setters usam 'raise ValueError(...)' exatamente assim para proteger atributos!
