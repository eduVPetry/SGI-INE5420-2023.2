from typing import List, Tuple

from model.transformations import normalization, transform, viewport_transformation


class GraphicalObject:

    def __init__(self, name: str, type: str, color_rgb: int, coordinates: List[Tuple[float, float]]) -> None:
        self.name = name
        self.type = type
        self.color_rgb = color_rgb
        self.world_coordinates = coordinates
        self.normalized_coordinates: List[Tuple[float, float]] = [None] * len(coordinates)
        self.viewport_coordinates: List[Tuple[float, float]] = [None] * len(coordinates)

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
        self.viewport_coordinates = transform(transformation_matrix, self.normalized_coordinates)
