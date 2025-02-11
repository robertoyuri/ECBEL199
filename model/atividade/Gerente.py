from Funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, nascimento, cpf, cargo, salario, departamento):
        super().__init__(nome, nascimento, cpf, cargo, salario)
        self.departamento = departamento

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self):
        super().calcularSalario(self)

    def gerenciarProjetos(self):
        return "Projeto Gerenciado"