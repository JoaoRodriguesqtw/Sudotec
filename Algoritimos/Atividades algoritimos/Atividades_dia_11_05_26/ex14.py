candidato1 = []
candidato2 = []


for x in range (10):
    print("-- Digite 1 para votar no candidato 1 -- ")
    print("-- Digite 2 para votar no candidato 2 -- ")
    print()
    li_opcao = int(input("digite o numero do candidato escolhido: "))

    if li_opcao == 1:
        candidato1.append(li_opcao+1)
    elif li_opcao == 2:
        candidato2.append(li_opcao+1)

print(f"o candidato 1 teve {len(candidato1)} votos e o candidato 2 teve {len(candidato2)} votos")

