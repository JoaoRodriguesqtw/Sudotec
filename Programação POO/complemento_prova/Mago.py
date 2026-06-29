#classe filha que por meio da herança recebe os atributos já existentes na classe pai

from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome, vida, ataque, mana):
        super().__init__(nome, vida, ataque) #metodo super chama o construtor da classe pai e faz necessario definir apenas o novo atributo
        self.mana = mana

    def atacar(self, alvo):  #o def atacar da classe mago sobreescreve a da classe pai a personalizando-a e adicionando novas funcionalidades, isso é polimorfismo
        if self.esta_vivo():
            if self.mana >= 10:
                super().atacar(alvo)
                self.mana -= 10
                print(f"{self.nome} lançou um feitiço em {alvo.nome} causando {self.ataque} de dano. Mana restante: {self.mana}.")
            else:
                print(f"{self.nome} não tem mana suficiente para atacar.")
        else:
            print(f"{self.nome} não pode atacar porque está morto.")