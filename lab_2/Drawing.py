import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np

def draw(self, title):
    add = 2
    if abs(self.a - self.b) < 1:
        add = 0.2
    x = np.linspace(self.a - add, self.b + add, 100)
    y = self.f(x)
    fig = plt.figure()
    ax = axisartist.Subplot(fig, 111)
    fig.add_axes(ax)

    ax.axis[:].set_visible(False)

    ax.axis['x'] = ax.new_floating_axis(0, 0)
    ax.axis['y'] = ax.new_floating_axis(1, 0)

    ax.axis['x'].set_axis_direction('top')
    ax.axis['y'].set_axis_direction('left')

    ax.plot(x, y)
    plt.title(f"{title}")

    a = ax.scatter(self.a, 0)
    b = ax.scatter(self.b, 0)

    handles = [a, b]
    labels = ["a", "b"]
    ax.legend(handles, labels)

    ax.grid()
    plt.show()