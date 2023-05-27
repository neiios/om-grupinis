import math
import matplotlib.pyplot as plt
import numpy as np
from inspect import signature
from random import uniform
from plot import *


# https://www.sfu.ca/~ssurjano/grlee12.htmld
def gramacy_lee(x: float) -> float:
    return (math.sin(10 * math.pi * x) / (2 * x)) + ((x - 1) ** 4)


def plot_gramacy_lee() -> None:
    x = np.linspace(0.5, 2.5, 1000)
    y = np.array([gramacy_lee(val) for val in x])
    plt.plot(x, y)
    plt.show()


# https://www.sfu.ca/~ssurjano/camel6.html
def six_hump_camel(x1: float, x2: float) -> float:
    part_one = (4 - 2.1 * x1**2 + (x1**4 / 3)) * x1**2
    part_two = x1 * x2
    part_three = (-4 + 4 * x2**2) * x2**2
    return part_one + part_two + part_three


def plot_six_hump_camel() -> None:
    x1 = np.linspace(-2, 2, 100)
    x2 = np.linspace(-1, 1, 100)

    X1, X2 = np.meshgrid(x1, x2)

    six_hump_camel_vec = np.vectorize(six_hump_camel)
    Z = six_hump_camel_vec(X1, X2)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X1, X2, Z, cmap="viridis", alpha=0.7)

    # Find the global minimum using optimization techniques
    from scipy.optimize import minimize

    result = minimize(lambda x: six_hump_camel(x[0], x[1]), [0, 0])
    x_min, y_min = result.x
    z_min = result.fun

    # Plot the global minimum point
    ax.scatter(
        x_min,
        y_min,
        z_min,
        color="r",
        marker="o",
        s=50,
        label="Global Minimum",
        zorder=10,
        alpha=1.0,
    )

    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("Z")
    ax.set_title("3D Plot of the Six-Hump Camel Function")

    plt.legend()
    plt.show()


def acceptance_criterion(cur_fval: float, prev_fval: float, temperature: float) -> bool:
    delta_fval = cur_fval - prev_fval
    if delta_fval < 0:
        return True
    else:
        r = uniform(0, 1)
        if r < math.exp(-delta_fval / temperature):
            return True
        else:
            return False


def generate_new_point(X: list[float], bounds: [list[list]]) -> list[float]:
    X_new = []
    for i, x in enumerate(X):
        while True:
            x_new = x + uniform(-0.2, 0.2)
            if x_new >= bounds[i][0] and x_new <= bounds[i][1]:
                X_new.append(x_new)
                break

    return X_new


# The probability of convergence is not 1. Sometimes it won't find the global minimum.
def simulated_annealing(
    f, bounds: list[list], temp_max: float, verbose: bool = True
) -> list[list[float]]:
    var_count = len(signature(f).parameters)
    if var_count != len(bounds):
        print("Variable count doesn't match the bound count.")

    temp = temp_max

    X = [uniform(bounds[i][0], bounds[i][1]) for i in range(0, var_count)]
    E = f(*X)

    if verbose:
        print(f"Initial temperature: {temp}")
        print(f"Initial solution: {X}")
        print(f"Energy of initial solution: {E}")

    i = 0
    coordinates = [X]

    while temp > 0.0000000001:  # Why this many zeros? Don't ask questions.
        i = i + 1

        X_new = generate_new_point(X, bounds)  # TODO: How to choose this?
        E_new = f(*X_new)

        if np.linalg.norm(np.array(X_new) - np.array(X)) < 0.0001:
            break

        if acceptance_criterion(E_new, E, temp):
            X = X_new
            E = E_new

        coordinates.append(X)

        temp = temp * 0.95  # TODO: How to choose this? I think there is a better way.

    if verbose:
        print(f(*X))
    return coordinates


def plot_six_hump_camel() -> None:
    x1 = np.linspace(-2, 2, 100)
    x2 = np.linspace(-1, 1, 100)

    X1, X2 = np.meshgrid(x1, x2)

    six_hump_camel_vec = np.vectorize(six_hump_camel)
    Z = six_hump_camel_vec(X1, X2)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    ax.plot_surface(X1, X2, Z, cmap="viridis", alpha=0.7, zorder=1)

    # Find the global minimum using optimization techniques
    from scipy.optimize import minimize

    result = minimize(lambda x: six_hump_camel(x[0], x[1]), [0, 0])
    x_min, y_min = result.x
    z_min = result.fun

    # Plot the global minimum point
    ax.scatter(
        x_min,
        y_min,
        z_min,
        color="r",
        marker="o",
        s=50,
        label="Global Minimum",
        zorder=10,
        alpha=1.0,
    )

    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("Z")
    ax.set_title("3D Plot of the Six-Hump Camel Function")

    plt.legend()
    plt.show()


def main():
    GramacyLeePoints = simulated_annealing(
        f=gramacy_lee, temp_max=10000, bounds=[[0.5, 2.5]]
    )
    SixHumpCamelPoints = simulated_annealing(
        f=six_hump_camel, temp_max=10000, bounds=[[-2, 2], [-1, 1]]
    )
    drawGramacyLee(GramacyLeePoints)
    drawSixHumpCamel(SixHumpCamelPoints)


if __name__ == "__main__":
    main()
