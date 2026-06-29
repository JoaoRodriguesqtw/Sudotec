# Desenvolva um algoritmo que calcule o fatorial de um número usando repetição.

def fatorial (n):
    resultado = 1
    for x in range(1, n + 1):
        resultado *= x
    return resultado


numero = int(input("digite um numero: "))

print(f"o fatorial de {numero} é {fatorial(numero)}")

