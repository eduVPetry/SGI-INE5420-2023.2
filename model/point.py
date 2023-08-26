from typing import List
from PyQt5.QtCore import QPointF

from model.graphical_object import GraphicalObject


class Point(GraphicalObject):

    def __init__(self, name: str, coordinates: List[QPointF], color_rgb: int):
        super().__init__(name, "Point", coordinates, color_rgb)
