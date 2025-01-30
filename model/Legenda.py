class Legenda:
    def __init__(self, cor, simbolo, nome, tamanho, formato):
        self.cor = cor
        self.simbolo = simbolo
        self.nome = nome
        self.tamanho = tamanho
        self.formato = formato

    def __str__(self):
        return self.nome