import numpy as np

from physical_constants import uniform_g


def acc_gravity_uniform(x: float, y: float) -> tuple[float, float]:
    acc_x = 0
    acc_y = -uniform_g
    return acc_x, acc_y


def acc_gravity(x: float, y: float) -> tuple[float, float]:
    acc_x = -x / np.hypot(x, y) ** 3
    acc_y = -y / np.hypot(x, y) ** 3
    return acc_x, acc_y
