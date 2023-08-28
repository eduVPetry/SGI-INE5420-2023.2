from functools import reduce
from math import cos, sin, radians
from typing import List
import numpy as np


def translation(delta_x, delta_y):
    result = np.matmul([delta_x, delta_y, 1],[[1, 0, 0], [0, 1, 0], [delta_x, delta_y, 1]])
    return np.array(result, dtype=float)

def rotation_around_center_of_world(angle):
    result = np.matmul([0, 0, 1], [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])
    return np.array(result, dtype=float)

def rotation_around_center_of_object(angle, center_x, center_y):
    return rotation_around_arbitrary_point(angle, center_x, center_y)

def rotation_around_arbitrary_point(angle, x, y):
    a = np.matmul([x, y, 1], [[1, 0, 0], [0, 1, 0], [-x, -y, 1]])
    b = np.matmult([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [x, y, 1]])
    result = np.matmul(a, b)
    return np.array(result, dtype=float)

def dilation(scale_x, scale_y):
    result = np.matmul([scale_x, scale_y, 1], [[scale_x, 0, 0], [0, scale_y, 0], [0, 0, 1]])
    return np.array([], dtype=float)

def natural_dilation(scale_x, scale_y, center_x, center_y):
    a = np.matmul([scale_x, scale_y, 1], [[1, 0, 0], [0, 1, 0], [-center_x, -center_y, 1]])
    b = np.matmult([[scale_x, 0, 0], [0, scale_y, 0], [0, 0, 1]],
                   [[1, 0, 0], [0, 1, 0], [scale_x, scale_y, 1]])
    result = np.matmul(a, b)
    return np.array(result, dtype=float)

def compose(transformation_matrices: List[np.array]):
    return reduce(np.matmul, transformation_matrices, np.identity(3))
