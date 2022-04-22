import numpy as np
import matplotlib.pyplot as plt
from sympy import Matrix, plot_implicit, symbols, Eq

class Newton:
    def __init__(self, f, g, x_0, y_0, eps, title):
        self.f = f
        self.g = g
        self.x_0 = x_0
        self.y_0 = y_0
        self.eps = eps
        self.title = title

    def is_ok_status(self):
        if self.eps <= 0:
            return 1


    def Jacobian(self):
        return Matrix([self.title[0], self.title[1]]).jacobian(['x', 'y'])

    def solve(self):
        x = self.x_0
        y = self.y_0
        iterations = 0
        values = []
        error_table = []
        while True:
            iterations += 1
            J = self.Jacobian().subs([('x', x), ('y', y)])
            F = [self.f(x, y), self.g(x, y)]
            dxy = np.linalg.solve(np.array(J).astype(np.float64), F)
            x_new = x + dxy[0]
            y_new = y + dxy[1]
            values.append([x_new, y_new])
            error_rate = [abs(x_new - x), abs((y_new - y))]
            error_table.append(error_rate)
            if max(error_rate) <= self.eps:
                break
            x = x_new
            y = y_new
        return values, iterations, error_table

    def draw(self, title):
        x, y = symbols('x y')
        p1 = plot_implicit(Eq((-1) * self.f(x, y), 0), show=False)
        p1.append(plot_implicit(Eq((-1) * self.g(x, y), 0), show=False, line_color='r')[0])
        p1.title = f"f(x,y) = {title[0]}\ng(x, y) = {title[1]}"
        plt.rcParams['figure.figsize'] = 10, 10
        p1.show()
