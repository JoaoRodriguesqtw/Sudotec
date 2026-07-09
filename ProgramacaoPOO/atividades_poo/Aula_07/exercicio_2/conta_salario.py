from conta import Conta

class Conta_salario(Conta):

    def receber_salario(self, valor):
        self.depositar = valor
        return(f"salario de {valor} depositado")
    

