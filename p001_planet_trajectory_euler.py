import matplotlib.pyplot as plt

from to_refactor.forces import acc_gravity
from utils.numerical_methods import perform_euler
from matplotlib.animation import FuncAnimation
from utils.plotting import plot_trajectory

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
