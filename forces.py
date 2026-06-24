import numpy as np


def acc_gravity(x: float, y: float) -> tuple[float, float]:
    acc_x = -x / np.hypot(x, y) ** 3
    acc_y = -y / np.hypot(x, y) ** 3
    return acc_x, acc_y
