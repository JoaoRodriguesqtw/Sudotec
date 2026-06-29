#Instancia objetos a partir de classes criadas

#1 - defina duas classes diferentes das utilizadas para exemplos
#2 - instancie 3 objetos a partir de cada uma das classes
#3 - imprima o tipo de cada um dos objetos
#4 - imprima o endereço de memória de cada objeto
#5 - verifique e imprima se um objeto é igual o outro (escolha dois objetos quaisquer)
#6 - verifique e imprima se um objeto corresponde à instancia de uma determinada classe (escolha um objeto qualquer)


class Cores:
    pass


class Pessoa:
    pass

#Instancias da classe cachorro
azul = Cores()
vermelho = Cores()
verde = Cores()
#Aqui termina as instancias da classe cachorro


#Instancias da classe Pessoa
gabriella = Pessoa()
gustavo = Pessoa()
fernando = Pessoa()
#Aqui termina as instancias da classe pessoa

#Tipos dos objetos da classe cachorro e seus endereços de memoria
print()
print(f"O tipo de azul é {(type(azul))} e seu endereço de memoria é {(id(azul))}")
print(f"o tipo de vermelho é {(type(vermelho))} e seu endereço de memoria é {(id(vermelho))}")
print(f"o tipo de verde é {(type(verde))} e seu endereço de memoria é {(id(verde))}")
print()
# aqui acaba Tipos dos objetos das classes cachorro e seus endereços de memoria

#tipos dos objetos da classe pessoa e seus endereços de memoria
print()
print(f"O tipo de gabriella é {(type(gabriella))} e seu endereço de memoria é {(id(gabriella))}")
print(f"o tipo de gustavo é {(type(gustavo))} e seu endereço de memoria é {(id(gustavo))}")
print(f"o tipo de fernando é {(type(fernando))} e seu endereço de memoria é {(id(fernando))}")
print()
# aqui termina tipos dos objetos da classe pessoa e seus endereços de memoria


#5 - verifique e imprima se um objeto é igual o outro (escolha dois objetos quaisquer)

print(f"azul é igual a verde?: {azul is verde}")

#6 - verifique e imprima se um objeto corresponde à instancia de uma determinada classe (escolha um objeto qualquer)

print(f"azul é da classe Pessoa? {(isinstance(azul,Pessoa))}")
print()