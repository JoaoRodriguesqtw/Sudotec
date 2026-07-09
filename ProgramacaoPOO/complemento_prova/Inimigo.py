#classe filha que por meio da herança recebe os atributos já existentes na classe pai
from Personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque) #metodo super chama o construtor da classe pai e nestre caso não tem necessidade de definir novos atributos, e os herdados são chamados pelo metodo super

    def atacar(self, alvo):
        if self.esta_vivo(): #o def atacar da classe inimigo sobreescreve a da classe pai a personalizando-a, isso é polimorfismo
            alvo.receber_dano(self.ataque)
            print(f"{self.nome} morde {alvo.nome} causando {self.ataque} de dano.")
        else:
            print(f"{self.nome} não pode atacar porque está morto.")