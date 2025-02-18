class Mapa:
    def __init__(self, escala, legenda, categoria, coordenada, orientacao, titulo, fonte, camada):
        self.escala = escala
        self.legenda = legenda
        self.categoria = categoria
        self.coordenada = coordenada
        self.orientacao = orientacao
        self.titulo = titulo
        self.fonte = fonte
        self.camada = camada

    def __str__(self):
        return self.titulo