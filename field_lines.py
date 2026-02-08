import numpy as np
from matplotlib import pyplot as plt

from Vector import Vector
from physical_constants import k, eps

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

    # Create coordinate grid
    x = np.linspace(-10, 10, N)
    y = np.linspace(-10, 10, N)
    X, Y = np.meshgrid(x, y)

    # Create distance grid and potential grid
    charge_distance_1 = np.sqrt((X - charge_position_1.x)**2 + (Y - charge_position_1.y)**2)
    charge_distance_2 = np.sqrt((X - charge_position_2.x)**2 + (Y - charge_position_2.y)**2)
    charge_distance_3 = np.sqrt((X - charge_position_3.x)**2 + (Y - charge_position_3.y)**2)
    charge_distance_4 = np.sqrt((X - charge_position_4.x)**2 + (Y - charge_position_4.y)**2)
    V = np.zeros_like(X)

    # Make sure distances are non-zero
    charge_distance_1[charge_distance_1 < eps] = np.inf
    charge_distance_2[charge_distance_2 < eps] = np.inf
    charge_distance_3[charge_distance_3 < eps] = np.inf
    charge_distance_4[charge_distance_4 < eps] = np.inf

    # Add potentials to grid,
    V += \
        k * charge_value_1 / charge_distance_1 + \
        k * charge_value_2 / charge_distance_2 + \
        k * charge_value_3 / charge_distance_3 + \
        k * charge_value_4 / charge_distance_4

    plt.contour(X, Y, V, levels=1000)
    plt.colorbar(label="Potential")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.show()

    print("debug")
