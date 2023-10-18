import numpy as np
from typing import List, Tuple

from model.graphical_object import GraphicalObject


class BSpline(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, control_points: List[Tuple[float, float]]):
        super().__init__(name, "B-Spline", color_rgb, [])
        self.control_points = control_points

        # B-Spline matrix ?????
        MBs = np.array([[-1,  3, -3, 1],
                        [ 3, -6,  3, 0],
                        [-3,  0,  3, 0],
                        [ 1,  4,  1, 0]]) / 6

        δ = 0.1
        N = int(1 / δ)

        E = np.array([[     0,      0, 0, 1],
                      [  δ**3,   δ**2, δ, 0],
                      [6*δ**3, 2*δ**2, 0, 0],
                      [6*δ**3,      0, 0, 0]])

        for i in range(0, len(control_points)-3):
            G_x, G_y = np.array(control_points[i:i+4]).T

            C_x = MBs @ G_x
            C_y = MBs @ G_y

            x, Δx, Δ2x, Δ3x = E @ C_x
            y, Δy, Δ2y, Δ3y = E @ C_y

            # x_old, y_old = x, y
            self.world_coordinates.append((x, y))
            for _ in range(N):
                x += Δx
                Δx += Δ2x
                Δ2x += Δ3x
                y += Δy
                Δy += Δ2y
                Δ2y += Δ3y
                self.world_coordinates.append((x, y))
                # plt.plot([x_old, x], [y_old, y])
                # x_old, y_old = x, y

    def clip(self, _window, clipping_method):
        clipped_lines = []
        for i in range(len(self.normalized_coordinates)-1):
            x0, y0 = self.normalized_coordinates[i]
            x1, y1 = self.normalized_coordinates[i+1]
            accept, new_line = clipping_method(x0, y0, x1, y1, _window)
            if accept:
                clipped_lines.append(new_line)
        self.clipped_lines = clipped_lines
