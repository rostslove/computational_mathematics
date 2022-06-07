import GaussMethod as gm
import numpy as np
import matplotlib.pyplot as plt

def draw(points):
    X = np.linspace(points[0][0] - 1, points[len(points)-1][0] + 1)
    lin1, lin2, lin3 = linear_approx(points)
    linear = lambda x: lin1[0] + lin1[1] * x
    q1, q2, q3 = quadratic_approx(points)
    quadratic = lambda x: q1[0] + q1[1] * x + q1[2] * x ** 2
    c1, c2, c3 = cubic_approx(points)
    cubic = lambda x: c1[0] + c1[1] * x + c1[2] * x ** 2 + c1[3] * x ** 3
    d1, d2, d3 = degree_approx(points)
    degree = lambda x: d1[0] * x ** d1[1]
    log1, log2, log3 = log_approx(points)
    log = lambda x: log1[1] * np.log(x) + log1[0]
    coefs, fi, delta = exp_approx(points)
    exp = lambda x: coefs[0] * np.exp(coefs[1] * x)

    plt.plot(X, linear(X), color='r', label='a * x + b')
    plt.plot(X, quadratic(X), color='g', label='a * x^2 + b * x + c')
    plt.plot(X, cubic(X), color='b', label='a3 * x^3 + a2 * x^2 + a1 * x + a0')
    plt.plot(X, degree(X), color='y', label='a * x^b')
    plt.plot(X, exp(X), color='k', label='a * exp(b * x)')
    plt.plot(X, log(X), color='m', label='a * ln(x) + b')

    plt.scatter(points[:,0], points[:,1])

    plt.legend()

    plt.show()


def linear_approx(points):
    SX, SXX, SY, SXY = 0, 0, 0, 0
    for point in points:
        SX += point[0]
        SXX += point[0] ** 2
        SY += point[1]
        SXY += point[0] * point[1]
    d = SXX * len(points) - SX ** 2
    a = (SXY * len(points) - SX * SY) / d
    b = (SXX * SY - SX * SXY) / d
    fi = [a * points[i][0] + b for i in range(len(points))]
    delta = np.sqrt(np.average([(fi[i] - points[i][1]) ** 2 for i in range(len(points))]))
    coefs = [b, a]
    return coefs, fi, delta

def pirson_corr(points):
    up, down_1, down_2 = 0, 0, 0
    _x = np.average(points[:, 0])
    _y = np.average(points[:, 1])
    for i in range(len(points)):
        up += (points[i][0] - _x) * (points[i][1] - _y)
        down_1 += (points[i][0] - _x) ** 2
        down_2 += (points[i][1] - _y) ** 2
    r = up / np.sqrt(down_1 * down_2)
    return r

def quadratic_approx(points):
    SX, SXX, SXXX, SXXXX, SY, SXY, SXXY = 0, 0, 0, 0, 0, 0, 0
    for point in points:
        SX += point[0]
        SXX += point[0] ** 2
        SXXX += point[0] ** 3
        SXXXX += point[0] ** 4
        SY += point[1]
        SXY += point[0] * point[1]
        SXXY += point[0] ** 2 * point[1]
    matrix = [[len(points), SX, SXX, SY], [SX, SXX, SXXX, SXY], [SXX, SXXX, SXXXX, SXXY]]
    coefs = gm.solve_gauss(matrix)
    fi = [coefs[0] + coefs[1] * points[i][0] + coefs[2] * points[i][0] ** 2 for i in range(len(points))]
    delta = np.sqrt(np.average([(fi[i] - points[i][1]) ** 2 for i in range(len(points))]))
    return coefs, fi, delta

def cubic_approx(points):
    SX, SX2, SX3, SX4, SX5, SX6, SY, SXY, SX2Y, SX3Y = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for point in points:
        SX += point[0]
        SX2 += point[0] ** 2
        SX3 += point[0] ** 3
        SX4 += point[0] ** 4
        SX5 += point[0] ** 5
        SX6 += point[0] ** 6
        SY += point[1]
        SXY += point[0] * point[1]
        SX2Y += point[0] ** 2 * point[1]
        SX3Y += point[0] ** 3 * point[1]
    matrix = [[len(points), SX, SX2, SX3, SY], [SX, SX2, SX3, SX4, SXY], [SX2, SX3, SX4, SX5, SX2Y], [SX3, SX4, SX5, SX6, SX3Y]]
    coefs = gm.solve_gauss(matrix)
    fi = [coefs[0] + coefs[1] * points[i][0] + coefs[2] * points[i][0] ** 2 + coefs[3] * points[i][0] ** 3 for i in
         range(len(points))]
    delta = np.sqrt(np.average(
        [(fi[i] - points[i][1]) ** 2 for i in
         range(len(points))]))
    return coefs, fi, delta

