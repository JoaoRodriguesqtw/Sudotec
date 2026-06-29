class Validadores: #classe que ira agrupar o metodo estático que ira verificar a senha

    @staticmethod
    def valida_senha(senha):
        quantidade = len(senha) #variavel que irá armazenar quantidades de caracteres que tem na senha

        if quantidade >= 8: #se quantidade de caracteres for maior ou igual a 8 irá retornar senha valida
            return ("senha valida ")
        return ("senha invalida, sua senha deve ter pelo menos 8 digitos") #caso não, irá retornar senha invalida, pelo caso de earn return



class Senhas: #classe que ira criar o objeto que será cada senha
    def __init__(self,senha): 
        self.senha = senha
        
ls_senha1 = Senhas(input("digite sua senha: ")) # instancia do objeto senha 1 cujo ira pedir para o usuario digitar sua senha

print(Validadores.valida_senha(ls_senha1.senha)) #print cujo irá chamar o metodo estatico valida_senha com om atributo senha do objeto ls_senha1
