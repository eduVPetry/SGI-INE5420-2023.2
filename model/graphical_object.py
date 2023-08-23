from typing import List
from PyQt5.QtCore import QPointF


class GraphicalObject:

    def __init__(self, name: str, type: str, coordinates: List[QPointF]):
        self.name = name
        self.type = type
        self.coordinates = coordinates

    def geometric_center(self) -> QPointF:
        center_x = center_y = 0
        for point in self.coordinates:
            center_x += point.x
            center_y += point.y
        center_x /= len(self.coordinates)
        center_y /= len(self.coordinates)
        return QPointF(center_x, center_y)
