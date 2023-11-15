from copy import deepcopy
import numpy as np
from typing import List, Tuple

from model.graphical_object import GraphicalObject
from model.transformations import normalization_3d, transform, viewport_transformation


class BSplineSurface(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, control_points: List[List[Tuple[float, float, float]]]):
        super().__init__(name, "B-Spline Surface", color_rgb, [])
        self.control_points = np.array(control_points)

        # Generate curve using forward differences
        def generate_curve_fwd_diff(n, x, Δx, Δ2x, Δ3x, y, Δy, Δ2y, Δ3y, z, Δz, Δ2z, Δ3z):
            curve = []
            curve.append((x, y, z))
            for _ in range(n):
                x += Δx
                Δx += Δ2x
                Δ2x += Δ3x
                y += Δy
                Δy += Δ2y
                Δ2y += Δ3y
                z += Δz
                Δz += Δ2z
                Δ2z += Δ3z
                curve.append((x, y, z))
            self.world_coordinates.append(curve)

        # B-Spline matrix
        M_b = np.array([[-1,  3, -3, 1],
                        [ 3, -6,  3, 0],
                        [-3,  0,  3, 0],
                        [ 1,  4,  1, 0]]) / 6

        # Geometry vectors
        G_x = self.control_points[:, :, 0]
        G_y = self.control_points[:, :, 1]
        G_z = self.control_points[:, :, 2]

        # 1. Calculate coefficients
        C_x = M_b @ G_x @ M_b.T
        C_y = M_b @ G_y @ M_b.T
        C_z = M_b @ G_z @ M_b.T

        # 2. Calculate deltas for n_i steps in t and s
        n_s = n_t = 20
        δ_s = 1 / (n_s - 1)
        δ_t = 1 / (n_t - 1)

        # 3. Generate matrices Eδ_s and Eδ_t and transpose Eδ_t
        E = lambda δ: np.array([[     0,      0, 0, 1],
                                [  δ**3,   δ**2, δ, 0],
                                [6*δ**3, 2*δ**2, 0, 0],
                                [6*δ**3,      0, 0, 0]])

        Eδ_s = E(δ_s)
        Eδ_t = E(δ_t).T

        # 4. Calculate initial conditions (immutable, no need to recalculate later)
        _DD_x = Eδ_s @ C_x @ Eδ_t
        _DD_y = Eδ_s @ C_y @ Eδ_t
        _DD_z = Eδ_s @ C_z @ Eδ_t

        # Copies of initial conditions
        DD_x = deepcopy(_DD_x)
        DD_y = deepcopy(_DD_y)
        DD_z = deepcopy(_DD_z)

        # 5. Draw family of curves in t
        for _ in range(n_s + 1):
            # 5.1. Draw curve using forward differences
            generate_curve_fwd_diff(n_t, *DD_x[0], *DD_y[0], *DD_z[0])

            # 5.2. Update DD_x, DD_y, DD_z to generate initial conditions for the next curve
            for i in range(3):
                for j in range(4):
                    DD_x[i][j] += DD_x[i+1][j]
                    DD_y[i][j] += DD_y[i+1][j]
                    DD_z[i][j] += DD_z[i+1][j]

        # 6. Regenerate initial conditions
        # 7. Transpose DD_x, DD_y and DD_z
        DD_x = deepcopy(_DD_x).T
        DD_y = deepcopy(_DD_y).T
        DD_z = deepcopy(_DD_z).T

        # 8. Draw family of curves in s
        for _ in range(n_t + 1):
            # 8.1. Draw curve using forward differences
            generate_curve_fwd_diff(n_s, *DD_x[0], *DD_y[0], *DD_z[0])

            # 8.2. Update DD_x, DD_y, DD_z to generate initial conditions for the next curve
            for i in range(3):
                for j in range(4):
                    DD_x[i][j] += DD_x[i+1][j]
                    DD_y[i][j] += DD_y[i+1][j]
                    DD_z[i][j] += DD_z[i+1][j]

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
