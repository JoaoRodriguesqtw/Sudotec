# Exercício 1 — Construtor alternativo simples

# Enunciado:
# Crie uma classe Produto com os atributos:
# - nome
# - preco

# A classe deve permitir criar objetos de duas formas:

# 1. Forma normal:
# Produto("Notebook", 3500)

# 2. A partir de uma string:
# Produto.from_string("Notebook,3500")

# Requisitos:
# - Criar um método de classe from_string
# - A string virá no formato: "nome,preco"
# - Converter o preço para float
# - Retornar uma instância da classe

class Produtos:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    
    def exibir(self):
        print(f"{self.nome}|{self.preco}")

    @classmethod
    def from_string(cls,string):
        data_split = string.split(",")

        nome = data_split[0]
        preco = data_split[1]

        return cls(nome,preco)



produto1 = Produtos.from_string("Notebook,3500")
print(produto1.nome, produto1.preco)






