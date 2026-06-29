ls_nome = input("digite seu nome: ")
li_idade = int(input("digite a sua idade: "))
print()
nota = []

li_quantas_notas = int(input("digite quantas notas quer lançar?: "))
print()
for x in range (li_quantas_notas):
    notas = float(input(f"digite a {x + 1} nota: "))
    nota.append(notas)

soma = sum(nota)

lf_media = soma/len(nota)

print()
print(f"seu nome é {ls_nome}, você tem {li_idade} e a sua media final é {(lf_media):.1f}")
