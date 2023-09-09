from typing import List, Tuple

from model.graphical_object import GraphicalObject


class Line(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, world_coordinates: List[Tuple[float, float]]):
        super().__init__(name, "Line", color_rgb, world_coordinates)
