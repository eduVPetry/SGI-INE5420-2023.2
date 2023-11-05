from typing import List, Tuple

from model.graphical_object import GraphicalObject
from model.transformations import normalization_3d, transform


class WavefrontOBJ(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, world_coordinates: List[Tuple[float, float]], faces: List[Tuple[int, ...]]):
        super().__init__(name, "Wavefront OBJ", color_rgb, world_coordinates)
        self.faces = faces

    def geometric_center(self) -> Tuple[float, float]:
        center_x = center_y = center_z = 0
        for x, y, z in self.world_coordinates:
            center_x += x
            center_y += y
            center_z += z
        center_x /= len(self.world_coordinates)
        center_y /= len(self.world_coordinates)
        center_z /= len(self.world_coordinates)
        return center_x, center_y, center_z

    def perspective_projection(self) -> None:
        self.projected_coordinates = []
        d = 1200  # distance to projection center
        for x, y, z in self.world_coordinates:
            x_new = (x * d) / (z + d)
            y_new = (y * d) / (z + d)
            self.projected_coordinates.append((x_new, y_new, 0))

    def normalize(self, _window) -> None:
        self.perspective_projection()  # apply perspective projection before normalization
        transformation_matrix = normalization_3d(_window)
        self.normalized_coordinates = transform(transformation_matrix, self.projected_coordinates)

    def clip(self, _window, clipping_method):
        clipped_lines = []
        for face in self.faces:
            for i in range(len(face)-1):
                vertex_index1 = face[i]
                vertex_index2 = face[i+1]
                x0, y0, z0 = self.normalized_coordinates[vertex_index1-1]
                x1, y1, z1 = self.normalized_coordinates[vertex_index2-1]
                accept, new_line = clipping_method(x0, y0, x1, y1, _window)
                if accept:
                    clipped_lines.append(new_line)
            vertex_index1 = face[-1]
            vertex_index2 = face[0]
            x0, y0, z0 = self.normalized_coordinates[vertex_index1-1]
            x1, y1, z1 = self.normalized_coordinates[vertex_index2-1]
            accept, new_line = clipping_method(x0, y0, x1, y1, _window)
            if accept:
                clipped_lines.append(new_line)
        self.clipped_lines = clipped_lines
