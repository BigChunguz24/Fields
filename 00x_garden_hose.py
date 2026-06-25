import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core import frame

from forces import acc_gravity_uniform
from numerical_methods import perform_euler
from matplotlib.animation import FuncAnimation
from phys_utils_plotting import plot_customisation

animate = False
delta_t = 0.005

# Initial coordinates
x, y = 0.000, 0.000

# Angular velocity of garden hose and exit speed of water
omega = 0.500
v = 10.000

# Iterations (only look at motion until hose is vertical)
iterations = int(np.pi / 2 / omega / delta_t)

# Draw the plot
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

final_positions = []
for i in range(0, iterations, 1):
    time = i * delta_t

    vx = v * np.cos(omega * time)
    vy = v * np.sin(omega * time)

    # Calculated motion of each particle
    df = perform_euler(
        initial_x=x,
        initial_y=y,
        initial_vx=vx,
        initial_vy=vy,
        acc_function=acc_gravity_uniform,
        iterations=iterations - i,
        delta_t=delta_t,
    )

    # Plot the full motion of each particle
    plot_customisation(
        subplot=ax[0],
        dataframe=df,
        keyword_for_x="x_values",
        keyword_for_y="y_values",
        axis_scaling="equal",
        coordinate_ticks=[0.5, 0.5],
        coordinate_limits=[-1, 10, -5, 5],
        axis_label_offset=0.1,
    )

    final_positions.append(df.tail(1))

# Plot just the final trajectory
df = pd.concat(final_positions, ignore_index=True)
plot_customisation(
    subplot=ax[1],
    dataframe=df,
    keyword_for_x="x_values",
    keyword_for_y="y_values",
    axis_scaling="equal",
    coordinate_ticks=[0.5, 0.5],
    coordinate_limits=[-1, 10, -5, 5],
    axis_label_offset=0.1,
)

ax[0].set_title(
    label=f"Траектория на всички частици по метод на Ойлер"
    f"\nСкорост на маркуча v = {v}, omega = {omega}"
    f"\nПараметри: dt={delta_t} и N={iterations} итерации",
    fontsize=13,
    color="#222222",
    pad=14,
)

ax[1].set_title(
    label=f"Траектория на струята по метод на Ойлер"
    f"\nСкорост на маркуча v = {v}, omega = {omega}"
    f"\nПараметри: dt={delta_t} и N={iterations} итерации",
    fontsize=13,
    color="#222222",
    pad=14,
)

plt.tight_layout()
plt.savefig(fname="trajectory.svg", format="svg")

if animate:
    (point,) = ax.plot([], [], "ro")

    def update(frame):
        point.set_data([df["x_values"][frame]], [df["y_values"][frame]])
        return (point,)

    ani = FuncAnimation(
        fig, update, frames=len(df["x_values"]), interval=0.01, blit=True
    )

plt.show()
