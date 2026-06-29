#Aqui esta a classe pai, tem os criterios basicos cujo seram herdados pelas classes filhas

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.__vida = vida #vida é um atributo privado, para controlar o acesso a ele, isto é uma demonstração de encapsulamento
        self.ataque = ataque

    @property  #decorado cujo cria um metodo getter para acessar o atributo privado __vida
    def vida(self):
        return self.__vida

    @vida.setter  #decorado cujo cria um metodo setter para controlar o acesso ao atributo privado __vida,o qual também garante que a vida nunca seja negativa
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    def esta_vivo(self):
        if self.vida > 0:
            return True
        return False

    def receber_dano(self, quantidade):
        self.vida -= quantidade

    def atacar(self, alvo):
        if self.esta_vivo():
            alvo.receber_dano(self.ataque)
            if not alvo.esta_vivo():
                print(f"{alvo.nome} foi derrotado!")
        else:
            print(f"{self.nome} não pode atacar porque está morto.")