class Casa:
    def __init__(self,material,cor,qtd_comodos):
        self.material =  material
        self.cor = cor
        self.qtd_comodos = qtd_comodos

casa1 = Casa("madeira","rosa",5)
casa2 = Casa("concreto", "roxa",8)
casa3 = Casa("tijolo","cinza",4)


class Pessoa:
    def __init__(self,kg,cor,tam
                 ):
        self.kg = kg
        self.cor = cor
        self.tam = tam


pessoa1 = Pessoa(40,"amarela",1.80)
pessoa2 = Pessoa(20,"rosa",1.60)
pessoa3 = Pessoa(55,"branca",1.77)


print(pessoa1.kg)
print(f"{pessoa1.tam}")


pessoa1.kg = 77

print(pessoa1.kg)
        