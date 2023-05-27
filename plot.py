import numpy as np
import matplotlib.pyplot as plt

# Gramacy Lee version with numpy functions
def gramacy_lee(x: float) -> float:
    return (np.sin(10 * np.pi * x) / (2 * x)) + ((x - 1) ** 4)

def configurePlot(ax):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data', -1))
    ax.spines['left'].set_position(('data', .5))
    ax.tick_params(axis='both', which='both', length=0)
    ax.xaxis.get_major_ticks()[0].label1.set_visible(False)

def drawGramacyLee(points, limit=True):
    points = [point[0] for point in points]
    fig, ax = plt.subplots()

    if limit is False:
        x = np.array(points)
        y = f(x)
        sizes = np.random.uniform(15, 100, len(points))
        colors = np.random.uniform(30, 86, len(points))

        ax.scatter(x, y, zorder=2, s=sizes, c=colors, vmin=0, vmax=100)
    else:
        indices = [0, 9, 19, 49, len(points)-1]
        x = np.array([points[i] for i in indices])
        y = gramacy_lee(x)
        for i, point in enumerate(zip(x, y)):
            if i == len(indices) - 1:
                offset_x, offset_y = 5, 10
                bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5)
                ax.scatter(point[0], point[1], color='red', zorder=3)
            else:
                offset_x, offset_y = 5, 10
                bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5)
            ax.annotate(indices[i] + 1, (point[0], point[1]), xytext=(offset_x, offset_y),
                        textcoords='offset points', bbox=bbox_props)
        ax.scatter(x[:-1], y[:-1], zorder=2)

    configurePlot(ax)

    x = np.linspace(-1, 2.5, 10000)
    y = gramacy_lee(x)
    plt.plot(x, y, zorder=1)
    # plt.grid(alpha=.6, linestyle='--')
    plt.xlim((0.5, 2.5))
    plt.ylim((-1, 5))
    plt.title("Gramacy & Lee (2012) funkcijos minimizavimas", y=1.04)
    plt.show()
