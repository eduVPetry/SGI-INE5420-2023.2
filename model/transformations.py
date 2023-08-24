from functools import reduce
from math import cos, sin, radians
from typing import List
import numpy as np


def translation(delta_x, delta_y):
    return np.array([], dtype=float)

def rotation_around_center_of_world(angle):
    return np.array([], dtype=float)

def rotation_around_center_of_object(angle, center_x, center_y):
    return rotation_around_arbitrary_point(angle, center_x, center_y)

def rotation_around_arbitrary_point(angle, x, y):
    return np.array([], dtype=float)

def dilation(scale_x, scale_y):
    return np.array([], dtype=float)

def natural_dilation(scale_x, scale_y, center_x, center_y):
    return np.array([], dtype=float)

def compose(transformation_matrices: List[np.array]):
    return np.array(reduce(np.matmul, transformation_matrices), dtype=float)
