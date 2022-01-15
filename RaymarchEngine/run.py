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
        if dist > 2:
            return 255, 255, 255
        elif dist % 2 == 0:
            return 0, 0, 0
        else:
            return 10, 10, 10

    def update(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                self.map[x][y] = self.generate_color(self.distance_func(x, y))


def generate_map():
    return np.full((configs.board_x_size, configs.board_y_size), (0, 0, 0), dtype=(float, 3))
