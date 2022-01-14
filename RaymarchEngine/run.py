import math as mt
import numpy as np
from numba import jit
from . import configs


class RayMarcher:
    def __init__(self):
        pass


@jit
def generate_map():
    return np.full((configs.board_x_size, configs.board_y_size), 0, dtype="f")
