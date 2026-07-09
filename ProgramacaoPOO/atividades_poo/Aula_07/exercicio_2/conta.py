class Conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def ver_saldo(self):
        return (f"saldo de {self.titular}: {self.__saldo}")
    
    @property
    def puxar_saldo(self):
        return self.__saldo


    @property
    def depositar(self):
        return self.__saldo

    @depositar.setter
    def depositar(self, valor):
        if valor > 0:
            
            self.__saldo += valor
            return(f"deposito de {valor} realizado, o novo saldo é de:{self.depositar} ")
        else:
            raise ValueError ("o valor deve ser maior que 0")
        
