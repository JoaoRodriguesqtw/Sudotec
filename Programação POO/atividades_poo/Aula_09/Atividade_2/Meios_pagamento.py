from abc import ABC, abstractmethod

class MeioPagamento(ABC):
     
     def pagar(self,valor):
          ...


class Pix(MeioPagamento):
     def pagar(self,valor): 
          print(f"Pagando {valor} via pix (instantaneo)")

class Cartao(MeioPagamento):
     def pagar(self,valor):
          print(f"Pagando R$ {valor} no cartão (parcelável)")

class Boleto(MeioPagamento):
     def pagar(self,valor):
          print(f"Boleto de R$ {valor} gerado (vence em 3 dias)")


def Finalizar(meio: MeioPagamento,valor: float):
     meio.pagar(valor)


meios = [Pix(), Cartao(), Boleto()]
    
valor_compra = 150.00
print()
for meio in meios:
    Finalizar(meio, valor_compra)
     
      