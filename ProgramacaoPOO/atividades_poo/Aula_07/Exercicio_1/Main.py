from Carro import carro
from Moto import moto
from Caminhao import caminhao

def main():

    moto1 = moto("suzuki", 1980)

    print()
    print(moto1.apresentar())
    print(moto1.ligar_veiculo)
    print(moto1.empinar())
    print()

    carro1 = carro("honda",2000)

    print()
    print(carro1.apresentar())
    print(carro1.ligar_veiculo())
    print(carro1.abrir_porta_malas())
    print()


    caminhao1 = caminhao("mercedes", 1992)


    print()
    print(caminhao1.apresentar())
    print(caminhao1.ligar_veiculo())
    print(caminhao1.engatar_reboque())
    print()

main()