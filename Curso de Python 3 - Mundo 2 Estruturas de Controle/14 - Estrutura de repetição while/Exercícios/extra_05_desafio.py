# Exercício Extra Python #14.5 - Autenticador com Bloqueio por Tentativas e while / else - Aula 00 até 14 - Mundo 1
# Nível: Avançado
#
# Defina uma senha secreta (ex: 'python123'). O usuário tem no máximo 3 tentativas.
# Use um laço while tentativas < 3 com o ramo else do próprio while:
# - Se acertar a senha, dê boas-vindas e encerre o laço.
# - Se esgotar as 3 tentativas sem acertar, o bloco else do while deve exibir 'CONTA BLOQUEADA POR SEGURANÇA!'.
#
# Exemplo de execução esperada:
#   Tentativa 1/3 - Senha: 123 (Incorreta!)
#   Tentativa 2/3 - Senha: abc (Incorreta!)
#   Tentativa 3/3 - Senha: xyz (Incorreta!)
#   CONTA BLOQUEADA POR SEGURANÇA!
#
# Dica: Lembre-se: o else de um loop while só é executado se o loop terminar normalmente (sem break)!
