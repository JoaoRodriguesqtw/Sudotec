class Produtos:
    def __init__(self,nome,preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque =  estoque

    def exibir_ficha (self):
        print(f"ficha do produto -- nome: {self.nome} | preço: {(self.preco):.2f} | estoque: {self.estoque}  ")

    
    def esta_disponivel (self):
        return self.estoque > 0
 

print()
produto1 = Produtos(input("digite o nome do produto: "), float(input("digite o valor do produto: ")), int(input("digite quantas unidades do produtos estão em estoque: ")))

produto2 = Produtos("mouse Gamer", 189.00, 0)

print()
produto1.exibir_ficha()
produto2.exibir_ficha()
print()

print(f"o {produto1.nome} está disponivel?: {produto1.esta_disponivel()}")
print(f"o {produto2.nome} está disponivel?: {produto2.esta_disponivel()}")
print()