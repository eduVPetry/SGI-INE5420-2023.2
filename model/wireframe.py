from typing import List

from model.point import Point


class Wireframe:

    def __init__(self, coordinates: List[Point], name: str):
        self.coordinates = coordinates
        self.name = name
        self.type = "Wireframe"
