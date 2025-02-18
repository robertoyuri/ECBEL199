from Camada import Camada
class Ponto(Camada):
    def __init__(self, nome, sistema, x, y):
        super().__init__(nome, sistema)
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " x " + str(self.y)

    def exibirInfo(self):
        return (str(super().exibirInfo(self)) +
                str(self.x) + " x " + str(self.y))

