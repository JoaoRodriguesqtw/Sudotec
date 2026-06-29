nome_e_medias = {} #criação do dicionario que irá armazenar os nomes e as médias

# inputs que irão definir quantos alunos o sistema irá usar as notas e quantas notas serão lançadas
li_quantidade_alunos = int(input("digite quantos alunos voce quer cadastrar a nota: "))
li_quantas_notas = int(input("digite quantas notas voce quer cadastrar por aluno: "))

for li_num_alunos in range(li_quantidade_alunos): #laço for que irá utilizar se repetira pelo valor armazenado em (li_quantidade_alunos)
    print()
    nome= input(f"digite o nome do {li_num_alunos + 1}° aluno: ") #irá perguntar o nome do aluno que terá a nota lançada
    print()
    notas = [] #cria a lista notas
    for x in range (li_quantas_notas): #laço que ira se repetir pelo valor armazenado em li_quantas_notas para perguntar as notas de cada aluno, como o laço está dentro do 1°
       
       nota= float(input(f"digite a {x + 1} nota do {nome}: ")) #irá perguntar as notas do aluno
       notas.append(nota) #irá adicionar as notas na lista nota
    media = sum(notas)/len(notas) #irá calcular a media das notas dentro da lista nota
    nome_e_medias[nome] = media #irá adicionar ao dicionario a média de cada aluno com 

print()
print(nome_e_medias) #irá imprimir ao dicionário
        
