from functools import reduce
from math import cos, sin, radians
from typing import List, Tuple
import numpy as np
from PyQt5.QtCore import QPointF


def compose(transformation_matrices: List[np.array]):
    dimensions = len(transformation_matrices[0])
    return reduce(np.matmul, transformation_matrices, np.identity(dimensions))

# def transform(transformation_matrix: np.array, coordinates: Tuple[float, float]) -> Tuple[float, float]:
#     transformed_coordinates = []
#     for x, y in coordinates:
#         old_coordinates = np.array([x, y, 1], dtype=float)
#         new_coordinates = old_coordinates @ transformation_matrix
#         new_x, new_y, _ = new_coordinates
#         transformed_coordinates.append((new_x, new_y))
#     return transformed_coordinates

def transform(transformation_matrix: np.array, coordinates: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
    transformed_coordinates = []
    for c in coordinates:
        old_coordinates = np.array([*c, 1], dtype=float)
        new_coordinates = old_coordinates @ transformation_matrix
        transformed_coordinates.append(tuple(new_coordinates[:len(c)]))
    return transformed_coordinates

def viewport_transformation(_viewport) -> QPointF:
    _translation1 = translation(1, -1)
    _dilation = dilation(_viewport.width/2, -_viewport.height/2)
    _translation2 = translation(_viewport.x_min, _viewport.y_min)
    return compose([_translation1, _dilation, _translation2])

# 2D transformations
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

# 3D transformations
def normalization_3d(_window):
    w_cx, w_cy = _window.center()
    _translation = translation_3d(-w_cx, -w_cy, 0)
    rotation = rotation_z(-_window.viewup_angle)
    _translation2 = translation_3d(-_window.x_pan, -_window.y_pan, 0)
    _dilation = dilation_3d(2/_window.width(), 2/_window.height(), 1)
    return compose([_translation, rotation, _translation2, _dilation])

def translation_3d(delta_x, delta_y, delta_z):
    return np.array([[      1,       0,       0, 0],
                     [      0,       1,       0, 0],
                     [      0,       0,       1, 0],
                     [delta_x, delta_y, delta_z, 1]], dtype=float)

def dilation_3d(scale_x, scale_y, scale_z):
    return np.array([[scale_x,       0,       0, 0],
                     [      0, scale_y,       0, 0],
                     [      0,       0, scale_z, 0],
                     [      0,       0,       0, 1]], dtype=float)

def natural_dilation_3d(scale_x, scale_y, scale_z, center_x, center_y, center_z):
    translation1 = translation_3d(-center_x, -center_y, -center_z)
    _dilation = dilation_3d(scale_x, scale_y, scale_z)
    translation2 = translation_3d(center_x, center_y, center_z)
    return compose([translation1, _dilation, translation2])

def rotation_x(angle):
    angle = radians(angle)
    return np.array([[1,           0,          0, 0],
                     [0,  cos(angle), sin(angle), 0],
                     [0, -sin(angle), cos(angle), 0],
                     [0,           0,          0, 1]], dtype=float)

def rotation_y(angle):
    angle = radians(angle)
    return np.array([[cos(angle), 0, -sin(angle), 0],
                     [         0, 1,           0, 0],
                     [sin(angle), 0,  cos(angle), 0],
                     [         0, 0,           0, 1]], dtype=float)

def rotation_z(angle):
    angle = radians(angle)
    return np.array([[ cos(angle), sin(angle), 0, 0],
                     [-sin(angle), cos(angle), 0, 0],
                     [          0,          0, 1, 0],
                     [          0,          0, 0, 1]], dtype=float)
