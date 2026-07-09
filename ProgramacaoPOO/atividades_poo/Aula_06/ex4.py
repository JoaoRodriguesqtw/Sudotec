# ═══════════════════════════════════════════════════════════════════════════════
# EXERCÍCIO 4 - Criar Getters e Setters com @property (Forma Pythônica)
# ═══════════════════════════════════════════════════════════════════════════════
# ═══════════════════════════════════════════════════════════════════════════════

# INSTRUÇÕES:
# 1. Complete a classe abaixo adicionando @property e @atributo.setter
# 2. Os atributos privados (com __) já estão definidos
# 3. Use @property para o getter e @atributo.setter para o setter
# 4. Valide os dados no setter
# 5. Crie propriedades read-only quando apropriado (sem setter)

# ═══════════════════════════════════════════════════════════════════════════════

# EXERCÍCIO: Classe Livro
# ────────────────────────

# A classe abaixo representa um livro de uma biblioteca. Complete-a com properties:

# class Livro:
#     def __init__(self, titulo, autor, paginas, ano_publicacao):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__paginas = paginas
#         self.__ano_publicacao = ano_publicacao
#         self.__emprestimos = 0
    
#     # COMPLETE AQUI - Adicione as properties:
#     # 1. @property titulo - getter
#     # 2. @titulo.setter - setter com validação
#     # 3. @property autor - getter
#     # 4. @autor.setter - setter com validação
#     # 5. @property paginas - getter
#     # 6. @paginas.setter - setter com validação
#     # 7. @property emprestimos - getter (SEM setter, só incrementa)
#     # 8. metodo registrar_emprestimo() - incrementa emprestimos

# ═══════════════════════════════════════════════════════════════════════════════

# REQUISITOS PARA OS SETTERS:

#  titulo (property com setter):
#    - Valide se não está vazio
#    - Levante ValueError se estiver vazio
#    - Exemplo de erro: "Título não pode estar vazio!"

#  autor (property com setter):
#    - Valide se não está vazio
#    - Valide se é uma string
#    - Levante ValueError se inválido
#    - Exemplo de erro: "Autor deve ser um texto não vazio"

#  paginas (property com setter):
#    - Valide se é um inteiro
#    - Valide se é maior que 0
#    - Levante ValueError se inválido
#    - Exemplo de erro: "Páginas deve ser um número maior que 0"

#  emprestimos (property SEM setter):
#    - Apenas retorna o valor
#    - Não deve haver @emprestimos.setter
#    - Só pode ser alterado pelo método registrar_emprestimo()

# ═══════════════════════════════════════════════════════════════════════════════

# EXEMPLO DE USO (como você espera que funcione):

# livro = Livro("1984", "George Orwell", 328, 1949)

# # Getters funcionam (parecem atributos comuns!):
# print(livro.titulo)           # 1984
# print(livro.autor)            # George Orwell
# print(livro.paginas)          # 328
# print(livro.emprestimos)      # 0

# # Setters funcionam (também parecem atributos comuns!):
# livro.titulo = "1984 - Edição Especial"
# livro.paginas = 330
# print(livro.titulo)           # 1984 - Edição Especial
# print(livro.paginas)          # 330

# # Setters rejeitam valores inválidos:
# livro.titulo = ""             #  ValueError: Título não pode estar vazio!
# livro.paginas = -50           #  ValueError: Páginas deve ser...
# livro.autor = 12345           #  ValueError: Autor deve ser...

# # emprestimos é read-only:
# print(livro.emprestimos)      # 0
# livro.registrar_emprestimo()
# print(livro.emprestimos)      # 1
# livro.emprestimos = 100       #  AttributeError: can't set attribute

# ═══════════════════════════════════════════════════════════════════════════════

# ESTRUTURA DO QUE VOCÊ PRECISA ESCREVER:

# Complete a classe com essas properties (escreva o código completo):



    
#     # COMPLETE AQUI - Adicione as properties:
#     # 1. @property titulo - getter
#     # 2. @titulo.setter - setter com validação
#     # 3. @property autor - getter
#     # 4. @autor.setter - setter com validação
#     # 5. @property paginas - getter
#     # 6. @paginas.setter - setter com validação
#     # 7. @property emprestimos - getter (SEM setter, só incrementa)
#     # 8. metodo registrar_emprestimo() - incrementa emprestimos

class Livro:
    def __init__(self, titulo, autor, paginas, ano_publicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas
        self.__ano_publicacao = ano_publicacao
        self.__emprestimos = 0

    @property
    def titulo(self):
        # Retorna o título
        print("getter titulo funcionando")
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if len(novo_titulo) == 0:
            raise ValueError ("o titulo não deve ficar vazio")
        print("setter titulo funcionando")
        self.__titulo = novo_titulo

    @property
    def autor(self):
        print("getter autor funcionando")
        return self.__autor
    

    @autor.setter
    def autor(self, novo_autor):
        if novo_autor == "":
            raise ValueError ("o autor não deve ficar vazio")
        if not isinstance(novo_autor,str):
            raise ValueError ("autor deve ser do tipo texto")
        print("setter autor funcionando")
        self.__autor = novo_autor
    

    @property
    def paginas(self):
        print("getter paginas funcionando")
        return self.__paginas

    @paginas.setter
    def paginas(self, novas_paginas):
        if novas_paginas < 0:
            raise ValueError ("o numero de paginas deve ser maior que zero")
        print("setter paginas funcionando")
        self.__paginas = novas_paginas

    @property
    def emprestimos(self):
        
        print("getter emprestimos funcionando")
        return self.__emprestimos
    

    def registrar_emprestimo(self):
        self.__emprestimos += 1
        print(f"total de emprestimos: {self.emprestimos}")



livro = Livro("1984", "George Orwell", 328, 1949)
print()
# Getters funcionam (parecem atributos comuns!):
print(livro.titulo)           # 1984
print(livro.autor)            # George Orwell
print(livro.paginas)          # 328
print(livro.emprestimos)      # 0

print()
# Setters funcionam (também parecem atributos comuns!):
livro.titulo = "1984 - Edição Especial"
livro.paginas = 330
print(livro.titulo)           # 1984 - Edição Especial
print(livro.paginas)          # 330


print()

# Setters rejeitam valores inválidos:
# livro.titulo = ""             #  ValueError: Título não pode estar vazio!
# livro.paginas = -50           #  ValueError: Páginas deve ser...
# livro.autor = 12345           #  ValueError: Autor deve ser...

print()
# emprestimos é read-only:
print(livro.emprestimos)      # 0
livro.registrar_emprestimo()
print(livro.emprestimos)      # 1
# livro.emprestimos = 100       #  AttributeError: can't set attribute
