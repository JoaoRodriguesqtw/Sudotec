def impar_par (a): #função para verificar se é par ou impar
    if a % 2 ==0: # se a divido por 2 ter resto 0 é impar
        return ("é par")
    return("é impar") #caso de earn return, cujo caso o numero não se adeque a estrutura if já irá cair no return ("é impar")

print()
li_num = int(input("digite o numero que você quer verificar se é par ou impar: ")) #variavel que ira armazenar o numero escolhido
print()
print(impar_par(li_num)) # print que irá chamar a função para verificar se o numero é par ou impar