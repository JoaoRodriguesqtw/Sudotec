import math


def IsPrimo (n):
    if n < 2:
        return False
    else: 
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True 
    

numero = int(input("Digite o numero que você quer verificar se é primo: "))

if IsPrimo(numero):
    print(f"{numero} é primo")
else: 
    print(f"{numero} não é primo")