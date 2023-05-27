import matplotlib.pyplot as plt

def simulated_annealing(
    f, bounds: list[list], temp_max: float, verbose: bool = True
) -> list[float]:
    # Function implementation...

    # Create lists to store the energy values and iteration numbers
    energy_values = []
    iterations = []

    # Function implementation...

    i = 0
    while temp > 0.0000000001:
        # Rest of the loop implementation...

        # Store the energy value and iteration number
        energy_values.append(E)
        iterations.append(i)

    # Plot the energy values over iterations
    plt.plot(iterations, energy_values)
    plt.xlabel('Iteration')
    plt.ylabel('Energy')
    plt.title('Simulated Annealing: Energy Minimization')
    plt.show()

    return X
