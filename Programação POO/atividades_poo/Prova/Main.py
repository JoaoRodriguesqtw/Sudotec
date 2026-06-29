from Personagem import Personagem
from guerreiro import Guerreiro
from mago import Mago
from inimigo import Inimigo



# def rodada_de_ataque(lista):
#     lista_personagens = [Guerreiro,Mago,Inimigo ]

#     for i in lista_personagens:
#         Personagem.atacar(lista_personagens[i],lista_personagens[i+1])


def rodada_de_ataque(lista):
    for i in range(len(lista)-1):
        atacante = lista[i]
        alvo = lista[i+1]
        atacante.atacar(alvo,quantidade=atacante.ataque)



def Main():
    guerreiro1 = Guerreiro("aragorn",7, 30,True)
    mago1 = Mago("gandalf",9,25,15)
    inimigo1 = Inimigo("goblin", 6,20)

    lista_npcs = [guerreiro1,mago1,inimigo1]

    rodada_de_ataque(lista_npcs)
Main()