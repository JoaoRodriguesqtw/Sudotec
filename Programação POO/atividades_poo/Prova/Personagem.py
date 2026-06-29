class Personagem:
    def __init__(self,nome,ataque,vida):

        self.nome = nome
        self.ataque = ataque
        self.__vida = vida
       # self.IsDead = IsDead
    
    @property
    def vida(self):
        return (f"{Personagem}| Vida:{self.__vida} | vivo: {self.esta_vivo}")
    
    @vida.setter
    def vida(self):
        if self.vida < 0:
            self.vida = 0
            print("nenhum personagem pode ter vida negativa")

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False
    
    @property
    def receber_dano(self,quantidade):
        self.vida = self.vida - quantidade
        return(f"{self.Personagem} perdeu {self.quantidade} de vida")

    def atacar(self,alvo,quantidade):
        alvo.receber_dano(self.ataque,self.quantidade)
        print(f"o {self.nome} recebeu {self.quantidade} de dano de {self.Personagem}")

    
        
        