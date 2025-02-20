from SerVivo import SerVivo
class Planta(SerVivo):
    def __init__(self, nome, reino, fotossinte):
        super().__init__(nome, reino)
        self.fotossinte = fotossinte

    def exibirInfo(self):
        return super().exibirInfo() + " - " + str(self.fotossinte)