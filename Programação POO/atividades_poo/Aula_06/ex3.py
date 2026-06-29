class Estudante:
    def __init__(self, nome, matricula, nota_inicial=0):
        self.__nome = nome
        self.__matricula = matricula
        self.__nota = nota_inicial
    
    def get_nome(self):
        print("getter nome funcionando")
        return self.__nome


    def set_nome(self, novo_nome):
        # Valida e depois atribui
         if len(novo_nome) == 0:
             raise ValueError("nome não deve ficar vazio")
         print("setter novo nome funcionando")
         self.__nome = novo_nome
         

    def get_matricula(self):
        print("getter matricula funcionando")
        return self.__matricula
    

    # def set_matricula(self, nova_matricula):
    #     if len(nova_matricula) == 0:
    #         raise ValueError ("matricula não deve ficar vazia")
    #     print("setter matricula funcionando")
    #     self.__matricula = nova_matricula

        

    def get_nota(self):
        print("getter nota funcionando")
        return self.__nota
        

    def set_nota(self, nova_nota):

        
        if  nova_nota < 0 or nova_nota > 10:
            raise ValueError ("nota invalida")



estudante = Estudante("Ana", "2024001", 7.5)
print()
# Getters funcionam:
print(estudante.get_nome())       # Ana
print(estudante.get_matricula())  # 2024001
print(estudante.get_nota())       # 7.5

print()
# Setters com validação funcionam:
estudante.set_nome("Ana Silva")
estudante.set_nota(9.0)
print(estudante.get_nota())       # 9.0

print()

