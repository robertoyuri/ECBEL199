from Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, nascimento, cpf, cargo, salario):
        super().__init__(nome, nascimento, cpf)
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self, horas, valor):
        self.salario = horas * valor * 8 * 22
        return self.salario