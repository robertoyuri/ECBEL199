from Funcionario import Funcionario
class Desenvolvedor(Funcionario):
    def __init__(self, nome, nascimento, cpf, cargo, salario, linguagem):
        super().__init__(nome, nascimento, cpf, cargo, salario)
        self.linguagem = linguagem

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self):
        super().calcularSalario(self)

    def gerenciarProjetos(self):
        return "Projeto Gerenciado"