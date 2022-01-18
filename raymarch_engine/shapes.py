from __future__ import annotations


from numba import jit, njit
import numpy as np
import math

from . import vectors as vec
from .tools import shape, ShapeExecutor


@shape
@jit(cache=True)
def example(ray: tuple[float, float]):
    pass


@shape
@jit(cache=True)
def circle(ray: tuple[float, float], circle_size):
    return vec.length(ray) - circle_size


@shape
@njit(cache=True)
def rectangle(ray: tuple[float, float], size: tuple[float, float]) -> float:
    clp = vec.box_border(ray, size)
    sub = vec.sub(ray, (clp[0], clp[1]))
    if clp[2]:
        return vec.length(sub)
    return -vec.length(sub)


@shape
def union(ray: tuple[float, float], shape1: ShapeExecutor, shape2: ShapeExecutor, *more: ShapeExecutor):
    if more:
        val = None
        for el in more:
            if val is None:
                val = el(ray[0], ray[1])
            else:
                val = min(val, el(ray[0], ray[1]))

        if val is not None:
            return min(shape1(ray[0], ray[1]), shape2(ray[0], ray[1]), val)
    return min(shape1(ray[0], ray[1]), shape2(ray[0], ray[1]))


@shape
def move(ray: tuple[float, float], shape1: ShapeExecutor, offset: tuple[float, float]):
    return shape1(ray[0] + offset[0], ray[1] + offset[1])


@shape
def reverse(ray: tuple[float, float], shape1: ShapeExecutor):
    return -shape1(ray[0], ray[1])


@shape
def rotate(ray: tuple[float, float], shape1: ShapeExecutor, angle: float, radian: bool = False):
    return shape1(*vec.rotate_vect(ray, angle, radian))


# @shape
# @jit(cache=True)


# @shape
# @jit(cache=True)
# def rectangle_(ray: tuple[float, float], a: tuple[float, float], b: tuple[float, float], th: float):
#     le = vec.length(vec.sub(b, a))
#     d = vec.div(vec.sub(b, a), le)
#     q = vec.sub(ray, vec.add(a, b))
#     q = q[0]/2, q[1]/2
#     v = np.array(q) @ np.array([[d[0], -d[1]], [d[1], d[0]]])
#     q = tuple(v)
#     q = vec.sub(vec.abs_vec(q), vec.mul((le, th), 0.5))
#
#     if q[0] > 0:
#         v1 = vec.length(q)
#     else:
#         v1 = 0.0
#     return v1 + min(max(q[0], q[1]), 0)
#
#
# @jit(cache=True)
# def magnitude(arr: np.ndarray) -> float:
#     return math.sqrt(np.sum(arr * arr))
#
#
# @shape
# def rectangle(ray: tuple[float, float], a: tuple[float, float], b: tuple[float, float], th: float):
#     return _rectangle_inside(np.array(ray), np.array(a), np.array(b), th)
#
#
# @jit(cache=True)
# def _rectangle_inside(p: np.ndarray, a: np.ndarray, b: np.ndarray, th: float) -> float:
#     l1 = magnitude(b - a)
#     if l1 == 0:
#         return math.inf
#
#     d = (b - a) / l1
#     q = p - (a + b) * 0.5
#     e = np.array([[d[0], -d[1]], [d[1], d[0]]])
#     q = e.T @ q  # I have no idea what mat2 is...
#     q = np.abs(q) - np.array([l1, th]) * 0.5
#     return magnitude(q) + min(max(q[0], q[1]), 0)


# float sdOrientedBox( in vec2 p, in vec2 a, in vec2 b, float th )
# {
#     float l = length(b-a);
#     vec2  d = (b-a)/l;
#     vec2  q = (p-(a+b)*0.5);
#           q = mat2(d.x,-d.y,d.y,d.x)*q;
#           q = abs(q)-vec2(l,th)*0.5;
#     return length(max(q,0.0)) + min(max(q.x,q.y),0.0);
# }


__all__ = [
    "circle",
    "rectangle",
    "union",
    "move",
    "reverse",
    "rotate"
]
