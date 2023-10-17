from typing import List, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from model.graphical_object import GraphicalObject


class BezierCurve(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, control_points: List[Tuple[float, float]]):
        super().__init__(name, "Bézier Curve", color_rgb, [])
        self.control_points = control_points

    def clip(self, _window, clipping_method):
        ...
