valor_meses = {}
valor_meses_copy = []


for dics in range (3):
    print()
    valor_meses["Nome"] = input("Digite o mes: ")
    valor_meses["recebidos"] = int(input("Digite o valor recebido do mês: "))
    valor_meses["gastos"] = int(input("digite o gasto do mes: "))
    valor_meses["lucro"] = valor_meses["recebidos"] - valor_meses["gastos"]

    valor_meses_copy.append(valor_meses.copy())

print()
for m in valor_meses_copy:
        for v in m.values():
            print(v, end = " | ")
        print()
