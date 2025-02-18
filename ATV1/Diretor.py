from Gerente import Gerente
class Diretor(Gerente):
    def __init__(self, nome, nascimento, cpf, cargo, salario, departamento, bonus):
        super().__init__(nome, nascimento, cpf, cargo, salario, departamento)
        self.bonus = bonus

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self):
        super().calcularSalario(self)

    def gerenciarProjetos(self):
        super().gerenciarProjetos(self)

    def definirEstrategia(self):
        return "Estrategia Definida"