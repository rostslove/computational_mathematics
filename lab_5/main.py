# This Python file uses the following encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import Newton as new


def draw(x, y, f):
    X = np.arange(x[0] - 1, x[len(x) - 1] + 1, .1)

    lagrange_f = [lagrange(x, y, t) for t in X]
    newton_f = [f(t) for t in X]

    plt.plot(X, lagrange_f, color='r', label='lagrange polynom')
    plt.plot(X, newton_f, color='b', label='newton polynom')

    plt.scatter(x, y)

    plt.legend()
    plt.show()


def lagrange(x, y, t):
    z = 0
    for j in range(len(y)):
        p1, p2 = 1, 1
        for i in range(len(x)):
            if i == j:
                continue
            else:
                p1 *= t - x[i]
                p2 *= x[j] - x[i]
        z += y[j] * p1 / p2
    return z

if __name__ == '__main__':
    while True:
        try:
            data_mode = int(input("Выберите способ ввода данных:\n1.Таблицей\n2.Формулой\n"))
            if data_mode != 1 and data_mode != 2:
                print("Выберите 1 или 2!")
            else:
                break
        except(ValueError, NameError, EOFError):
            print("Неверный формат")
    if data_mode == 1:
        while True:
            try:
                n = int(input("Введите количество точек:"))
                print("Введите точки в формате x y с переносом строки:")
                points = []
                for i in range(n):
                    x, y = map(float, input().split())
                    points.append([x, y])
                break
            except(ValueError, NameError, EOFError):
                print("Неверный формат")
        points = np.array(points)
        x, y = points[:, 0], points[:, 1]
        while True:
            try:
                arg = float(input("Введите аргумент: "))
                break
            except(ValueError, NameError, EOFError):
                print("Неверный формат")
        newton_poly = new.Newton(x, y)
        draw(x, y, newton_poly.get_newton_poly)
