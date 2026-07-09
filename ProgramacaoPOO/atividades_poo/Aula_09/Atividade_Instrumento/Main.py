from Instrumento import Instrumento
from Bateria import Bateria
from violao import Violao

#funciona
print()
Violao().tocar()
Bateria().tocar()

viola = Violao()
batera = Bateria()
print()
viola.tocar()
batera.tocar()
print()

#Instrumento()
#Não é possivel criar um objeto da classe instrumento(classe pai) pois a mesma foi definida como abstrata
# e o python não permite criarmos uma instancia de uma classe abstrata

