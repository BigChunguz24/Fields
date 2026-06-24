import matplotlib.pyplot as plt

from forces import acc_gravity
from numerical_methods import perform_euler
from matplotlib.animation import FuncAnimation
from phys_utils_plotting import plot_customisation

animate = False
iterations = 10000
delta_t = 0.010

# Initial coordinates and initial velocities
x, y = 0.500, 0.000
vx, vy = 0.000, 1.630

df = perform_euler(initial_x=x,
                   initial_y=y,
                   initial_vx=vx,
                   initial_vy=vy,
                   acc_function=acc_gravity,
                   iterations=iterations,
                   delta_t=delta_t,
                   )

# Drawing the plot
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
plot_customisation(subplot=ax,
                   dataframe=df,
                   keyword_for_x="x_values",
                   keyword_for_y="y_values",
                   axis_scaling="equal",
                   coordinate_ticks=[0.5, 0.5],
                   coordinate_limits=[-4.2, 1.1, -2.1, 2],
                    axis_label_offset=0.1,
                   )

ax.set_title(label=f"Траектория по метод на Ойлер с dt={delta_t} и N={iterations} итерации",
             fontsize=13,
             color="#222222",
             pad=14,
             )

plt.tight_layout()
plt.savefig(fname="trajectory.svg", format="svg")

if animate:
    point, = ax.plot([], [], "ro")

    def update(frame):
        point.set_data([df["x_values"][frame]], [df["y_values"][frame]])
        return point,

    ani = FuncAnimation(fig, update, frames=len(df["x_values"]), interval=0.01, blit=True)

plt.show()
