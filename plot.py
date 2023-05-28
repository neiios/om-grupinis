import matplotlib.pyplot as plt
import numpy as np

# Gramacy Lee version with numpy functions
def gramacy_lee(x: float) -> float:
    return (np.sin(10 * np.pi * x) / (2 * x)) + ((x - 1) ** 4)

def six_hump_camel(x1: float, x2: float) -> float:
    part_one = (4 - 2.1 * x1 ** 2 + (x1 ** 4 / 3)) * x1 ** 2
    part_two = x1 * x2
    part_three = (-4 + 4 * x2 ** 2) * x2 ** 2
    return part_one + part_two + part_three

def draw_gramacy_lee(points):
    points = [point[0] for point in points]
    fig, ax = plt.subplots()

    indices = [0, 9, 19, 49, len(points) - 1]
    x = np.array([points[i] for i in indices])
    y = gramacy_lee(x)
    for i, point in enumerate(zip(x, y)):
        if i == len(indices) - 1:
            offset_x, offset_y = 5, 10
            bbox_props = dict(
                boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5
            )
            ax.scatter(point[0], point[1], color="red", zorder=3)
        else:
            offset_x, offset_y = 5, 10
            bbox_props = dict(
                boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5
            )
        ax.annotate(
            indices[i] + 1,
            (point[0], point[1]),
            xytext=(offset_x, offset_y),
            textcoords="offset points",
            bbox=bbox_props,
        )
        ax.scatter(x[:-1], y[:-1], zorder=2)

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
    plt.show()


def draw_six_hump_camel(points):
    points = np.array(points)

    indices = [0, 49, 199, len(points) - 1]
    points = np.array([points[i] for i in indices])

    x1 = np.linspace(-2, 2, 100)
    x2 = np.linspace(-1, 1, 100)

    X1, X2 = np.meshgrid(x1, x2)

    six_hump_camel_vec = np.vectorize(six_hump_camel)
    Z = six_hump_camel_vec(X1, X2)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d", computed_zorder=False)
    ax.plot_surface(X1, X2, Z, cmap="hsv", alpha=0.9, zorder=1)

    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    # Plot the function surface
    X1, X2 = np.meshgrid(np.linspace(0, 1, 50), np.linspace(0, 1, 50))
    Z = six_hump_camel(X1, X2)
    ax.plot_surface(X1, X2, Z, cmap="cool", alpha=1, zorder=0)

    # Plot the points as a scatter plot
    ax.scatter(
        points[:, 0],
        points[:, 1],
        six_hump_camel(points[:, 0], points[:, 1]),
        color="black",
        s=30,
        zorder=2,
    )

    # Add annotations for each point with a background
    for i, point in enumerate(points):
        offset_x = 0.09
        offset_y = 0.09
        label = str(indices[i] + 1)
        bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5)
        ax.text(
            point[0] + offset_x,
            point[1] + offset_y,
            six_hump_camel(*point),
            label,
            color="black",
            fontsize=8,
            zorder=2,
            bbox=bbox_props,
        )

    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("f(x1, x2)")

    plt.show()

def plot_temperature_iterations(temperature: list = []) -> None:
    iterations = list(range(len(temperature)))
    plt.plot(iterations, temperature)
    plt.xlabel("Iterations")
    plt.ylabel("Temperature")
    plt.show()

# aint used
# def plot2d(points, approaching_points=[9, 49, 99]):
#     points = np.array(points)
#     fig, ax = plt.subplots()
#     approaching_points.append(len(points) - 1)
#     x = np.arange(0, 2, 0.01)
#     y = np.arange(-1, 2, 0.01)
#     X, Y = np.meshgrid(x, y)
#     Z = -0.125 * X * Y * (1 - X - Y)
#     CS = ax.contour(X, Y, Z, 15, linewidths=0.3)
#     ax.clabel(CS, inline=True, fontsize=9)
#
#     x_points = [points[i][0] for i in approaching_points]
#     y_points = [points[i][1] for i in approaching_points]
#     ax.plot(x_points, y_points, "bo")
#
#     for i in approaching_points:
#         ax.annotate(
#             str(i + 1),
#             xy=(points[i][0], points[i][1]),
#             xytext=(7, 0),
#             textcoords="offset points",
#         )
#
#     ax.spines["right"].set_visible(False)
#     ax.spines["top"].set_visible(False)
#     ax.tick_params(axis="both", which="both", length=0)
#     ax.xaxis.get_major_ticks()[0].label1.set_visible(False)
#     plt.show()

#
# def plot_six_hump_camel(X1final, X2final, Yfinal) -> None:
#     x1 = np.linspace(-2, 2, 100)
#     x2 = np.linspace(-1, 1, 100)
#
#     X1, X2 = np.meshgrid(x1, x2)
#
#     six_hump_camel_vec = np.vectorize(six_hump_camel)
#     Z = six_hump_camel_vec(X1, X2)
#
#     fig = plt.figure(figsize=(8, 6))
#     ax = fig.add_subplot(111, projection="3d")
#     ax.plot_surface(X1, X2, Z, cmap="viridis")
#     ax.scatter(X1final, X2final, Yfinal, color="r", label="Global minimum")
#
#     ax.set_xlabel("X1")
#     ax.set_ylabel("X2")
#     ax.set_zlabel("Z")
#     ax.set_title("3D Plot of the Six-Hump Camel Function")
#
#     plt.show()