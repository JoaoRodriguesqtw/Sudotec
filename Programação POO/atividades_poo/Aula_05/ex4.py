# Crie uma classe Matematica com um método estático que:

# recebe um número
# retorna o quadrado desse número

class Calculos:

    @staticmethod
    def calculo_quadrado (a):
        resultado = a **2
        return resultado
    
class Numero:

    def __init__(self,num):
        self.num = num

num1 = Numero(int(input("Digite o numero à ser multiplicado ao quadrado: ")))

print(f"o resultado é: {Calculos.calculo_quadrado(num1.num)}")
