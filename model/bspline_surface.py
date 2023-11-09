import numpy as np
from typing import List, Tuple

from model.graphical_object import GraphicalObject
from model.transformations import normalization_3d, transform, viewport_transformation


class BSplineSurface(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, control_points: List[List[Tuple[float, float, float]]]):
        super().__init__(name, "B-Spline Surface", color_rgb, [])
        self.control_points = np.array(control_points)

        ...

    def geometric_center(self) -> Tuple[float, float]:
        center_x = center_y = center_z = 0
        for curve in self.world_coordinates:
            for x, y, z in curve:
                center_x += x
                center_y += y
                center_z += z
        center_x /= self.num_points_total
        center_y /= self.num_points_total
        center_z /= self.num_points_total
        return center_x, center_y, center_z

    def transform(self, transformation_matrix) -> None:
        self.world_coordinates = [transform(transformation_matrix, e) for e in self.world_coordinates]

    def perspective_projection(self) -> None:
        self.projected_coordinates = []
        d = 1200  # distance to projection center
        for curve in self.world_coordinates:
            row = []
            for x, y, z in curve:
                x_new = (x * d) / (z + d)
                y_new = (y * d) / (z + d)
                row.append((x_new, y_new, 0))
            self.projected_coordinates.append(row)

    def normalize(self, _window) -> None:
        self.perspective_projection()  # apply perspective projection before normalization
        transformation_matrix = normalization_3d(_window)
        self.normalized_coordinates = [transform(transformation_matrix, e) for e in self.projected_coordinates]

    def clip(self, _window, clipping_method):
        clipped_lines = []
        for e in self.normalized_coordinates:
            row = []
            for i in range(len(e)-1):
                x0, y0, z0 = e[i]
                x1, y1, z1 = e[i+1]
                accept, new_line = clipping_method(x0, y0, x1, y1, _window)
                if accept:
                    row.append(new_line)
            clipped_lines.append(row)
        self.clipped_lines = clipped_lines

    def viewport_transform(self, _viewport) -> None:
        transformation_matrix = viewport_transformation(_viewport)
        viewport_lines = []
        for e in self.clipped_lines:
            row = []
            for line in e:
                (x0, y0), (x1, y1) = line
                line0 = np.array([x0, y0, 1], dtype=float)
                line1 = np.array([x1, y1, 1], dtype=float)
                new_line0 = line0 @ transformation_matrix
                new_line1 = line1 @ transformation_matrix
                new_x0, new_y0, _ = new_line0
                new_x1, new_y1, _ = new_line1
                row.append([(new_x0, new_y0), (new_x1, new_y1)])
            viewport_lines.append(row)
        self.viewport_lines = viewport_lines
