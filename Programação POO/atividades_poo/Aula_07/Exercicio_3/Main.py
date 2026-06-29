from Estudante import Estudante
from Professor import Professor
from Pessoa import Pessoa

def main():

    # criação e apresentação da pessoa normal
    print()
    pessoa_normal = Pessoa("Fernando", 22)
    print(pessoa_normal.apresentar())

    #
    print()
    Estudante1 = Estudante("Gabriella", 16, "ADS")
    print(Estudante1.apresentar())
    print()

    Professor1 = Professor("Ângelo", 22, "Backend")
    print(Professor1.apresentar())
    print()

main()
