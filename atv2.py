# Classe base
class Camada:
    def __init__(self, nome, sistema_coordenadas):
        self.nome = nome
        self.sistema_coordenadas = sistema_coordenadas

    def exibir_info(self):
        print(f"Camada: {self.nome}, Sistema de Coordenadas: {self.sistema_coordenadas}")

# Subclasse Ponto
class Ponto(Camada):
    def __init__(self, nome, sistema_coordenadas, coordenada):
        super().__init__(nome, sistema_coordenadas)
        self.coordenada = coordenada

    def exibir_info(self):
        super().exibir_info()
        print(f"Coordenada: {self.coordenada}")

# Subclasse Linha
class Linha(Camada):
    def __init__(self, nome, sistema_coordenadas, coordenadas):
        super().__init__(nome, sistema_coordenadas)
        self.coordenadas = coordenadas

    def exibir_info(self):
        super().exibir_info()
        print(f"Traçado: {self.coordenadas}")

# Subclasse Polígono
class Poligono(Camada):
    def __init__(self, nome, sistema_coordenadas, vertices):
        super().__init__(nome, sistema_coordenadas)
        self.vertices = vertices

    def exibir_info(self):
        super().exibir_info()
        print(f"Vértices: {self.vertices}")

# Testando o sistema
ponto1 = Ponto("Ponto A", "WGS 84", (10.5, -45.3))
linha1 = Linha("Rio", "SIRGAS 2000", [(10, 20), (15, 25), (18, 30)])
poligono1 = Poligono("Área Protegida", "SIRGAS 2000", [(5, 10), (10, 15), (15, 10), (5, 10)])

ponto1.exibir_info()
linha1.exibir_info()
poligono1.exibir_info()
