from typing import List
from PyQt5.QtCore import QPointF

from model.graphical_object import GraphicalObject


class Point(GraphicalObject):

    def __init__(self, name: str, coordinates: List[QPointF]):
        super().__init__(name, "Point", coordinates)
