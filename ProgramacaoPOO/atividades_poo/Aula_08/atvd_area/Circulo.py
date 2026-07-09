from Classe_area import Forma
import math

class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio

    
    def area(self):
        print(f"{math.pi * (self.raio ** 2):.1f}")