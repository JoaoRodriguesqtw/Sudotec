#classe filha que por meio da herança recebe os atributos já existentes na classe pai

from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque, armadura):
        super().__init__(nome, vida, ataque) #metodo super chama o construtor da classe pai e faz necessario definir apenas o novo atributp
        self.armadura = armadura


    def atacar(self, alvo): #o def atacar da classe guerreiro sobreescreve a da classe pai a personalizando-a, isso é polimorfismo
        if self.esta_vivo():
            super().atacar(alvo)
            print(f"{self.nome} atacou {alvo.nome} com sua espada, causando {self.ataque} de dano.")
        else:
            print(f"{self.nome} não pode atacar porque está morto.")




    def receber_dano(self, quantidade): #o def receber_dano da classe guerreiro sobreescreve a da classe pai a personalizando-a e adicionando o novo atributo armadura, cujo serve para diminuir o dano recebido, isso é polimorfismo
        dano_reduzido = max(0, quantidade - self.armadura)
        super().receber_dano(dano_reduzido)
        print(f"{self.nome} tem armadura de {self.armadura}, então o dano foi reduzido para {dano_reduzido}.")