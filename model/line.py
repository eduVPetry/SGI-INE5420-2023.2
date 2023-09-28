from typing import List, Tuple

from model.graphical_object import GraphicalObject


class Line(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, world_coordinates: List[Tuple[float, float]]):
        super().__init__(name, "Line", color_rgb, world_coordinates)

    def clip(self, _window, clipping_method):
        (x0, y0), (x1, y1) = self.normalized_coordinates
        accept, new_line = clipping_method(x0, y0, x1, y1, _window)
        self.clipped_lines = [new_line] if accept else []
