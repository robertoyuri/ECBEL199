class Aluno:
    def __init__(self, matricula, cpf, nome, nascimento, email):
        self.matricula = matricula
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.email = email

    def __str__(self):
        return str(self.matricula) + " - " + self.nome
