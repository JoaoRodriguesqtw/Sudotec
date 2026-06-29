lf_notas = [] #Criação da lista notas cujo irá armazenas as notas do aluno

li_qtd_notas = int(input("Digite quantas notas voce quer lançar: ")) #variavel que ira perguntar quantas notas o professor deseja lançar

print() # print vazio para dar um espaço no terminar e ficar visualmente mais agradavel

for n in range (li_qtd_notas): # laço de repetição "for" que irá utilizar a variavel qtd_notas para definir quantas vezes será definido
    lf_notas_lancadas = float(input(f"digite a {n + 1}° nota: "))#variavel que irá pedir as notas do aluno
    lf_notas.append(lf_notas_lancadas) #.append irá adicionar as notas lançadas na lista notas

lf_media = sum(lf_notas)/len(lf_notas) #sum ira somar todas as notas dentro de listas e irá dividir por len() cujo informa quantos valores tem dentro da lista, resultando na média

print()
print(f"a média do aluno foi de: {(lf_media):.1f}") #apresentação da média