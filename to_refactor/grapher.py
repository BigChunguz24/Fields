import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

r = 3

fig, ax = plt.subplots()
ax.axis([-10, 10, -10, 10])
ax.set_aspect("equal")

t = np.linspace(0, 2 * np.pi, 1000)
x = r * np.cos(t)
y = r * np.sin(t)

ax.plot(x, y)

(point,) = ax.plot(0, 1, marker="o")


def circle(phi):
    return np.array([r * np.cos(phi), r * np.sin(phi)])


def update(phi):
    x_, y_ = circle(phi)
    point.set_data([x_], [y_])
    return (point,)


ani = FuncAnimation(
    fig=fig,
    func=update,
    interval=10,
    blit=True,
    repeat=True,
    frames=np.linspace(0, 2 * np.pi, 360, endpoint=False),
)

plt.show()
