# Exercício Extra Python #09.6 - Demonstração de Imutabilidade e Encadeamento de Métodos (Pré-POO) - Aula 00 até 09 - Mundo 1
# Nível: Desafio Pré-POO
#
# Em POO, métodos que não alteram o objeto original retornam um NOVO objeto, permitindo encadear chamadas
# (Method Chaining), como: texto.strip().lower().replace(' ', '_').
# Leia o título de um artigo (ex: '  Introdução à Orientação a Objetos  ') e gere um 'slug' de URL
# (ex: 'introducao-a-orientacao-a-objetos') encadeando métodos, mostrando que o título original permanece intacto.
#
# Exemplo de execução esperada:
#   Título original: '  Aprendendo Python 3 no Curso em Vídeo  '
#   Slug gerado    : 'aprendendo-python-3-no-curso-em-video'
#   Original mudou?: False (continua igual pois str é imutável)
#
# Dica: Cada ponto (.) chama um método sobre o novo objeto string retornado pelo método anterior!
