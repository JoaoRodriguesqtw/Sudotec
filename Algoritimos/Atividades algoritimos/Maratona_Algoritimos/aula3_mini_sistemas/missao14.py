saldo_total = 500.00

while True:
    print()
    print(f" o saldo atual é de {saldo_total}") #imprime p saldo total sempre que while 
    print()
    print("--digite 1 para adicionar saldo --")
    print("--digite 2 para sacar  --")
    print("--digite 3 para fechar o programa--")
    print()
    li_opcao = int(input("digite o numero da opção escolida: ")) #variavel que irá armazenar a opção escolhida
    print()

    if li_opcao == 1: # estrutura if para adicionar saldo
        adicionar_saldo = float(input("digite quanto de saldo voce quer adicionar: "))
        saldo_total += adicionar_saldo #+= irá sempre adicionar o valor de "adicionar_saldo" ao saldo_total
    
    elif li_opcao == 2: #estrutura if para sacar um valor do saldo
        saque = float(input("digite quanto de saldo voce quer sacar: "))
        if saque > saldo_total: #estrutura if para tratar de caso o valor desejado seja maior que o saldo total da conta
            print("erro, saldo insuficiente ")
        else:
            saldo_total -= saque #se o valor desejado de saque for menor que o saldo total -= ira sempre retirar o valor desejado do saldo total
    
    elif li_opcao == 3: #estrutura if para a opção de fechar o sistema
        print("fechando sistema")
        break #break para parar o codigo