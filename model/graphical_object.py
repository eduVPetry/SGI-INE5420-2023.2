from typing import List, Tuple
import numpy as np

from model.transformations import normalization, transform, viewport_transformation


class GraphicalObject:

    def __init__(self, name: str, type: str, color_rgb: int, world_coordinates: List[Tuple[float, float]]) -> None:
        self.name = name
        self.type = type
        self.color_rgb = color_rgb
        self.world_coordinates = world_coordinates
        self.normalized_coordinates: List[Tuple[float, float]] = [None] * len(world_coordinates)
        self.clipped_lines: List[List[Tuple[float, float], Tuple[float, float]]] = []
        self.viewport_lines: List[Tuple[float, float]] = []

    def geometric_center(self) -> Tuple[float, float]:
        center_x = center_y = 0
        for x, y in self.world_coordinates:
            center_x += x
            center_y += y
        center_x /= len(self.world_coordinates)
        center_y /= len(self.world_coordinates)
        return center_x, center_y

    def transform(self, transformation_matrix) -> None:
        self.world_coordinates = transform(transformation_matrix, self.world_coordinates)

    def normalize(self, _window) -> None:
        transformation_matrix = normalization(_window)
        self.normalized_coordinates = transform(transformation_matrix, self.world_coordinates)

    def viewport_transform(self, _viewport) -> None:
        transformation_matrix = viewport_transformation(_viewport)
        viewport_lines = []
        for line in self.clipped_lines:
            (x0, y0), (x1, y1) = line
            line0 = np.array([x0, y0, 1], dtype=float)
            line1 = np.array([x1, y1, 1], dtype=float)
            new_line0 = line0 @ transformation_matrix
            new_line1 = line1 @ transformation_matrix
            new_x0, new_y0, _ = new_line0
            new_x1, new_y1, _ = new_line1
            viewport_lines.append([(new_x0, new_y0), (new_x1, new_y1)])
        self.viewport_lines = viewport_lines
