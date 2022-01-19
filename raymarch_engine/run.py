from __future__ import annotations

import numpy as np
from numba import jit
from . import configs
from .tools import ShapeExecutor as _ShapeExecutor


class RayMarcher:
    def __init__(self, distance_func: _ShapeExecutor):
        self.distance_func = distance_func
        self.map = generate_map()

    @staticmethod
    @jit(cache=True)
    def generate_color(dist: float) -> tuple[int, int, int]:
        if 1 > dist > -1:
            return 255, 0, 0
        elif dist <= -1:
            if dist % 5 < 2.5:
                return 50, 50, 50
            return 30, 30, 30
        elif dist % 5 < 2.5:
            return 255, 255, 255
        else:
            return 200, 200, 200

    def update(self, offset: tuple[float, float] = (0, 0)):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                self.map[x][y] = self.generate_color(self.distance_func((float(x + offset[0]), float(y + offset[1]))))


def generate_map():
    return np.full((configs.board_x_size, configs.board_y_size), (0, 0, 0), dtype=(float, 3))
