ld_livros = {}
list_livros_copy = []
ja_existe = False


while True:
    print()
    print("--Seja bem vindo ao sistema da biblioteca--")
    print()
    print("--Digite 1 para fazer uma reserva de livro --")
    print("--Digite 2 para fechar o sistema --")
    print()
    li_opcao = int(input("Digite o numero da sua escolha: "))
    print()

    if li_opcao == 1:
        print()
        ld_livros["Livro"] = input("Digite o nome do livro: ").lower()
        ld_livros["aluno"] = input("Digite o nome do aluno: ").lower()

        novo_livro = ld_livros["Livro"] 
        novo_aluno = ld_livros["aluno"]

        for reserva in list_livros_copy:
            if reserva["aluno"] == novo_aluno:
                ja_existe = True
                break
        
        if ja_existe == True:
            print("error: um aluno não pode reservar o mesmo livro duas vezes")

        else:
            list_livros_copy.append(ld_livros.copy())
        print()
            
        for m in list_livros_copy:
            for v in m.values():
                print(v, end = " | ")
            print()

    elif li_opcao == 2:
        print("finalizando sistema")
        break
    
    else:
        print("error: opção desconhecida")

        

        