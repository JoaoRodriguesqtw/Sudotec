# Crie uma classe Retangulo com atributos largura e altura recebidos no __init__. 

# Implemente dois métodos: 
# - calcular_area(self) que retorna a área
# - calcular_perimetro(self) que retorna o perímetro. 

# Crie dois retângulos diferentes e exiba os resultados de ambos.

class Retangulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    
    def calc_area(self):
        return self.altura * self.largura
    
    def calc_perimetro(self):
        return (self.altura + self.largura) * 2


print()
retangulo1 = Retangulo(float(input("digite a altura do 1° retangulo: ")),float(input("digite a largura do 1° retangulo: ")))
print()
retangulo2 = Retangulo(float(input("digite a altura do 2° retangulo: ")),float(input("digite a largura do 2° retangulo: ")))


print()
print(f"o retangulo1 tem uma area de: {retangulo1.calc_area()} e um perimetro de: {retangulo1.calc_perimetro()}")
print(f"o retangulo2 tem uma area de: {retangulo2.calc_area()} e um perimetro de: {retangulo2.calc_perimetro()}")
print()