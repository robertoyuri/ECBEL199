class Coordenada:
    def __init__(self, lat, log, tipo):
        self.lat = lat
        self.log = log
        self.tipo = tipo

    def utm2dec(self):
        return False

    def __str__(self):
        return f"{self.lat} X {self.log}"
        #return str(self.lat) + "X" + str(self.log)
