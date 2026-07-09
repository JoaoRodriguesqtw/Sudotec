#não prescisei re-escrever depositar() na poupança pois como já o havia declarado na classe pai, apenas o chamei na classe filha diminuindo o codigo, isto é possivel por causa da Herança entre classes pai e filhas






from conta import Conta
from conta_poupanca import Conta_poupanca
from conta_salario import Conta_salario

def main():

    print()
    conta1 = Conta_poupanca("ana", 500)
    conta1.depositar = float(input("digite o valor de deposito: "))
    print(conta1.ver_saldo)
    print(conta1.render_juros(0.05))
    print(conta1.ver_saldo)
    print()

    print("DESAFIO OPCIONAL")

    conta2 = Conta_salario("joao",500)
    print()
    print(conta2.ver_saldo)
    print(conta2.receber_salario(float(input("digite o valor de deposito: "))))
    print(conta2.ver_saldo)
    print()


main()