def degree_approx(points):
    copy = points.copy()
    for i in range(len(copy)):
        copy[i] = [np.log(copy[i][j]) for j in range(2)]
    coefs = linear_approx(copy)[0]
    coefs[0] = np.exp(coefs[0])
    fi = [coefs[0] * points[i][0] ** coefs[1] for i in range(len(points))]
    delta = np.sqrt(np.average([(fi[i] - points[i][1]) ** 2 for i in range(len(points))]))
    return coefs, fi, delta

def log_approx(points):
    copy = points.copy()
    for i in range(len(points)):
        copy[i][0] = np.log(copy[i][0])
    coefs = linear_approx(copy)[0]
    fi = [coefs[1] * np.log(points[i][0]) + coefs[0] for i in range(len(points))]
    delta = np.sqrt(np.average([(fi[i] - points[i][1]) ** 2 for i in range(len(points))]))
    return coefs, fi, delta

def exp_approx(points):
    copy = points.copy()
    for i in range(len(points)):
        copy[i][1] = np.log(copy[i][1])
    coefs = linear_approx(copy)[0]
    coefs[0] = np.exp(coefs[0])
    fi = [coefs[0] * np.exp(coefs[1] * points[i][0]) for i in range(len(points))]
    delta = np.sqrt(np.average([(fi[i] - points[i][1]) ** 2 for i in range(len(points))]))
    return coefs, fi, delta

if __name__ == '__main__':
    while True:
        try:
            input_mode = int(input("Выберите режим ввода:\n1.С клавиатуры\n2.Файл\n"))
            if input_mode != 1 and input_mode != 2:
                print("Выберите 1 или 2!")
            else:
                break
        except(ValueError, NameError, EOFError):
            print("Неверный формат")
    if input_mode == 2:
        while True:
            try:
                input_file = str(input("Введите имя файла: "))
                break
            except(ValueError, NameError, EOFError, FileNotFoundError):
                print("Неверный формат")
    while True:
        try:
            output_mode = int(input("Выберите режим вывода:\n1.Основной поток\n2.Файл\n"))
            if output_mode != 1 and output_mode != 2:
                print("Выберите 1 или 2!")
            else:
                break
        except(ValueError, NameError, EOFError):
            print("Неверный формат")
    if output_mode == 2:
        while True:
            try:
                output_file = str(input("Введите имя файла: "))
                break
            except(ValueError, NameError, EOFError, FileNotFoundError):
                print("Неверный формат")
    if input_mode == 1:
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
    elif input_mode == 2:
        while True:
            try:
                with open(f"{input_file}", "r") as f:
                    n = int(f.readline())
                    points = []
                    for i in range(n):
                        x, y = map(float, f.readline().split())
                        points.append([x, y])
                break
            except(ValueError, NameError, EOFError):
                print("Неверный формат")
    methods = [linear_approx, quadratic_approx, cubic_approx, exp_approx, log_approx, degree_approx]
    names = ["Линейная аппроксимация", "Квадратичная аппроксимация", "Кубическая аппроксимация", "Экспоненциальная аппроксимация", "Логарифмическая аппроксимация", "Степенная аппроксимация"]
    deltas = []
    points = np.array(points)
    if output_mode == 1:
        for i in range(len(methods)):
            coefs, fi, delta = methods[i](points)
            deltas.append(delta)
            print(names[i])
            print("Коэффициенты: ", coefs)
            print("Значения аппроксимирующей функции в заданных точках: ", fi)
            print("Среднеквадратичное отклонение: ", delta)
            if i == 0:
                print("Коэффициент корреляции Пирсона: ", pirson_corr(points))
        print("Минимальное среднеквадратичное отклонение: ", min(deltas))
    else:
        with open(f"{output_file}", "w") as f:
            for i in range(len(methods)):
                coefs, fi, delta = methods[i](points)
                deltas.append(delta)
                f.write(str(names[i]) + '\n')
                f.write("Коэффициенты: "+ str(coefs) + '\n')
                f.write("Значения аппроксимирующей функции в заданных точках: "+ str(fi) + '\n')
                f.write("Среднеквадратичное отклонение: " + str(delta) + '\n')
                if i == 0:
                    f.write("Коэффициент корреляции Пирсона: " + str(pirson_corr(points)) + '\n')
            f.write("Минимальное среднеквадратичное отклонение: " + str(min(deltas)))
    draw(points)