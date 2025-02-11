class Pessoa:
    def __init__(self, nome, nascimento, cpf):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf

    def __str__(self):
        return str(self.cpf) + " - " + self.nome

    def exibirInfo(self):
        return str(self.cpf) + " - " + self.nome + self.nascimento