from Desenvolvedor import Desenvolvedor
class DevBack(Desenvolvedor):
    def __init__(self, nome, nascimento, cpf, cargo, salario, linguagem, banco):
        super().__init__(nome, nascimento, cpf, cargo, salario, linguagem)
        self.banco = banco

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self):
        super().calcularSalario(self)

    def gerenciarProjetos(self):
        super().gerenciarProjetos(self)

    def configServer(self):
        return "Servidor configurado"