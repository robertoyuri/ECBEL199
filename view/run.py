from model.Cor import Cor
from model.Camada import Camada
from model.Coordenada import Coordenada
from model.Legenda import Legenda
from model.Mapa import Mapa
from model.Simbolo import Simbolo
from model.Turma import Turma
from model.Aluno import Aluno


cor1 = Cor(255,255,255, "#FFFFFF", "Branco")

cor2 = Cor(255, 0, 0, "#FF0000", "Vermelho")

coordenada1 = Coordenada(-15,10,"utm")

coordenada2 = Coordenada(-20, 22, "utm")

camada = Camada("Rodovia", cor2,"fim",coordenada2, "norte", "PA", "RD", "")

simbolo = Simbolo("norte", "roda dos ventos", 200, 200, "/image/roda.png")

legenda = Legenda(cor1,simbolo,"Legenda", 500, "quadrado")

mapa =  Mapa("1:500",legenda, "Geografico",coordenada1,"Retrato",
             "Top 10 mapas", "Arial",camada)
print(mapa)
print(mapa.coordenada)

aluno1 = Aluno("2023007919", "12345678901","Carlos Gabriel da Silva", "30/10/1994", "carlos@ufra.edu.br")
aluno2 = Aluno("2023003633", "12345678902","Helio Junior", "16/10/2001", "julio@ufra.edu.br")
aluno3 = Aluno("2023006014", "12345678903","Lucas Silva", "14/07/2006", "lucas@ufra.edu.br")
aluno4 = Aluno("2024300601", "12345678904","Cristian Oliveira", "11/10/2003", "cristian@ufra.edu.br")
aluno5 = Aluno("2023012525", "12345678905","Patrick Santos", "08/10/1998", "patrick@ufra.edu.br")
discentes = [aluno1, aluno2, aluno3, aluno4, aluno5]

turma = Turma("ECBEL199", "Eng. Cartografica", "2024.2", "Pavilhão - Lab2",
              "Roberto Yuri da Silva Franco", discentes)

print(turma)
for i, d in enumerate(turma.discentes):
    print(d)