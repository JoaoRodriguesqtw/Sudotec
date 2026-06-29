from Personagem import Personagem

class Mago(Personagem):
    def __init__(self,nome,ataque,vida,mana):
        super().__init__(nome,ataque,vida)
        self.mana = mana
    
    
    def atacar(self,alvo):
        alvo.receber_dano(self.ataque)
        print(f"o {Mago} atacou com uma bola de fogo")