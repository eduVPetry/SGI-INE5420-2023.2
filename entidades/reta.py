from entidades.ponto import Ponto

class Reta:
    def __init__(self, x1, y1, x2, y2):
        self.a = Ponto(x1, y1)
        self.b = Ponto(x2, y2)
