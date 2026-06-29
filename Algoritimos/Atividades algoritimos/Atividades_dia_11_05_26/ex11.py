# 11. Desenvolva um algoritmo que gere a tabuada completa de um número.

qual_tabuada = int(input("digite qual numero voce quer ver a tabuada: "))

ate_qual_numero = int(input("digite até onde voce quer ver a tabuada: "))

for x in range(ate_qual_numero):
    print(f"{qual_tabuada} X {x+1} = {qual_tabuada * (x+1)}")