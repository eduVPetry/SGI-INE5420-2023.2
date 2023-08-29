from functools import reduce
from math import cos, sin, radians
from typing import List
import numpy as np


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
