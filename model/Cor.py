class Cor:
    def __init__(self, red, green, blue, codigo, nome):
        self.red = red
        self.green = green
        self.blue = blue
        self.codigo = codigo
        self.nome = nome

    def rgb2codigo(self):
        return False

    def __str__(self):
        return self.nome + " - " + self.codigo