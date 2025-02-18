from Camada import Camada
from Ponto import Ponto
from Linha import Linha
from Poligono import Poligono

camada = Camada("Teste", "metros")
ponto1 = Ponto(camada.nome, camada.sistema, 21, 56)
ponto2 = Ponto(camada.nome, camada.sistema, 12, 65)
linha = Linha(camada.nome, camada.sistema, ponto1, ponto2)
pontos = [ponto1, ponto2, ponto1, ponto2, ponto1, ponto2]
poligono = Poligono(camada.nome, camada.sistema, pontos)

print(camada)
print(ponto1)
print(ponto2)
print(linha)
print(pontos)
print(poligono)