from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self,nome,ataque,vida,armadura):
        super().__init__(nome,ataque,vida)
        self.armadura = armadura

        def atacar(self,alvo):
            alvo.receber_dano(self.ataque)
            print(f"o {Guerreiro} atacou com a espada")
