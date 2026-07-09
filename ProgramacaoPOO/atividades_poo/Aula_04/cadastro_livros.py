# Exercício 2: Sistema de Cadastro de Livros em Biblioteca
# Bibliotecas precisam catalogar livros com informações essenciais. O título e autor são obrigatórios, mas outros dados podem ser preenchidos depois ou ter valores padrão.
# Requisitos:

# O construtor deve exigir apenas titulo e autor
# ano_publicacao deve ter valor padrão 2024
# genero deve ter valor padrão "Não classificado"
# emprestado deve ter valor padrão False
# Crie três instâncias:

# Uma passando só título e autor
# Outra passando título, autor e ano de publicação
# Outra passando todos os parâmetros


# Implemente mostrar_detalhes(self) que exibe todos os atributos do livro

class  Livros:
    def __init__(self,titulo="",autor="",genero="não classificado",ano_publicacao=2024,emprestado=False):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_publicacao =ano_publicacao
        self.emprestado = emprestado

    # def esta_emprestado (self):
        
    #     esta_emprestado = input("Digite se o livro está emprestado: ").lower()

    #     if esta_emprestado == "sim": 
    #         return True
    #     else:
    #         return False
        
    def cadastro (self):
        print()
        while True:
            self.titulo = input("digite o titulo do livro: ")
            self.autor = input("digite o nome do autor do livro: ")

            if self.titulo.strip() and self.autor.strip():
                self.genero = input("digite o genero do livro: ")
                self.ano_publicacao = int(input("digite o ano de pubicação: "))
                self.emprestado = emprestado = input("Digite se o livro está emprestado: ").lower()
                self.emprestado = True if emprestado == "sim" else False
                print()


                break
            else:
                print()
                print("Estes campos não podem ficar vazio, escreva novamente")
                print()
                


    def exibir_ficha_livro(self):
        
        print(f"Titulo: {self.titulo} | autor: {self.autor} | genero: {self.genero} | ano de publicação: {self.ano_publicacao} | o livro está emprestado? {self.emprestado}")
        

livro1 = Livros("O Hobbit", "Tolkien")
livro2 = Livros("Duna", "Frank Herbert", 1965)
livro3 = Livros()

livro3.cadastro()


livro1.exibir_ficha_livro()
livro2.exibir_ficha_livro()
livro3.exibir_ficha_livro()
print()