from tabulate import tabulate

from plot import draw_gramacy_lee, draw_six_hump_camel, plot_temperature_iterations


def output_data(simulated_annealing, gramacy_lee, six_hump_camel):
    gramacy_lee_data = simulated_annealing(
        f=gramacy_lee, temp_max=10000, bounds=[[0.5, 2.5]]
    )

    six_hump_camel_data = simulated_annealing(
        f=six_hump_camel, temp_max=10000, bounds=[[-3, 3], [-2, 2]]
    )

    print_points(f=gramacy_lee, data=gramacy_lee_data)
    print_points(f=six_hump_camel, data=six_hump_camel_data)

    plot_minimization(gramacy_lee_data, six_hump_camel_data)

    experiment(
        simulated_annealing,
        gramacy_lee,
        [5000, 10000, 15000, 20000],
        bounds=[[0.5, 2.5]],
    )
    experiment(
        simulated_annealing,
        six_hump_camel,
        [5000, 10000, 15000, 20000],
        bounds=[[-3, 3], [-2, 2]],
    )


def print_points(f, data):
    points = data["points"]
    limited_data = points[:5] + points[-5:]

    print("Values of ", f.__name__)

    # for Gramacy Lee
    if f.__name__ == "gramacy_lee":
        headers = ["Index", "X", "Y"]

        indexes = list(range(1, 6)) + list(range(len(points) - 4, len(points) + 1))

        table_data = [
            [indexes[i], row[0], f(row[0])] for i, row in enumerate(limited_data)
        ]
    # for Six Hump Camel
    else:
        headers = ["Index", "X1", "X2", "Y"]

        indexes = list(range(1, 6)) + list(range(len(points) - 4, len(points) + 1))

        table_data = [
            [indexes[i], row[0], row[1], f(row[0], row[1])]
            for i, row in enumerate(limited_data)
        ]

    print(tabulate(table_data, headers, tablefmt="grid"))


def plot_minimization(gramacy_lee_data, six_hump_camel_data):
    draw_gramacy_lee(gramacy_lee_data["points"])
    draw_six_hump_camel(six_hump_camel_data["points"])

    plot_temperature_iterations(gramacy_lee_data["temperatures"])
    plot_temperature_iterations(six_hump_camel_data["temperatures"])


def experiment(simulated_annealing, f, temperatures, bounds):
    data = {"minimums": [], "iterations": []}

    print("Values of ", f.__name__)

    for temperature in temperatures:
        tempData = simulated_annealing(f, bounds, temperature)
        data["minimums"].append(tempData["minimum"])
        data["iterations"].append(tempData["iterations"])

    table_data = []
    # for Gramacy Lee
    if f.__name__ == "gramacy_lee":
        headers = ["Temperature", "min X", "min Y", "Iterations"]

        for temperature, minimum, iterations in zip(
            temperatures, data["minimums"], data["iterations"]
        ):
            x = minimum[0][0]
            y = minimum[1]
            table_data.append([temperature, x, y, iterations])
    # for Six Hump Camel
    else:
        headers = ["Temperature", "min X1", "min X2", "min Y", "Iterations"]

        for temperature, minimum, iterations in zip(
            temperatures, data["minimums"], data["iterations"]
        ):
            x1 = minimum[0][0]
            x2 = minimum[0][1]
            y = minimum[1]
            table_data.append([temperature, x1, x2, y, iterations])
    print(tabulate(table_data, headers, tablefmt="grid"))
