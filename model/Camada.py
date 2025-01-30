class Camada:
    def __init__(self, nome, cor, tipo, coordenada, regiao, uf, sigla, area):
        self.nome = nome
        self.cor = cor
        self.tipo = tipo
        self.coordenada = coordenada
        self.regiao = regiao
        self.uf = uf
        self.sigla = sigla
        self.area = area

    def __str__(self):
        return self.nome