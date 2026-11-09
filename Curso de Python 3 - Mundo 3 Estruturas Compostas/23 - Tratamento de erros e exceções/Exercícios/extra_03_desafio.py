# Exercício Extra Python #23.3 - Diário de Bordo em Arquivo de Texto com with open() ('a' e 'r') - Aula 00 até 23 - Mundo 3
# Nível: Intermediário
#
# Crie um programa que permita adicionar uma nova anotação em um arquivo 'diario.txt'
# usando with open('diario.txt', 'a', encoding='utf-8') as f:.
# Em seguida, leia e exiba todas as linhas já salvas no arquivo numerando-as,
# tratando FileNotFoundError caso a leitura seja feita antes do arquivo existir.
#
# Exemplo de execução esperada:
#   Digite sua anotação: Estudei manipulação de arquivos e POO!
#   --- Histórico do Diário ---
#   01: Estudei manipulação de arquivos e POO!
#
# Dica: O gerenciador de contexto 'with open(...) as f:' garante o fechamento automático do arquivo!

# Tarefa 1: Ler a anotação do usuário.


# Tarefa 2: Abrir 'diario.txt' no modo 'a' (append) com encoding='utf-8' usando o bloco with.


# Tarefa 3: Abrir 'diario.txt' no modo 'r' (read) e exibir todas as linhas com enumerate().

