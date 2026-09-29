import matplotlib.pyplot as plt

from classes.NumericalMethods import NumericalMethods
from to_refactor.forces import acc_gravity
from matplotlib.animation import FuncAnimation

if __name__ == "__main__":
    animate = False
    iterations = 10000
    delta_t = 0.010

    # Initial coordinates and initial velocities
    x, y = 0.500, 0.000
    vx, vy = 0.000, 1.630

    planet_trajectory = NumericalMethods(initial_x=x, initial_y=y, initial_vx=vx, initial_vy=vy)

    fig, ax = planet_trajectory.plot_trajectory(numerical_method=NumericalMethods.perform_euler,
                                                acc_function=acc_gravity,
                                                iterations=iterations,
                                                delta_t=delta_t)


    if animate:
        (point,) = ax.plot([], [], "ro")

        df = planet_trajectory.perform_euler(acc_function=acc_gravity,
                                             iterations=iterations,
                                             delta_t=delta_t)
        def update(frame):
            point.set_data([df["x_values"][frame]], [df["y_values"][frame]])
            return (point,)

        ani = FuncAnimation(
            fig, update, frames=len(df["x_values"]), interval=0.01, blit=True
        )

    plt.show()
    plt.savefig(fname="static/planet_trajectory/trajectory.svg", format="svg")
