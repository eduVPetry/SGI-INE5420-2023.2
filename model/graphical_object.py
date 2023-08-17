from typing import List
from PyQt5.QtCore import QPointF


class GraphicalObject:

    def __init__(self, name: str, type: str, coordinates: List[QPointF]):
        self.name = name
        self.type = type
        self.coordinates = coordinates
