import numpy as np
from typing import List, Tuple

from model.graphical_object import GraphicalObject


class BezierCurve(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, control_points: List[Tuple[float, float]]):
        super().__init__(name, "Bézier Curve", color_rgb, [])
        self.control_points = control_points

        # Blending functions
        self.B0 = lambda t: t**3
        self.B1 = lambda t: t**2
        self.B2 = lambda t: t
        self.B3 = lambda t: 1

        # Bézier matrix
        self.M_b = np.array([[-1,  3, -3, 1],
                             [ 3, -6,  3, 0],
                             [-3,  3,  0, 0],
                             [ 1,  0,  0, 0]])

        N = len(control_points)
        for i in range(0, N-2-(N-1)%3, 3):
            sub_curve = self.generate_sub_curve(control_points[i:i + 4])
            self.world_coordinates.extend(sub_curve)

    def generate_sub_curve(self, control_points, num_points=100):
        control_points = np.array(control_points)
        sub_curve = []

        t_values = np.linspace(0, 1, num_points)
        for t in t_values:
            T = np.array([self.B0(t), self.B1(t), self.B2(t), self.B3(t)])
            TM_b = T @ self.M_b

            x_coordinate = TM_b @ control_points[:, 0]
            y_coordinate = TM_b @ control_points[:, 1]

            sub_curve.append([x_coordinate, y_coordinate])

        return sub_curve

    def clip(self, _window, clipping_method):
        clipped_lines = []
        for i in range(len(self.normalized_coordinates)-1):
            x0, y0 = self.normalized_coordinates[i]
            x1, y1 = self.normalized_coordinates[i+1]
            accept, new_line = clipping_method(x0, y0, x1, y1, _window)
            if accept:
                clipped_lines.append(new_line)
        self.clipped_lines = clipped_lines
