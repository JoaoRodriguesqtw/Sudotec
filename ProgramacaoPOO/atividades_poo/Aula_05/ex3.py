
# Crie uma classe Validador com um método estático que:

# recebe uma senha
# retorna True se ela tiver pelo menos 8 caracteres
# retorna False caso contrário




class Validadores:

    @staticmethod
    def valida_senha(senha):
        caracteres = senha
        quantidade = len(caracteres)

        if quantidade >= 8:
            return True
        return False



class Senhas:
    def __init__(self,senha):
        self.senha = senha
        
senha1 = Senhas(input("digite sua senha: "))

print(Validadores.valida_senha(senha1.senha))



