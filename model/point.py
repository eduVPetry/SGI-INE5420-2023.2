from typing import List, Tuple

from model.clipping import point_clipping
from model.graphical_object import GraphicalObject


class Point(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, world_coordinates: List[Tuple[float, float]]):
        super().__init__(name, "Point", color_rgb, world_coordinates)

    def clip(self, _window):
        x0, y0 = self.normalized_coordinates[0]
        accept = point_clipping(x0, y0, _window)
        self.clipped_lines = [[(x0, y0), (x0, y0)]] if accept else []
