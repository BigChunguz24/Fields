import numpy as np
import pandas as pd

from typing import List

from matplotlib import pyplot as plt


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
    customized_plot(
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


def customized_plot(
    subplot,
    dataframe: pd.DataFrame,
    keyword_for_x: str,
    keyword_for_y: str,
    axis_scaling: str,
    coordinate_ticks: List[float],
    coordinate_limits: List[float],
    axis_label_offset: float,
):
    """
    :param subplot: ax[0], ax[1], ax[2], etc.
    :param dataframe: the dataframe with plot data
    :param keyword_for_x: column name for x-axis from dataframe
    :param keyword_for_y: column name for y-axis from dataframe
    :param axis_scaling: this is the scale of the x-axis vs y-axis. Available options are:
                "equal"  ---> Here 1 unit on x-axis = 1 unit on y-axis
                "auto"   ---> Stretches the axes independently so the plot fills the available space
                "scaled" ---> Maintains equal scaling like "equal", but auto-adjusts limits to fit data more tightly
    :param coordinate_ticks: this is how frequent are ticks on axes i.e. every 10 units
         coordinate_ticks[0] ---> for the x-axis
         coordinate_ticks[1] ---> for the y-axis
    :param coordinate_limits: these are numerical limits for x-axis and y-axis
                coordinate_limits[0] ---> for the x-axis - minimum
                coordinate_limits[1] ---> for the x-axis - maximum
                coordinate_limits[2] ---> for the y-axis - minimum
                coordinate_limits[3] ---> for the y-axis - maximum
    :param axis_label_offset: this is the offset of the label from the arrow position
    """
    # Plot x vs y
    subplot.plot(
        dataframe[keyword_for_x], dataframe[keyword_for_y], linewidth=1.2, alpha=0.85
    )

    # Set the scaling + tick positions
    subplot.set_aspect(axis_scaling)
    subplot.xaxis.set_major_locator(plt.MultipleLocator(coordinate_ticks[0]))
    subplot.yaxis.set_major_locator(plt.MultipleLocator(coordinate_ticks[1]))

    # Styling the background and the main axes lines
    subplot.set_facecolor("white")
    subplot.axhline(0, color="#222222", linewidth=1.5, linestyle="-", zorder=3)
    subplot.axvline(0, color="#222222", linewidth=1.5, linestyle="-", zorder=3)

    # Borderlines around the axes
    for spine in subplot.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(2.5)
        spine.set_color("black")

    # Control the grid, ticks, and minor tick marks to make it look more like a clean “graph paper” coordinate system
    subplot.minorticks_on()
    subplot.grid(True, which="major", linewidth=1.0, alpha=0.5, color="#AAAAAA")
    subplot.grid(True, which="minor", linewidth=0.5, alpha=0.3, color="#CCCCCC")
    subplot.tick_params(which="both", length=0, labelsize=10, labelcolor="#555555")

    # Set the coordinate limits
    xmin, xmax, ymin, ymax = coordinate_limits
    subplot.set_xlim(xmin, xmax)
    subplot.set_ylim(ymin, ymax)

    # Draw custom x- and y-axes with arrowheads on your plot
    subplot.annotate(
        "",
        xy=(xmax, 0),
        xytext=(xmin, 0),
        arrowprops=dict(arrowstyle="-|>", mutation_scale=18, color="#222222", lw=1.5),
        zorder=4,
    )

    subplot.annotate(
        "",
        xy=(0, ymax),
        xytext=(0, ymin),
        arrowprops=dict(arrowstyle="-|>", mutation_scale=18, color="#222222", lw=1.5),
        zorder=4,
    )

    # Add text labels (“x” and “y”) near the ends of your custom axes
    subplot.annotate(
        "x",
        xy=(xmax, 0),
        xytext=(xmax - axis_label_offset, -axis_label_offset * 1.2),
        fontsize=12,
        color="#222222",
        fontstyle="italic",
    )

    subplot.annotate(
        "y",
        xy=(0, ymax),
        xytext=(axis_label_offset * 0.5, ymax - axis_label_offset),
        fontsize=12,
        color="#222222",
        fontstyle="italic",
    )


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
