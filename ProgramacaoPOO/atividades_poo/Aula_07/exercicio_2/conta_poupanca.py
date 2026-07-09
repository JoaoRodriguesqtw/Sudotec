from conta import Conta

class Conta_poupanca(Conta):


    def render_juros (self, taxa):
        rendimento = self.puxar_saldo * taxa
        self.depositar = rendimento
        return(f"juros de {rendimento} aplicados, novo saldo é de {self.puxar_saldo}")


