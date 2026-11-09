# Exercício Extra Python #22.5 - Formatador de Relatórios em Tabelas ASCII Reutilizável - Aula 00 até 22 - Mundo 3
# Nível: Avançado
#
# Crie um conjunto de funções de interface de terminal:
# - linha(tam=42, char='-') -> str
# - cabecalho(titulo, tam=42) -> str
# - tabela_chave_valor(dicionario, tam=42) -> None (imprime cada par alinhado com pontos)
# Teste exibindo um relatório completo de sistema usando apenas chamadas a essas funções.
#
# Exemplo de execução esperada:
#   ------------------------------------------
#               RELATÓRIO DE SISTEMA          
#   ------------------------------------------
#   Processador......................: Ryzen 7
#   Memória RAM......................:   16 GB
#
# Dica: Note como separar a formatação visual da lógica de negócio deixa o programa principal muito mais limpo!
