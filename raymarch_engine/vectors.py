import math as mt
from numba import jit
import numpy as np


@jit(cache=True)
def length(vec: tuple[float, float]) -> float:
    val = vec[0]**2 + vec[1]**2

    if val != 0:
        return mt.sqrt(val)
    return val


@jit(cache=True)
def add(vec1: tuple[float, float], vec2: tuple[float, float]):
    return vec1[0] + vec2[0], vec1[1] + vec2[1]


@jit(cache=True)
def sub(vec1: tuple[float, float], vec2: tuple[float, float]):
    return vec1[0] - vec2[0], vec1[1] - vec2[1]


@jit(cache=True)
def mul(vec: tuple[float, float], siz: float):
    return vec[0] * siz, vec[1] * siz


@jit(cache=True)
def div(vec: tuple[float, float], siz: float):
    if siz != 0:
        return mul(vec, 1/siz)
    return 0, 0


@jit(cache=True)
def abs_vec(vec: tuple[float, float]):
    return abs(vec[0]), abs(vec[1])


@jit(cache=True)
def clamp(val: float, mn: float, mx: float) -> float:
    return min(max(mn, val), mx)


@jit(cache=True)
def clamp_vec(vec: tuple[float, float], border: tuple[float, float]) -> tuple[float, float]:
    return clamp(vec[0], -border[0], border[0]), clamp(vec[1], -border[1], border[1])


@jit(cache=True)
def nearer(val: float, left: float, right: float):
    return left if abs(left - val) < abs(right - val) else right


@jit(cache=True)
def clamp_out(val: float, left: float, right: float):
    if val < left:
        return val
    if val > right:
        return val
    return nearer(val, left, right)


@jit(cache=True)
def box_border(val: tuple[float, float], box: tuple[float, float]) -> tuple[float, float, bool]:
    # return clamp(clamp_out(val[0], -box[0], box[0]), -box[0], box[0]),\
    #        clamp(clamp_out(val[1], -box[1], box[1]), -box[1], box[1])
    if val[0] < -box[0]:
        return -box[0], clamp(val[1], -box[1], box[1]), True
    if val[0] > box[0]:
        return box[0], clamp(val[1], -box[1], box[1]), True
    if val[1] < -box[1]:
        return clamp(val[0], -box[0], box[0]), -box[1], True
    if val[1] > box[1]:
        return clamp(val[0], -box[0], box[0]), box[1], True
    return clamp_out(val[0], -box[0], box[0]), clamp_out(val[1], -box[1], box[1]), False


@jit(cache=True)
def get_rotation_matrix(angle: float):
    return np.array([[mt.cos(angle), -mt.sin(angle)], [mt.sin(angle), mt.cos(angle)]])


@jit(cache=True)
def rotate_vect(ray: tuple[float, float], angle: float, radian: bool = False):
    th: float = angle
    if not radian:
        np.deg2rad(th)
    ret = np.dot(get_rotation_matrix(th), np.array(ray))
    return ret[0], ret[1]
