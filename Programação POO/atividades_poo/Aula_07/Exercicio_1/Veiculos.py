class veiculos:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def apresentar(self):
        return (f"a marca é {self.marca} e ano é {self.ano}")
    
    def ligar_veiculo(self):
        return(f"Veiculo ligado")


