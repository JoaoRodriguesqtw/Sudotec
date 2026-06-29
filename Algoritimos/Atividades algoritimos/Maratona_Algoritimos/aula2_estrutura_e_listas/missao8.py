ls_lista_compras = [] #criação da lista de compras

while True: #wilhe true para fazer com que o codigo se repita até que o usuario decida finalizar o programa
    print() 
    print('--seja bem vindo à lista de compras--') #inicio do menu do sistema de listas
    print() 
    print("--digite 1 para adicionar itens a lista--")
    print("--digite 2 para remover itens da lista--")
    print("--digite 3 para vizualizar a lista--")
    print("--digite 4 para fechar o programa--")
    print()
    li_opcao = int(input("digite o numero da opção escolida: ")) #variavel que irá armazenar a opção escolhida
    print()

    if li_opcao == 1: # estrutura if para a opção de adicionar itens a lista
        ls_item = input("digite o item cujo você quer adicionar na lista: ").lower() #variavel para adicionar o item escolhido, .lower é utilizado para manter um padrão de digitação
        ls_lista_compras.append(ls_item) #adiciona o item na lista
    
    elif li_opcao == 2:# estrutura if para a opção de remover itens a lista
        ls_item = input("digite o item cujo você quer remover na lista: ").lower() #variavel para remover o item escolhido, .lower é utilizado para manter um padrão de digitação
        ls_lista_compras.remove(ls_item) #.remove() remove o item armazenado na variavel ls_item

    elif li_opcao == 3: #estrutura if para a opção de visualizar a lista
        print(ls_lista_compras) #printa a lista

    elif li_opcao == 4: #estrutura if para a opção de fechar o sistema
        print("fechando sistema")
        break #break para parar o codigo

    else: #else para tratar de opções cujo não sejam as 4 predefinidas
        print("error: opção desconhecida") #error para informar que esta opção não é conhecida
