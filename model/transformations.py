from functools import reduce
from math import cos, sin, radians
from typing import List, Tuple
import numpy as np
from PyQt5.QtCore import QPointF


def viewport_transformation(_viewport) -> QPointF:
    _translation = translation(1, -1)
    _dilation = dilation(_viewport.width/2, -_viewport.height/2)
    return compose([_translation, _dilation])

def normalization(_window):
    w_cx, w_cy = _window.center()
    _translation = translation(-w_cx, -w_cy)
    rotation = rotation_around_center_of_world(-_window.viewup_angle)
    _translation2 = translation(-_window.x_pan, -_window.y_pan)
    _dilation = dilation(2/_window.width(), 2/_window.height())
    return compose([_translation, rotation, _translation2, _dilation])

def translation(delta_x, delta_y):
    return np.array([[      1,       0, 0],
                     [      0,       1, 0],
                     [delta_x, delta_y, 1]], dtype=float)

def rotation_around_center_of_world(angle):
    angle = radians(angle)
    return np.array([[cos(angle), -sin(angle), 0],
                     [sin(angle),  cos(angle), 0],
                     [         0,           0, 1]], dtype=float)

def rotation_around_center_of_object(angle, center_x, center_y):
    return rotation_around_arbitrary_point(angle, center_x, center_y)

def rotation_around_arbitrary_point(angle, x, y):
    translation1 = translation(-x, -y)
    rotation = rotation_around_center_of_world(angle)
    translation2 = translation(x, y)
    return compose([translation1, rotation, translation2])

def dilation(scale_x, scale_y):
    return np.array([[scale_x,       0, 0],
                     [      0, scale_y, 0],
                     [      0,       0, 1]], dtype=float)

def natural_dilation(scale_x, scale_y, center_x, center_y):
    translation1 = translation(-center_x, -center_y)
    _dilation = dilation(scale_x, scale_y)
    translation2 = translation(center_x, center_y)
    return compose([translation1, _dilation, translation2])

def compose(transformation_matrices: List[np.array]):
    return reduce(np.matmul, transformation_matrices, np.identity(3))

def transform(transformation_matrix: np.array, coordinates: Tuple[float, float]) -> Tuple[float, float]:
    transformed_coordinates = []
    for x, y in coordinates:
        old_coordinates = np.array([x, y, 1], dtype=float)
        new_coordinates = old_coordinates @ transformation_matrix
        new_x, new_y, _ = new_coordinates
        transformed_coordinates.append((new_x, new_y))
    return transformed_coordinates
