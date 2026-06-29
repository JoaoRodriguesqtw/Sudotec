# Exercício 4: Sistema de Cadastro de Produtos em Loja

# Em lojas físicas ou e-commerces, produtos são cadastrados com informações básicas. Alguns dados são essenciais (nome e preço), mas outros podem ter valores padrão caso não sejam informados no momento do cadastro.
# Requisitos:

# O construtor deve exigir apenas nome e preco
# categoria deve ter valor padrão "Geral"
# estoque deve ter valor padrão 0

# Crie três instâncias:

# Uma passando só nome e preço
# Outra passando nome, preço e categoria
# Outra passando todos os parâmetros


# Implemente exibir_info(self) que mostra todos os atributos do produto

class Produtos:
    def __init__(self,nome, preco, categoria="geral" ,estoque=0,): 
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque =estoque
        
    
    def exibir_info(self):
        print(f"nome do produto: {self.nome} | preço: {(self.preco):.2f} | estoque: {self.estoque} | categoria: {self.categoria} | está disponivel?: {self.esta_disponivel()} ")

    def esta_disponivel (self):
        disponibilidade = self.estoque > 0
        return disponibilidade
print() 
produto1 = Produtos(input("digite o nome do produto: "), float(input("digite o valor do produto: ")))
print()
produto2 = Produtos(input("digite o nome do produto: "), float(input("digite o valor do produto: ")), input("digite qual a categoria do item: "))
print()
produto3 = Produtos(input("digite o nome do produto: "), float(input("digite o valor do produto: ")), input("digite qual a categoria do item:  ") , int(input("digite quantas unidades do produtos estão em estoque: ")))       
print()

produto1.exibir_info()
produto2.exibir_info()
produto3.exibir_info()
print()

# #print(f"o {produto1.nome} está disponivel?: {produto1.esta_disponivel()}")
# print(f"o {produto2.nome} está disponivel?: {produto2.esta_disponivel()}")
# print(f"o {produto3.nome} está disponivel?: {produto3.esta_disponivel()}")
