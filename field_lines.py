import numpy as np
from matplotlib import pyplot as plt

from Vector import Vector
from physical_constants import k
from utils import distance_between_points

if __name__ == "__main__":
    N = 1500

    charge_value_1 = 1
    charge_value_2 = 1
    charge_value_3 = 1
    charge_value_4 = 5

    charge_position_1 = Vector(x=+1, y=0)
    charge_position_2 = Vector(x=-1, y=0)
    charge_position_3 = Vector(x=0, y=+1)
    charge_position_4 = Vector(x=0, y=-1)

    x = np.linspace(-10, 10, N)
    y = np.linspace(-10, 10, N)

    X, Y = np.meshgrid(x, y)

    V = np.zeros_like(X)

    for i in range(N):
        for j in range(N):
            position = Vector(x=X[i, j], y=Y[i, j])
            charge_distance_1 = distance_between_points(point_1=position, point_2=charge_position_1)
            charge_distance_2 = distance_between_points(point_1=position, point_2=charge_position_2)
            charge_distance_3 = distance_between_points(point_1=position, point_2=charge_position_3)
            charge_distance_4 = distance_between_points(point_1=position, point_2=charge_position_4)

            if charge_distance_1 == 0 or charge_distance_2 == 0 or charge_distance_3 == 0:
                continue
            V[i, j] = \
                k * charge_value_1 / charge_distance_1 + \
                k * charge_value_2 / charge_distance_2 + \
                k * charge_value_3 / charge_distance_3 + \
                k * charge_value_4 / charge_distance_4

    plt.contour(X, Y, V, levels=500)
    plt.colorbar(label="Potential")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.show()

    print("debug")