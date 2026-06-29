print()
print("seja bem vindo ao conversor de moedas!")
print("escolha como quer usar o conversor")
print("digite 1 para converter real para dolar")
print("digite 2 para converter dolar para real")
print()
while True:
    print()
    ls_qual_modo = int(input("digite em qual modo você quer usar o conversor: "))
    print()
    li_cotacao = 5

    if ls_qual_modo == 1:
        print("Modo real para dolar escolhido")
        print()
        lf_quantidade_em_reais = float(input("digite quantos reais você quer converter para dolar: "))
        lf_quantidade_em_dolar = lf_quantidade_em_reais/li_cotacao
        print(f"{(lf_quantidade_em_reais):.2f} reais são {(lf_quantidade_em_dolar):.2f} dolares")

    elif ls_qual_modo == 2:
        print("Modo dolar para real escolhido")
        print()
        lf_quantidade_em_dolar = float(input("digite quantos dolares você quer converter para real: "))
        lf_quantidade_em_real = lf_quantidade_em_dolar*li_cotacao
        print(f"{(lf_quantidade_em_dolar):.2f} dolares são {(lf_quantidade_em_real):.2f} reais")
    elif ls_qual_modo == 0:
        print("desligando conversor")
        break
