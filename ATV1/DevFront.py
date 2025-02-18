from Desenvolvedor import Desenvolvedor
class DevFront(Desenvolvedor):
    def __init__(self, nome, nascimento, cpf, cargo, salario, linguagem, framework):
        super().__init__(nome, nascimento, cpf, cargo, salario, linguagem)
        self.framework = framework

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self):
        super().calcularSalario(self)

    def gerenciarProjetos(self):
        super().gerenciarProjetos(self)

    def colorir(self):
        return "Colorir a interface"