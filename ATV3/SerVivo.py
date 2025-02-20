class SerVivo:
    def __init__(self, nome, reino):
        self.nome = nome
        self.reino = reino

    def exibirInfo(self):
        return str(self.nome + " - " + self.reino)