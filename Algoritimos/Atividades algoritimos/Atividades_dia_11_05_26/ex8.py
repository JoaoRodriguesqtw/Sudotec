
cadastro_user = input("cadastre o seu user: ")
cadastro_senha = input("cadastre a sua senha: ")
print()

login_user = input("digite seu user: ")
login_senha = input("digite sua senha: ")

while login_user != cadastro_user or login_senha != cadastro_senha:
  print("User e ou senha incorretos, tente novamente")
  print()
  login_user = input("digite seu user: ")
  login_senha = input("digite sua senha: ")

print()
print("Login efetuado com sucesso!")