from Diretor import Diretor
class CEO(Diretor):
    def __init__(self, nome, nascimento, cpf, cargo, salario, departamento, bonus, lucro):
        super().__init__(nome, nascimento, cpf, cargo, salario, departamento, bonus)
        self.lucro = lucro

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self):
        super().calcularSalario(self)

    def gerenciarProjetos(self):
        super().gerenciarProjetos(self)

    def definirEstrategia(self):
        super().definirEstrategia(self)

    def tomaDecisao(self):
        return "Escolhido"