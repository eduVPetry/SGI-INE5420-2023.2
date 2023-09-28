from typing import List, Tuple

from model.graphical_object import GraphicalObject


class Wireframe(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, world_coordinates: List[Tuple[float, float]]):
        super().__init__(name, "Wireframe", color_rgb, world_coordinates)

    def clip(self, _window, clipping_method):
        clipped_lines = []
        for i in range(len(self.normalized_coordinates)-1):
            x0, y0 = self.normalized_coordinates[i]
            x1, y1 = self.normalized_coordinates[i+1]
            accept, new_line = clipping_method(x0, y0, x1, y1, _window)
            if accept:
                clipped_lines.append(new_line)
        x0, y0 = self.normalized_coordinates[-1]
        x1, y1 = self.normalized_coordinates[0]
        accept, new_line = clipping_method(x0, y0, x1, y1, _window)
        if accept:
            clipped_lines.append(new_line)
        self.clipped_lines = clipped_lines
