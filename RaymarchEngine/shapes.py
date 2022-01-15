from __future__ import annotations

from numba import jit
import numpy as np
from . import vectors as vec
from .tools import shape


@shape
@jit(cache=True)
def example(ray: tuple[int, int]):
    pass


@shape
@jit(cache=True)
def circle(ray: tuple[int, int], circle_size):
    return vec.length(ray) - circle_size


@shape
@jit(cache=True, forceobj=True)
def rectangle(ray: tuple[int, int], a: tuple[int, int], b: tuple[int, int], th: int):
    le = vec.length(vec.sub(b, a))
    d = vec.div(vec.sub(b, a), le)
    q = vec.sub(ray, vec.add(a, b))
    q = q[0]/2, q[1]/2
    mx = np.matrix([[d[0], -d[1]], [d[1], d[0]]])
    q = tuple((mx @ q).tolist()[0])
    q = vec.sub(vec.abs_vec(q), vec.mul((le, th), 0.5))

    if q[0] > 0:
        v1 = vec.length(q)
    else:
        v1 = 0.0
    return v1 + min(max(q[0], q[1]), 0)


# float sdOrientedBox( in vec2 p, in vec2 a, in vec2 b, float th )
# {
#     float l = length(b-a);
#     vec2  d = (b-a)/l;
#     vec2  q = (p-(a+b)*0.5);
#           q = mat2(d.x,-d.y,d.y,d.x)*q;
#           q = abs(q)-vec2(l,th)*0.5;
#     return length(max(q,0.0)) + min(max(q.x,q.y),0.0);
# }
