from typing import Callable

import pandas as pd

column_labels = [
    "t_values",
    "x_values",
    "y_values",
    "vx_values",
    "vy_values",
    "ax_values",
    "ay_values",
]


def perform_euler(
    initial_x: float,
    initial_y: float,
    initial_vx: float,
    initial_vy: float,
    acc_function: Callable[[float, float], tuple[float, float]],
    iterations: int,
    delta_t: float,
) -> pd.DataFrame:
    x, y = initial_x, initial_y
    vx, vy = initial_vx, initial_vy

    rows = []
    for i in range(iterations):
        ax, ay = acc_function(x, y)
        rows.append((i * delta_t, x, y, vx, vy, ax, ay))

        x += vx * delta_t
        y += vy * delta_t

        vx += ax * delta_t
        vy += ay * delta_t

    return pd.DataFrame(rows, columns=column_labels)
