import math
import matplotlib.pyplot as plt
import numpy as np


# https://www.sfu.ca/~ssurjano/grlee12.html
def gramacy_lee(X: list) -> float:
    return math.sin(10 * math.pi * X[0]) / 2 * X[0] + (X[0] - 1) ** 4


def plot_gramacy_lee() -> None:
    x = np.linspace(0, math.pi, 1000)
    y = np.array([gramacy_lee([val]) for val in x])
    plt.plot(x, y)
    plt.show()


# https://www.sfu.ca/~ssurjano/camel6.html
def six_hump_camel(X: list) -> float:
    x1 = X[0]
    x2 = X[1]

    part_one = (4 - 2.1 * x1**2 + (x1**4 / 3)) * x1**2
    part_two = x1 * x2
    part_three = (-4 + 4 * x2**2) * x2**2
    return part_one + part_two + part_three


def plot_six_hump_camel() -> None:
    x1 = np.linspace(-2, 2, 100)
    x2 = np.linspace(-1, 1, 100)

    X1, X2 = np.meshgrid(x1, x2)
    Z = six_hump_camel([X1, X2])

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X1, X2, Z, cmap="viridis")

    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("Z")
    ax.set_title("3D Plot of the Six-Hump Camel Function")

    plt.show()


def main():
    plot_gramacy_lee()
    plot_six_hump_camel()


if __name__ == "__main__":
    main()
