class Camada:
    def __init__(self, nome, sistema):
        self.nome = nome
        self.sistema = sistema

    def __str__(self):
        return str(self.nome) + " - " + str(self.sistema)

    def exibirInfo(self):
        return str(self.nome) + " - " + str(self.sistema)

