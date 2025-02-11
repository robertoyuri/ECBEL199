from Pessoa import Pessoa
class Estagiario(Pessoa):
    def __init__(self, nome, nascimento, cpf, universidade, bolsa):
        super().__init__(nome, nascimento, cpf)
        self.universidade = universidade
        self.bolsa = bolsa

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def trabalhar(self, horas, valor):
        return "Trabalhar Trabalhar Trabalhar"