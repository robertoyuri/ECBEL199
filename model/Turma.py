class Turma:
    def __init__(self, codigo, curso, periodo, local, docentes, discentes):
        self.codigo = codigo
        self.curso = curso
        self.periodo = periodo
        self.local = local
        self.docentes = docentes
        self.discentes = discentes

    def __str__(self):
        return self.codigo