from tabulate import tabulate

from plot import (
    draw_gramacy_lee,
    draw_six_hump_camel,
    plot_temperature_iterations,
    plot_iteration_functionvalue
)


def output_data(simulated_annealing, gramacy_lee, six_hump_camel):
    gramacy_lee_data = simulated_annealing(
        f=gramacy_lee, temp_max=10000, bounds=[[0.5, 2.5]]
    )

    six_hump_camel_data = simulated_annealing(
        f=six_hump_camel, temp_max=10000, bounds=[[-2, 2], [-1, 1]]
    )

    print_point_table(f=gramacy_lee, data=gramacy_lee_data)
    print_point_table(f=six_hump_camel, data=six_hump_camel_data)
    plot_iteration_functionvalue(f=gramacy_lee, data=gramacy_lee_data)
    plot_iteration_functionvalue(f=six_hump_camel, data=six_hump_camel_data)

    draw_gramacy_lee(gramacy_lee_data["points"])
    draw_six_hump_camel(six_hump_camel_data["points"])
    plot_temperature_iterations(gramacy_lee_data["temperatures"])
    plot_temperature_iterations(six_hump_camel_data["temperatures"])

    draw_six_hump_camel(only_save_surface=True)
    draw_six_hump_camel(only_save_surface=True, bounds=[[-3, 3], [-2, 2]])

    experiment(
        simulated_annealing,
        gramacy_lee,
        [10, 100, 1000, 2000, 5000, 10000, 1000000],
        bounds=[[0.5, 2.5]],
    )
    experiment(
        simulated_annealing,
        six_hump_camel,
        [10, 100, 1000, 2000, 5000, 10000, 1000000],
        bounds=[[-2, 2], [-1, 1]],
    )

    print_comparison(gramacy_lee_data, six_hump_camel_data)


def print_point_table(f, data):
    points = data["points"]
    limited_data = points[:5] + points[-5:]

    print(f"Pirmos ir paskutinės penkios iteracijos ({f.__name__})")

    # for Gramacy Lee
    if f.__name__ == "gramacy_lee":
        headers = ["Iteracija", "X", "Y"]

        indexes = list(range(1, 6)) + list(range(len(points) - 4, len(points) + 1))

        table_data = [
            [indexes[i], row[0], f(row[0])] for i, row in enumerate(limited_data)
        ]
    # for Six Hump Camel
    else:
        headers = ["Iteracija", "X1", "X2", "Y"]

        indexes = list(range(1, 6)) + list(range(len(points) - 4, len(points) + 1))

        table_data = [
            [indexes[i], row[0], row[1], f(row[0], row[1])]
            for i, row in enumerate(limited_data)
        ]

    print(tabulate(table_data, headers, tablefmt="rounded_grid"))


def experiment(simulated_annealing, f, temperatures, bounds):
    data = {"minimums": [], "iterations": []}

    print(f"Rezultatai pradedant iš skirtingų temperatūros reikšmių ({f.__name__})")

    for temperature in temperatures:
        tempData = simulated_annealing(f, bounds, temperature)
        data["minimums"].append(tempData["minimum"])
        data["iterations"].append(tempData["iterations"])

    table_data = []
    # for Gramacy Lee
    if f.__name__ == "gramacy_lee":
        headers = ["Temperatūra", "min X", "min Y", "Iteracijų sk."]

        for temperature, minimum, iterations in zip(
                temperatures, data["minimums"], data["iterations"]
        ):
            x = minimum[0][0]
            y = minimum[1]
            table_data.append([temperature, x, y, iterations])
    # for Six Hump Camel
    else:
        headers = ["Temperatūra", "min X1", "min X2", "min Y", "Iteracijų sk."]

        for temperature, minimum, iterations in zip(
                temperatures, data["minimums"], data["iterations"]
        ):
            x1 = minimum[0][0]
            x2 = minimum[0][1]
            y = minimum[1]
            table_data.append([temperature, x1, x2, y, iterations])
    print(tabulate(table_data, headers, tablefmt="rounded_grid"))


def print_comparison(gramacy_lee_data, six_hump_camel_data):
    formatted_gramacy_lee_min = gramacy_lee_data['minimum'][0] + [gramacy_lee_data['minimum'][1]]
    formatted_six_hump_camel_min = six_hump_camel_data['minimum'][0] + [six_hump_camel_data['minimum'][1]]

    table_data = [
        ['Algoritmas', ' Minimumo taškas', ' Minimali reikšmė', 'Iteracijų'],
        ['Gramacy Lee', formatted_gramacy_lee_min[:-1], formatted_gramacy_lee_min[-1], gramacy_lee_data['iterations']],
        ['Six-Hump Camel', formatted_six_hump_camel_min[:-1], formatted_six_hump_camel_min[-1],
         six_hump_camel_data['iterations']]
    ]
    print("Rezultatų palyginimai")
    print(tabulate(table_data, headers='firstrow', tablefmt="rounded_grid"))
