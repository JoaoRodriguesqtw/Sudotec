# Em sistemas web, usuários podem se cadastrar com poucos ou muitos dados. Crie uma classe Usuario onde alguns campos são obrigatórios e outros têm valores padrão para quem não os informar.

# O construtor deve exigir apenas nome e email

# cargo deve ter valor padrão "Visitante" e ativo deve ter valor padrão True

# Crie três instâncias: uma passando só nome e email, outra passando cargo, outra passando todos os parâmetros

# Implemente apresentar(self) que exibe todos os atributos

class Usuarios:
    def __init__(self,nome,email,cargo="visitante", ativo=True,numero=1123456789):
        self.nome = nome
        self.email = email
        self.ativo = ativo
        self.cargo = cargo
        self.numero = numero

    def apresentar(self):
        print(f"nome de usuario: {self.nome}| email: {self.email}| está ativo?: {self.ativo}| cargo: {self.cargo}| numero de telefone: {self.numero}")
print()
user1 = Usuarios(input("digite seu nome: "), input("digite seu email: "))
print()
user2 =  Usuarios(input("digite seu nome: "),input("digite seu email: "), input("digite seu cargo: "))
user3 = Usuarios("Gabriella","Gabriellanoara@gmail.com","CEO",False,"4691024816")

print()
user1.apresentar()
user2.apresentar()
user3.apresentar()
print()