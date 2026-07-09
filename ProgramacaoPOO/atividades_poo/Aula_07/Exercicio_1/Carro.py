from Veiculos import veiculos

class carro(veiculos):
    def quantas_portas (self):
        portas = 4
        print(f"o carro tem {portas} portas")
    
    def abrir_porta_malas(self):
        return("porta malas aberto")

carro1 = carro("honda",2000)

print()
print(carro1.apresentar())
print(carro1.ligar_veiculo())
print(carro1.abrir_porta_malas())
print()
