class Simbolo:
    def __init__(self, nome, imagem, altura, largura, endereco):
        self.nome = nome
        self.imagem = imagem
        self.altura = altura
        self.largura = largura
        self.endereco = endereco

    def zoom(self):
        return False

    def __str__(self):
        return self.nome + "(" + self.altura + "x" + self.largura + ")"