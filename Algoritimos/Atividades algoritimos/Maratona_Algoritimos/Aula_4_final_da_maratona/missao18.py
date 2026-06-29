# Controle de estoque

# Criação de um dicionário para armazenar os produtos e suas quantidades.
ld_produtos = {
} # o dicionário é inicialmente vazio, mas os produtos e suas quantidades serão adicionados conforme o usuário interagir com o programa. 


while True: # laço de repetição para permitir que o usuário realize várias operações até decidir sair do programa.
    
    # exibe o estoque atual, mostrando cada produto e sua quantidade.
    print("\nEstoque atual:") # o "\n" é utilizado para criar uma nova linha.
    for produto, quantidade in ld_produtos.items(): # o método items() é utilizado para obter os itens do dicionário correspondente.
        print(f"{produto}: {quantidade}") # aqui é exibido o nome do produto e a quantidade correspondente.
    print()

    # aqui foi utilizado uma série de prints para mostrar as opções disponíveis para o usuário com clareza, e deixar o programa mais organizado e fácil de usar.
    print("Digite a operação que deseja realizar:") # o usuário é orientado a escolher uma ação pré-definida, onde cada uma delas resulta em uma operação diferente.
    print("1 - Adicionar produto") # o usuario pode adicionar um produto ao estoque.
    print("2 - Remover produto") # o usuario pode remover um produto do estoque.
    print("3 - Verificar estoque") # o usuario pode verificar o estoque atual.
    print("4 - Sair") # o usuario encerra o programa.
    li_opcao = int(input("Opção: ")) 

    if li_opcao == 1: # caso o usuário escolha a opção 1 a seguinte operação será realizada:
        ls_produto = input("\nDigite o nome do produto que deseja adicionar: ").lower() # o usuario informa qual produto deseja adicionar ao estoque
        li_quantidade = int(input("Digite a quantidade do produto: ")) # logo em seguida informa a quantidade desse produto que vai ir para o estoque
        if ls_produto in ld_produtos: # o programa verifica se o produto já existe no estoque.
            ld_produtos[ls_produto] += li_quantidade # se o produto já existir, a quantidade informada é adicionada à quantidade existente no estoque
        else:
            ld_produtos[ls_produto] = li_quantidade # se o produto não existir, ele é adicionado ao dicionário com a quantidade informada
        print(f"Produto '{ls_produto}' adicionado com sucesso! Quantidade atual: {ld_produtos[ls_produto]}") # o programa confirma que o produto foi adicionado com sucesso e exibe a quantidade atual do produto

    elif li_opcao == 2: # caso o usuário escolha a opção 2 a seguinte operação será realizada:
        ls_produto = input("\nDigite o nome do produto que deseja remover: ").lower() # o usuario informa qual produto deseja remover do estoque
        if ls_produto in ld_produtos: # o programa verifica se o produto existe no estoque
            li_quantidade = int(input("Digite a quantidade do produto a ser removida: ")) # o usuario informa a quantidade do produto que deseja remover do estoque
            if li_quantidade <= ld_produtos[ls_produto]: # o programa verifica se a quantidade a ser removida é menor ou igual à quantidade disponível no estoque
                ld_produtos[ls_produto] -= li_quantidade # se a quantidade a ser removida for válida, ela é subtraída da quantidade atual do produto no estoque
                print(f"Produto '{ls_produto}' removido com sucesso! Quantidade atual: {ld_produtos[ls_produto]}") #o codigo ira imprimir a a confirmacao de que o produto foi removido com sucesso e exibe a quantidade atual do produto no estoque
            else:
                print(f"Quantidade insuficiente em estoque. Quantidade atual de '{ls_produto}': {ld_produtos[ls_produto]}") # se a quantidade a ser removida for maior do que a quantidade disponível no estoque, o programa exibe uma mensagem de erro.
        else:
            print(f"Produto '{ls_produto}' não encontrado no estoque.") # se o produto informado para remoção não existir no estoque, o programa exibe uma mensagem de erro.

    elif li_opcao == 3: # caso o usuário escolha a opção 3 a seguinte operação será realizada:
        print("\nEstoque atual:") # o programa exibe o estoque atual, mostrando cada produto e sua quantidade.
        for produto, quantidade in ld_produtos.items(): # o método items() é utilizado para obter os itens do dicionário correspondente, e exibe o nome do produto e a quantidade correspondente.
            print(f"\n{produto}: {quantidade}") # exibe o nome do produto e a quantidade correspondente.

        if not ld_produtos: # se o dicionário de produtos estiver vazio o programa exibe uma mensagem de alerta
            print("O estoque está vazio.")

    elif li_opcao == 4: # caso o usuário escolha a opção 4 a seguinte operação será realizada:
        print("\nEncerrando o programa. Até mais!") # o programa exibe uma mensagem de despedida e encerra o programa utilizando o comando break.
        break # encerra o loop, e consequentemente o programa.