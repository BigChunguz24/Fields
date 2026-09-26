from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from forces import acc_gravity
from numerical_methods import perform_euler
from matplotlib.animation import FuncAnimation
from phys_utils_plotting import plot_customisation


def tick_interval(axis_range: float, target_ticks: int = 10) -> float:
    raw_interval = axis_range / target_ticks
    if raw_interval <= 0:
        return 0.1

    magnitude = 10 ** np.floor(np.log10(raw_interval))
    normalized = raw_interval / magnitude
    nice_interval = np.select(
        [normalized <= 1, normalized <= 2, normalized <= 5],
        [1, 2, 5],
        default=10,
    )
    return float(nice_interval * magnitude)


def plot_trajectory(
    df: pd.DataFrame,
    delta_t: float,
    iterations: int,
    coordinate_limits: List[float] = None,
    coordinate_ticks: List[float] = None,
):

    if coordinate_limits is None:
        lim_left, lim_right = df["x_values"].min(), df["x_values"].max()
        lim_bottom, lim_top = df["y_values"].min(), df["y_values"].max()

        coordinate_limits = [lim_left, lim_right, lim_bottom, lim_top]

    if coordinate_ticks is None:
        lim_left, lim_right = df["x_values"].min(), df["x_values"].max()
        lim_bottom, lim_top = df["y_values"].min(), df["y_values"].max()

        coordinate_ticks = [
            tick_interval(lim_right - lim_left),
            tick_interval(lim_top - lim_bottom),
        ]

    # Drawing the plot
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
    plot_customisation(
        subplot=ax,
        dataframe=df,
        keyword_for_x="x_values",
        keyword_for_y="y_values",
        axis_scaling="equal",
        coordinate_ticks=coordinate_ticks,
        coordinate_limits=coordinate_limits,
        axis_label_offset=0.1,
    )

    ax.set_title(
        label=f"Траектория по метод на Ойлер с dt={delta_t} и N={iterations} итерации",
        fontsize=13,
        color="#222222",
        pad=14,
    )

    plt.tight_layout()

    return fig, ax


if __name__ == "__main__":
    animate = False
    iterations = 10000
    delta_t = 0.010

    # Initial coordinates and initial velocities
    x, y = 0.500, 0.000
    vx, vy = 0.000, 1.630

    df = perform_euler(
        initial_x=x,
        initial_y=y,
        initial_vx=vx,
        initial_vy=vy,
        acc_function=acc_gravity,
        iterations=iterations,
        delta_t=delta_t,
    )

    fig, ax = plot_trajectory(
        df=df,
        delta_t=delta_t,
        iterations=iterations,
        coordinate_limits=[-4.2, 1.1, -2.1, 2],
        coordinate_ticks=[0.5, 0.5],
    )

    if animate:
        (point,) = ax.plot([], [], "ro")

        def update(frame):
            point.set_data([df["x_values"][frame]], [df["y_values"][frame]])
            return (point,)

        ani = FuncAnimation(
            fig, update, frames=len(df["x_values"]), interval=0.01, blit=True
        )

    plt.show()
    plt.savefig(fname="static/planet_trajectory/trajectory.svg", format="svg")
