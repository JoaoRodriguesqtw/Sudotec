lf_nota = []

print()
li_quantos_alunos = int(input("informe para quantos alunos quer lançar notas: "))
li_quantas_notas = int(input(f"digite quantas você quer lançar para cada aluno: "))
print()

for x in range(li_quantos_alunos ):
    for y in range (li_quantas_notas):
        print()
        lf_notas = float(input(f"digite a {y + 1} nota do aluno {x + 1}: "))
        print()
        lf_nota.append(lf_notas)

    media = sum(lf_nota)/len(lf_nota)
    print(f"a media do aluno {x + 1} é {(media):.1f}")
    






