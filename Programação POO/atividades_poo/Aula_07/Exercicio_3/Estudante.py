from Pessoa import Pessoa

class Estudante (Pessoa):
    def __init__(self, nome, idade,curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
      dados_pessoais = super().apresentar()
      return (f"{dados_pessoais} Curso: {self.curso}")
        