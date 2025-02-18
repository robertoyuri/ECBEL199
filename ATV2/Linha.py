from Camada import Camada

class Linha(Camada):
    def __init__(self, nome, sistema, ponto1, ponto2):
        super().__init__(nome, sistema)
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def __str__(self):
        return str(super.__str__(self)) + " .. " + str(self.ponto1)+ " .. " + str(self.ponto2)

    def exibirInfo(self):
        return str(super().exibirInfo(self)) + " .. " + str(self.ponto1)+ " .. " + str(self.ponto2)