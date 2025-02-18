from xml.sax.handler import property_interning_dict

from CEO import CEO
from Desenvolvedor import Desenvolvedor
from DevBack import DevBack
from DevFront import DevFront
from DevFull import DevFull
from Diretor import Diretor
from Estagiario import Estagiario
from Funcionario import Funcionario
from Gerente import Gerente
from Pessoa import Pessoa

lucas = Pessoa("Lucas Bastos", "14/07/2006", "123.456.789-01")
cristian = Funcionario("Cristian Lucas", "11/10/2003", "123.456.789-02","Dev Junior", 1000)
dani = Desenvolvedor("Dani", "13/01/2005", "550.123.456-91", "Dev", 2000, "python")
fernanda = Gerente("Fernanda Noronha", "20/02/2006", "022.123.456-78","Gerente", 22000, "Administrativo")
wesley = Estagiario("Wesley Batista", "19/07/2004","123.456.789-03","UFRA",500)
andre = DevBack("Andre Luis","11/11/2011", "124.456.789-99","Back",1500,"python","MariaDB")
junior = DevFront("Helio Junior", "16/10/2001", "123.456.789-77","Front",1600,"JS","Node")
iva = DevFull("Iva Santos","13/06/2001","123.456.789-34","Full",7000,"pythomn","postegrees","Django")
edilson = Diretor("Edilson Barbosa", "01/10/2003", "123.456.789-99","Diretor",10000,"Desenvolvedores","20%")
carlos = CEO("Carlos Silva","01/01/1975","123.456.789-88","CEO",20000,"cobertura","50%","50000")
print(lucas)
print(cristian.exibirInfo())
print(dani.calcularSalario())
print(fernanda.gerenciarProjetos())
print(wesley.trabalhar())
print(andre.gerenciarProjetos())
print(junior.calcularSalario())
print(iva.colorir())
print(edilson.definirEstrategia())
print(carlos.tomaDecisao())
