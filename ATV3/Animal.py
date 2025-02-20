from SerVivo import SerVivo
class Animal(SerVivo):
    def __init__(self, nome, reino, locomocao):
        super().__init__(nome, reino)
        self.locomocao = locomocao

    def exibirInfo(self):
        return super().exibirInfo() + " - " +str(self.locomocao)