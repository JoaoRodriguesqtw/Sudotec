from Pessoa import Pessoa

class Professor (Pessoa):
    def __init__(self, nome, idade,disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
      dados_pessoais = super().apresentar()
      return (f"{dados_pessoais} Disciplina: {self.disciplina}")
        