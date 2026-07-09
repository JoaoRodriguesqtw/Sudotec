from Veiculos import veiculos

class moto(veiculos):
    def empinar(self):
        return("a moto esta empinando")


moto1 = moto("suzuki", 1980)

print()
print(moto1.apresentar())
print(moto1.ligar_veiculo)
print(moto1.empinar())
print()