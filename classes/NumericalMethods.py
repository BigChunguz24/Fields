import numpy as np
import pandas as pd

from enum import Enum
from typing import Callable, List

from matplotlib import pyplot as plt

# All numerical methods from this module should return the following column labels:
column_labels = [
    "t_values",
    "x_values",
    "y_values",
    "vx_values",
    "vy_values",
    "ax_values",
    "ay_values",
]


class ColumnLabels(str, Enum):
    t_values = "t_values"
    x_values = "x_values"
    y_values = "y_values"
    vx_values = "vx_values"
    vy_values = "vy_values"
    ax_values = "ax_values"
    ay_values = "ay_values"


class NumericalMethods:
    def __init__(
        self, initial_x: float, initial_y: float, initial_vx: float, initial_vy: float
    ):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.initial_vx = initial_vx
        self.initial_vy = initial_vy

    def perform_euler(
        self,
        acc_function: Callable[[float, float], tuple[float, float]],
        iterations: int,
        delta_t: float,
    ) -> pd.DataFrame:
        x, y = self.initial_x, self.initial_y
        vx, vy = self.initial_vx, self.initial_vy

        rows = []
        for i in range(iterations):
            ax, ay = acc_function(x, y)
            rows.append((i * delta_t, x, y, vx, vy, ax, ay))

            x += vx * delta_t
            y += vy * delta_t

            vx += ax * delta_t
            vy += ay * delta_t

        return pd.DataFrame(rows, columns=list(ColumnLabels.__members__))

    def perform_euler_cromer(
        self,
        acc_function: Callable[[float, float], tuple[float, float]],
        iterations: int,
        delta_t: float,
    ) -> pd.DataFrame:
        x, y = self.initial_x, self.initial_y
        vx, vy = self.initial_vx, self.initial_vy

        rows = []
        for i in range(iterations):
            ax, ay = acc_function(x, y)
            rows.append((i * delta_t, x, y, vx, vy, ax, ay))

            vx += ax * delta_t
            vy += ay * delta_t

            x += vx * delta_t
            y += vy * delta_t

        return pd.DataFrame(rows, columns=list(ColumnLabels.__members__))

    def plot_trajectory(
        self,
        numerical_method: Callable,
        acc_function: Callable[[float, float], tuple[float, float]],
        iterations: int,
        delta_t: float,
        coordinate_limits: List[float] = None,
        coordinate_ticks: List[float] = None,
    ):
        df = numerical_method(
            self,
            acc_function=acc_function,
            iterations=iterations,
            delta_t=delta_t,
        )

        if coordinate_limits is None:
            lim_left, lim_right = (
                df[ColumnLabels.x_values].min(),
                df[ColumnLabels.x_values].max(),
            )
            lim_bottom, lim_top = (
                df[ColumnLabels.y_values].min(),
                df[ColumnLabels.y_values].max(),
            )

            coordinate_limits = [lim_left, lim_right, lim_bottom, lim_top]

        if coordinate_ticks is None:
            lim_left, lim_right = (
                df[ColumnLabels.x_values].min(),
                df[ColumnLabels.x_values].max(),
            )
            lim_bottom, lim_top = (
                df[ColumnLabels.y_values].min(),
                df[ColumnLabels.y_values].max(),
            )

            coordinate_ticks = [
                self._tick_interval(lim_right - lim_left),
                self._tick_interval(lim_top - lim_bottom),
            ]

        # Drawing the plot
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
        self._customized_plot(
            subplot=ax,
            dataframe=df,
            axis_scaling="equal",
            coordinate_ticks=coordinate_ticks,
            coordinate_limits=coordinate_limits,
            axis_label_offset=0.1,
        )

        ax.set_title(
            label=self._plot_title(
                numerical_method=numerical_method,
                iterations=iterations,
                delta_t=delta_t,
            ),
            fontsize=13,
            color="#222222",
            pad=14,
        )

        plt.tight_layout()

        return fig, ax

    @staticmethod
    def _customized_plot(
        subplot,
        dataframe: pd.DataFrame,
        axis_scaling: str,
        coordinate_ticks: List[float],
        coordinate_limits: List[float],
        axis_label_offset: float,
    ):
        """
        :param subplot: ax[0], ax[1], ax[2], etc.
        :param dataframe: the dataframe with plot data
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
            dataframe[ColumnLabels.x_values],
            dataframe[ColumnLabels.y_values],
            linewidth=1.2,
            alpha=0.85,
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
            arrowprops=dict(
                arrowstyle="-|>", mutation_scale=18, color="#222222", lw=1.5
            ),
            zorder=4,
        )

        subplot.annotate(
            "",
            xy=(0, ymax),
            xytext=(0, ymin),
            arrowprops=dict(
                arrowstyle="-|>", mutation_scale=18, color="#222222", lw=1.5
            ),
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

    @staticmethod
    def _tick_interval(axis_range: float, target_ticks: int = 10) -> float:
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

    @staticmethod
    def _plot_title(numerical_method: Callable, iterations: int, delta_t: float) -> str:
        if numerical_method is NumericalMethods.perform_euler:
            return (
                f"Траектория по метод на Ойлер с dt={delta_t} и N={iterations} итерации"
            )
        if numerical_method is NumericalMethods.perform_euler_cromer:
            return f"Траектория по метод на Ойлер-Кромер с dt={delta_t} и N={iterations} итерации"
        return ""
