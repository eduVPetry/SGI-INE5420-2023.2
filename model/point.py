from PyQt5.QtCore import QPointF


class Point(QPointF):

    def __init__(self, x: float, y: float, name: str):
        super().__init__(x, y)
        self.name = name
        self.type = "Point"
