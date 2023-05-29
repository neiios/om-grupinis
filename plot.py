import matplotlib.pyplot as plt
import numpy as np


# Gramacy Lee version with numpy functions
def gramacy_lee(x: float) -> float:
    return (np.sin(10 * np.pi * x) / (2 * x)) + ((x - 1) ** 4)


def six_hump_camel(x1: float, x2: float) -> float:
    part_one = (4 - 2.1 * x1**2 + (x1**4 / 3)) * x1**2
    part_two = x1 * x2
    part_three = (-4 + 4 * x2**2) * x2**2
    return part_one + part_two + part_three


def draw_gramacy_lee(points):
    points = [point[0] for point in points]
    fig, ax = plt.subplots()

    x = np.array(points)
    y = gramacy_lee(x)

    for i, point in enumerate(zip(x, y)):
        if i == len(points) - 1:
            ax.scatter(point[0], point[1], zorder=3, s=60, color="red")
            continue
        if i == 0:
            ax.scatter(point[0], point[1], zorder=3, s=60, color="forestgreen")

        ax.scatter(
            x[:-1],
            y[:-1],
            zorder=2,
            s=30,
            facecolors="none",
            edgecolors="royalblue",
        )

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_position(("data", -1))
    ax.spines["left"].set_position(("data", 0.5))
    ax.tick_params(axis="both", which="both", length=0)
    ax.xaxis.get_major_ticks()[0].label1.set_visible(False)

    x = np.linspace(-1, 2.5, 10000)
    y = gramacy_lee(x)
    plt.plot(x, y, zorder=1)
    plt.xlim((0.5, 2.5))
    plt.ylim((-1, 5))
    plt.savefig("main_gramacy_lee.png")
    plt.show()


def draw_six_hump_camel(
    points=[], bounds=[[-2, 2], [-1, 1]], only_show_surface=False
) -> None:
    points = np.array(points)

    x1 = np.linspace(bounds[0][0], bounds[0][1], 100)
    x2 = np.linspace(bounds[1][0], bounds[1][1], 100)

    X1, X2 = np.meshgrid(x1, x2)

    six_hump_camel_vec = np.vectorize(six_hump_camel)
    Z = six_hump_camel_vec(X1, X2)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d", computed_zorder=False)
    ax.plot_surface(X1, X2, Z, cmap="viridis", alpha=0.9, zorder=1)

    if only_show_surface:
        flat_bounds = np.array(bounds).flatten()
        plt.savefig(
            f"surface_[{','.join(str(x) for x in flat_bounds)}]_six_hump_camel.png"
        )
        return

    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    # Plot the points as a scatter plot
    ax.scatter(
        points[:, 0],
        points[:, 1],
        six_hump_camel(points[:, 0], points[:, 1]),
        facecolors="none",
        edgecolors="black",
        s=20,
        zorder=2,
    )

    ax.scatter(
        points[0][0],
        points[0][1],
        six_hump_camel(points[0][0], points[0][1]),
        s=60,
        zorder=3,
        color="forestgreen",
    )

    ax.scatter(
        points[-1][0],
        points[-1][1],
        six_hump_camel(points[-1][0], points[-1][1]),
        s=60,
        zorder=3,
        color="red",
    )

    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("f(x1, x2)")

    plt.savefig("main_six_hump_camel.png")
    plt.show()


def plot_temperature_iterations(temperature: list = []) -> None:
    iterations = list(range(len(temperature)))
    plt.plot(iterations, temperature)
    plt.xlabel("Iterations")
    plt.ylabel("Temperature")
    plt.savefig("temperature_change.png")
    plt.show()


def plot_iteration_functionvalue(f, data) -> None:
    y_values = []

    for point in data["points"]:
        y_values.append(f(*point))

    iterations = list(range(len(y_values)))

    plt.figure()
    plt.title(f.__name__)
    plt.plot(iterations, y_values)
    plt.xlabel("Iterations")
    plt.ylabel("Function value")
    plt.show()
