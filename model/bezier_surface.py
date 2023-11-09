import numpy as np
from typing import List, Tuple

from model.graphical_object import GraphicalObject
from model.transformations import normalization_3d, transform, viewport_transformation


class BezierSurface(GraphicalObject):

    def __init__(self, name: str, color_rgb: int, control_points: List[List[Tuple[float, float, float]]]):
        super().__init__(name, "Bézier Surface", color_rgb, [])
        self.control_points = np.array(control_points)

        # Blending functions
        B0 = lambda x: x**3
        B1 = lambda x: x**2
        B2 = lambda x: x
        B3 = lambda x: 1

        # Bézier matrix
        M_b = np.array([[-1,  3, -3, 1],
                        [ 3, -6,  3, 0],
                        [-3,  3,  0, 0],
                        [ 1,  0,  0, 0]])

        # Geometry vectors
        G_x = self.control_points[:, :, 0]
        G_y = self.control_points[:, :, 1]
        G_z = self.control_points[:, :, 2]

        num_points_s = num_points_t = 15
        self.num_points_total = num_points_s * num_points_t
        s_values = np.linspace(0, 1, num_points_s)
        t_values = np.linspace(0, 1, num_points_t)

        # S direction
        for s in s_values:
            S = np.array([B0(s), B1(s), B2(s), B3(s)])
            A = S @ M_b
            curve = []
            for t in t_values:
                T = np.array([B0(t), B1(t), B2(t), B3(t)])
                B = M_b.T @ T.T

                x = A @ G_x @ B
                y = A @ G_y @ B
                z = A @ G_z @ B

                curve.append((x, y, z))
            self.world_coordinates.append(curve)

        # T direction
        for t in t_values:
            T = np.array([B0(t), B1(t), B2(t), B3(t)])
            B = M_b.T @ T.T
            curve = []
            for s in s_values:
                S = np.array([B0(s), B1(s), B2(s), B3(s)])
                A = S @ M_b

                x = A @ G_x @ B
                y = A @ G_y @ B
                z = A @ G_z @ B

                curve.append((x, y, z))
            self.world_coordinates.append(curve)

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
