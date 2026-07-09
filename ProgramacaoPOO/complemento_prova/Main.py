# Arquivo principal que executa o programa, onde são criados os personagens e a rodada de ataques, além de mostrar os resultados ao final do combate.

from Guerreiro import Guerreiro
from Mago import Mago
from Inimigo import Inimigo

def rodada_de_ataques(equipe): #função que executa a rodada de ataques, onde cada personagem ataca o próximo da lista, e o ultimo ataca o primeiro
    turnos = int(input("Quantos turnos terá o combate? "))
    for n in range(turnos):
        for i in range(len(equipe)):
            atacante = equipe[i]
            alvo = equipe[(i + 1) % len(equipe)]  
            atacante.atacar(alvo)
            print()



def Main(): 
    guerreiro1 = Guerreiro("Aragorn", 100, 15, 5)
    mago1 = Mago("Gandalf", 80, 20, 50)
    inimigo1 = Inimigo("Balrog", 10, 10)

    equipe = [guerreiro1, mago1, inimigo1]
    print()
    rodada_de_ataques(equipe)
    print()
    print("Resultados")
    for personagem in equipe:
        print(f"{personagem.nome} - Vida: {personagem.vida}, Vivo?: {personagem.esta_vivo()}")
    
    print() #teste do encapsulamento, a vida é setada como -500, porem o setter impede que seja negativa
    print("--- Teste do encapsulamento como privated---")
    guerreiro1.vida = -500 
    print(f"Vida de {guerreiro1.nome} após tentar deixar como -500: {guerreiro1.vida}")
    print()
Main()

