import math as mt
from numba import jit


@jit(cache=True)
def length(vec: tuple[float, float]):
    return mt.sqrt(vec[0]**2 + vec[1]**2)


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
    return mul(vec, 1/siz)


@jit(cache=True)
def abs_vec(vec: tuple[float, float]):
    return abs(vec[0]), abs(vec[1])
