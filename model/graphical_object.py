import numpy as np
from typing import List, Tuple
from PyQt5.QtCore import QPointF


class GraphicalObject:

    def __init__(self, name: str, type: str, coordinates: List[QPointF], color_rgb: int) -> None:
        self.name = name
        self.type = type
        self.coordinates = coordinates
        self.color_rgb = color_rgb

    def geometric_center(self) -> Tuple[float, float]:
        center_x = center_y = 0
        for point in self.coordinates:
            center_x += point.x()
            center_y += point.y()
        center_x /= len(self.coordinates)
        center_y /= len(self.coordinates)
        return center_x, center_y

    def apply_transformation(self, transformation_matrix) -> None:
        for i, point in enumerate(self.coordinates):
            old_coordinates = np.array([point.x(), point.y(), 1], dtype=float)
            new_coordinates = old_coordinates @ transformation_matrix
            new_x, new_y, _ = new_coordinates
            self.coordinates[i] = QPointF(new_x, new_y)
