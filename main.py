import math
import matplotlib.pyplot as plt
import numpy as np
from inspect import signature
from random import uniform


# https://www.sfu.ca/~ssurjano/grlee12.html
def gramacy_lee(x: float) -> float:
    return (math.sin(10 * math.pi * x) / (2 * x)) + ((x - 1) ** 4)


def plot_gramacy_lee(FinalX: float, FinalY: float) -> None:
    x = np.linspace(0.5, 2.5, 1000)
    y = np.array([gramacy_lee(val) for val in x])
    plt.plot(x, y)
    plt.scatter(FinalX, FinalY, color="r", label="Global Minimum")
    plt.show()


def plot_temperature_iterations(temperature: list = [], iterations: list = []) -> None:
    plt.plot(iterations, temperature)
    plt.xlabel("Iterations")
    plt.ylabel("Temperature")
    plt.show()


# https://www.sfu.ca/~ssurjano/camel6.html
def six_hump_camel(x1: float, x2: float) -> float:
    part_one = (4 - 2.1 * x1**2 + (x1**4 / 3)) * x1**2
    part_two = x1 * x2
    part_three = (-4 + 4 * x2**2) * x2**2
    return part_one + part_two + part_three


def plot_six_hump_camel(X1final, X2final, Yfinal) -> None:
    x1 = np.linspace(-2, 2, 100)
    x2 = np.linspace(-1, 1, 100)

    X1, X2 = np.meshgrid(x1, x2)

    six_hump_camel_vec = np.vectorize(six_hump_camel)
    Z = six_hump_camel_vec(X1, X2)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X1, X2, Z, cmap="viridis")
    ax.scatter(X1final, X2final, Yfinal, color="r", label="Global minimum")

    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("Z")
    ax.set_title("3D Plot of the Six-Hump Camel Function")

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
) -> list[float]:
    temperatures = []
    iterations = []
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
    while temp > 0.0000000001:  # Why this many zeros? Don't ask questions.
        i = i + 1

        X_new = generate_new_point(X, bounds)  # TODO: How to choose this?
        E_new = f(*X_new)

        if (
            np.linalg.norm(np.array(X_new) - np.array(X)) < 0.0001
        ):  # TODO: do we need that?
            break

        if acceptance_criterion(E_new, E, temp):
            X = X_new
            E = E_new

        temperatures.append(temp)
        iterations.append(i)

        temp = temp * 0.95  # TODO: How to choose this? I think there is a better way.

    plot_temperature_iterations(temperatures, iterations)

    if verbose:
        print(f(*X))
    return X


def main():
    X = simulated_annealing(f=gramacy_lee, temp_max=10000, bounds=[[0.5, 2.5]])
    print("pirmas")
    final = gramacy_lee(X[0])
    plot_gramacy_lee(X, final)
    print("cia yra final")
    print(final)

    X = simulated_annealing(f=six_hump_camel, temp_max=10000, bounds=[[-2, 2], [-1, 1]])
    final2 = six_hump_camel(X[0], X[1])
    plot_six_hump_camel(X[0], X[1], final2)
    print(final2)
    print(X)


if __name__ == "__main__":
    main()
