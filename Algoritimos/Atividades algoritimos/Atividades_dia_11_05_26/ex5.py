# Desenvolva um algoritmo que leia notas até o usuário encerrar e mostre a média geral.

notas = []

nota = float(input("digite a primeira nota: "))

while True :
    nota = float(input(f"digite as notas nota: "))
    

    if nota <= 0:
        break
    notas.append(nota)
    
if len(notas) > 0:
    media = sum(notas)/len(notas)  
    print(f"a media de tudo é {media}")
else:
    print("nada foi digitado")

    