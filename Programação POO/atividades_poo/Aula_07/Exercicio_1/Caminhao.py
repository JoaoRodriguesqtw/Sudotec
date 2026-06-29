from Veiculos import veiculos

class caminhao(veiculos):
    def engatar_reboque(self):
        return("reboque engatado")
    
caminhao1 = caminhao("mercedes", 1992)


print()
print(caminhao1.apresentar())
print(caminhao1.ligar_veiculo)
print(caminhao1.engatar_reboque())
print()