from DevBack import DevBack
from DevFront import DevFront
class DevFull(DevBack, DevFront):
    def __init__(self):
        super().__init__(self)
        #DevBack.__init__(self, nome, nascimento, cpf, cargo, salario, linguagem, banco)
        #DevFront.__init__(self, nome, nascimento, cpf, cargo, salario, linguagem, framework)
        

    def __str__(self):
        super().__str__(self)

    def exibirInfo(self):
        super().exibirInfo(self)

    def calcularSalario(self):
        super().calcularSalario(self)

    def gerenciarProjetos(self):
        super().gerenciarProjetos(self)
        
    def configServer(self):
        super().configServer(self)

    def colorir(self):
        super().colorir(self)