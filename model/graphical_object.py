from typing import List, Tuple


class GraphicalObject:
    def __init__(self, name, type, coordinates):
        self.name: str = name
        self.type: str = type
        self.coordinates: List[Tuple(float, float)] = coordinates
