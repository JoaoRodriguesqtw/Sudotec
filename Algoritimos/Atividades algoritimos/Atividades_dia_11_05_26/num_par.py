# Faça um programa que leia 10 números e informe quantos são pares e ímpares.
numeros = []
pares = []
impares = []


print()
li_quantos_numeros = int(input("digite quantos numeros você quer verificar se impar ou par: "))
print()

for x in range(li_quantos_numeros):
    numero = int(input(f"digite o {x+1}° numero que voce quer verificar se é par ou impar: "))
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)
    numeros.append(numero)
    # calculo_Impar_par(numero)

print()
print(f"dentre os {len(numeros)}, {len(pares)} são pares e {len(impares)} são impares")
print()

