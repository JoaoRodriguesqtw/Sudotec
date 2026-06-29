lf_lista_numeros = [] #criação da lista que irá armazenar os numeros escolhidos

li_quantos_nums = int(input("quantos numeros você quer digitar? ")) #variavel que irá pedir quantos numeros o usuario quer digitar

for n in range (li_quantos_nums): #estrutura for que usará li_quantos_nums para definir quantas vezes irá se repetir 
    lf_nums_escolhidos = float(input(f"digite o {n + 1}° numero: "))#variavel que irá pedir os numeros a serem somados e feitos a média
    lf_lista_numeros.append(lf_nums_escolhidos) #.append irá adicionar os numeros escolhidos na lista_numeros

lf_media = sum(lf_lista_numeros)/len(lf_lista_numeros) #fará a média dos numeros escolhidos

print(f"a lista contem {len(lf_lista_numeros)} numeros, a soma de tudo é {sum(lf_lista_numeros)} e a média de tudo é {lf_media}")
#len() mostrará quantos numeros tem na lista, sum() fará a soma de tudo que está na lista e lf_media mostrará a média de tudo que esta na lista