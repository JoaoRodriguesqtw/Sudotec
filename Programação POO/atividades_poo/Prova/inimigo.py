from Personagem import Personagem

class Inimigo(Personagem):
    def __init__(self,nome,ataque,vida):
        super().__init__(nome,ataque,vida)
    
    
    def atacar(self,alvo):
        alvo.receber_dano(self.ataque)
        print(f"o {Inimigo} atacou")