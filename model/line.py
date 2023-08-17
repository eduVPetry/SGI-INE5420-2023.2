from typing import List
from PyQt5.QtCore import QPointF

from model.graphical_object import GraphicalObject


class Line(GraphicalObject):

    def __init__(self, name: str, coordinates: List[QPointF]):
        super().__init__(name, "Line", coordinates)
