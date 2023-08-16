from PyQt5.QtCore import QLineF


class Line(QLineF):

    def __init__(self, x1: float, y1: float, x2: float, y2: float, name: str):
        super().__init__(x1, y1, x2, y2)
        self.name = name
        self.type = "Line"
