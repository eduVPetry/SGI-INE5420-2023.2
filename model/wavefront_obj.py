from typing import List, Tuple

from model.graphical_object import GraphicalObject


class WavefrontOBJ(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, world_coordinates: List[Tuple[float, float]], faces: List[Tuple[int, ...]]):
        super().__init__(name, "Wavefront OBJ", color_rgb, world_coordinates)
        self.faces = faces

    def clip(self, _window, clipping_method):
        clipped_lines = []
        for face in self.faces:
            for i in range(len(face)-1):
                vertex_index1 = face[i]
                vertex_index2 = face[i+1]
                x0, y0 = self.normalized_coordinates[vertex_index1-1]
                x1, y1 = self.normalized_coordinates[vertex_index2-1]
                accept, new_line = clipping_method(x0, y0, x1, y1, _window)
                if accept:
                    clipped_lines.append(new_line)
            vertex_index1 = face[-1]
            vertex_index2 = face[0]
            x0, y0 = self.normalized_coordinates[vertex_index1-1]
            x1, y1 = self.normalized_coordinates[vertex_index2-1]
            accept, new_line = clipping_method(x0, y0, x1, y1, _window)
            if accept:
                clipped_lines.append(new_line)
        self.clipped_lines = clipped_lines
