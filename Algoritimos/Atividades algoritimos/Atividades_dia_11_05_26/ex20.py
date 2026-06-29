# 20. Desenvolva um sistema bancário simples com depósito e saque.

saldo = 00.00

while True:
    print()
    print("--Bem vindo À tela inicial--")
    print("--Digite 1 para realiar depositos--")
    print("--Digite 2 para realizar saques--")
    print("--Digite 3 para visualizar saldo--")
    print("--Digite 4 para sair--")
    print()

    li_opcao = int(input("digite o numero da opção desejada: "))

    if li_opcao == 1:
        print()
        deposito = float(input("digite quanto voce deseja depositar na conta: "))

        saldo += deposito
        print(f"o novo saldo é de: {saldo}")
        print()
    elif li_opcao == 2:
        print()
        saque = float(input("digite quanto voce deseja sacar da conta: "))
        if saque > saldo:
            print()
            print("error: saldo insuficiente")
            print()
        else:
            saldo -= saque
            print(f"o novo saldo é de: {saldo}")
            print()
    elif li_opcao == 3:
        print(f"o saldo atual é de: {saldo}")
    elif li_opcao == 4:
        print("saindo do sistema bancario")
        break