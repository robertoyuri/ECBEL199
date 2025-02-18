from Camada import Camada

class Poligono(Camada):
    def __init__(self, nome, sistema, pontos):
        super().__init__(nome, sistema)
        self.pontos = pontos

    def __str__(self):
        result = "Pontos:"
        for ponto in self.pontos:
            result += "\n" + str(ponto)
        return result

    def exibirInfo(self):
        result = "Pontos:"
        for ponto in self.pontos:
            result += "\n" + str(ponto)
        return result