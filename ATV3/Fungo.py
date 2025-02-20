from SerVivo import SerVivo
class Fungo(SerVivo):
    def __init__(self, nome, reino, reproducao):
        super().__init__(nome, reino)
        self.reproducao = reproducao

    def exibirInfo(self):
        return super().exibirInfo() + " - " + str(self.reproducao)