#Crie um sistema que leia vários alunos e mostre o aluno com maior média.

# ls_nome_alunos = []
# lf_medias = []

# li_quantidade_alunos = int(input("digite quantos alunos voce quer cadastrar a nota: "))
# li_quantas_notas = int(input("digite quantas notas voce quer cadastrar por aluno: "))

# for num_alunos in range (li_quantidade_alunos):
#     lf_notas = []
#     print()
#     ls_nomes = input(f"digite  o nome do {num_alunos + 1} aluno: ")
#     print()
#     ls_nome_alunos.append(ls_nomes)
#     for x in range(li_quantas_notas):
#         lf_nota = float(input(f"digite a {x + 1} nota do {ls_nome_alunos[num_alunos]} "))
#         lf_notas.append(lf_nota)
#         #lf_media = sum(lf_notas)/len(lf_notas)
#        # lf_medias.append(lf_media)
#     lf_media = sum(lf_notas)/len(lf_notas)
#     lf_medias.append(lf_media)
#     print(f"a média do {ls_nome_alunos[num_alunos]} é {lf_media} ")

# map(ls_nome_alunos,lf_medias)



# print()
# print(f"o aluno")

nome_e_medias = {}


li_quantidade_alunos = int(input("digite quantos alunos voce quer cadastrar a nota: "))
li_quantas_notas = int(input("digite quantas notas voce quer cadastrar por aluno: "))

for li_num_alunos in range(li_quantidade_alunos):
    print()
    nome= input(f"digite o nome do {li_num_alunos + 1}° aluno: ")
    print()
    notas = []
    for x in range (li_quantas_notas):
       
       nota= float(input(f"digite a {x + 1} nota do {nome}: "))
       notas.append(nota)
    media = sum(notas)/len(notas)
    nome_e_medias[nome] = media


print("o aluno com a maior média é: ", max(nome_e_medias, key=nome_e_medias.get))
        


