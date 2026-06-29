li_numeros = []

li_quantos_nums = int(input("digite quantos numeros voce quer registar: "))

for x in range(li_quantos_nums):
    li_numero = int(input(f"digite o {x + 1}° numero: "))
    li_numeros.append(li_numero)

print(f"o maior numero da lista é: {max(li_numeros)} e o menor é: {min(li_numeros)}")