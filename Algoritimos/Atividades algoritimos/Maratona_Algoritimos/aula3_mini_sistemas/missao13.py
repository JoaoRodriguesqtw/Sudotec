#sistema de login com o while

cadastro_user = input("cadastre o seu user: ")
cadastro_senha = input("cadastre a sua senha: ") # cria variaveis que seram o cadastro da senha e do user
print()

login_user = input("digite seu user: ")
login_senha = input("digite sua senha: ") #variavel que irá pedir o nome de user e senha ao usuario

while login_user != cadastro_user or login_senha != cadastro_senha: #enquanto login user não ser cadastro user ou login senha não ser cadastro senha irá se repetir
  print("User e ou senha incorretos, tente novamente") #print informando que o usuario errou a senha
  print()
  login_user = input("digite seu user: ")
  login_senha = input("digite sua senha: ") #variaveis iguais às que estão fora do while que irão pedir o nome de user e senha ao usuario

print()
print("Login efetuado com sucesso!") #print informando que o login foi efetuado