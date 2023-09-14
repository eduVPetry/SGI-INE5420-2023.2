from typing import List, Tuple

from model.graphical_object import GraphicalObject


class WavefrontOBJ(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, world_coordinates: List[Tuple[float, float]], faces: List[Tuple[int, ...]]):
        super().__init__(name, "Wavefront OBJ", color_rgb, world_coordinates)
        self.faces = faces
