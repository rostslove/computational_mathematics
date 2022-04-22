import Dichotomy as d
import SimpleIteration as si
import Newton as n
import sys
import numpy as np
import Drawing as dr

while True:
    try:
        problem = int(input("Что надо решить?\n1.Линейное уравнение\n2.Система нелинейных уравнений\n"))
        if problem != 1 and problem != 2:
            print("Выберите 1 или 2!")
        else:
            break
    except(ValueError, NameError, EOFError):
            print("Неверный формат")
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
if problem == 1:
    while True:
        try:
            equation = int(input("Выберите уравнение для решения:\n1.x^3 - x + 4 = 0\n2.2x^5-x^4 + 2.74x^3 - 1.93x^2 - 15.28x - 3.72 = 0\n3.e^x * sin(x^3 + 0.67x) = 0\n"))
            if equation != 1 and equation != 2 and equation != 3:
                 print("Выберите одно из трех!")
            else:
                break
        except(ValueError, NameError, EOFError):
            print("Неверный формат")
    if equation == 1:
        func = lambda x: x ** 3 - x + 4
        title = "f(x) = x^3 - x + 4"
    elif equation == 2:
        func = lambda x: 2 * x ** 5 - x ** 4 + 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
        title = "f(x) = 2x^5-x^4 + 2.74x^3 - 1.93x^2 - 15.28x - 3.72"
    elif equation == 3:
        func = lambda x: np.exp(x) * np.sin(x ** 3 + 0.67 * x)
        title = "f(x) = e^x * sin(x^3 + 0.67x)"
    while True:
        try:
            m = int(input("Выберите метод для решения:\n1.Метод половинного деления\n2.Метод простых итераций\n"))
            if m != 1 and m != 2:
                print("Выберите 1 или 2!")
            else:
                break
        except(ValueError, NameError, EOFError):
            print("Неверный формат")
    if input_mode == 1:
        while True:
            try:
                a = float(input("Введите левую границу интервала: "))
                b = float(input("Введите правую границу интервала: "))
                eps = float(input("Введите точность: "))
                break
            except(ValueError, NameError, EOFError):
                print("Неверный формат")
    elif input_mode == 2:
        while True:
            try:
                with open(f"{input_file}", "r") as f:
                    a = float(f.readline())
                    b = float(f.readline())
                    eps = float(f.readline())
                break
            except(ValueError, NameError, EOFError):
                print("Неверный формат")
    if m == 1:
        method = d.Dichotomy(func, a, b, eps)
        dr.draw(method, title)
    elif m == 2:
        method = si.SimpleIteration(func, a, b, eps)
        dr.draw(method, title)
    if method.is_ok_status() == 1:
        print("Недопустимая точность")
        sys.exit()
    elif method.is_ok_status() == 2:
        print("В интервале нет корня")
        sys.exit()
    elif method.is_ok_status() == 3:
        print("Недопустимый интервал")
        sys.exit()
    elif method.is_ok_status() == 4:
        print("Не выполняется достаточное условие сходимости")
        sys.exit()
    res = method.solve()
elif problem == 2:
    while True:
        try:
            system = int(input("Выберите систему для решения:\n1.x^2 + y^2 = 4\n  y = 3x^2\n"))
            if system != 1:
                print("Выберите 1!")
            else:
                break
        except(ValueError, NameError, EOFError):
            print("Неверный формат")
    fu = lambda x, y: 4 - x ** 2 - y ** 2
    gu = lambda x, y: 3 * x ** 2 - y
    title = ["x ** 2 + y ** 2 - 4", "-3 * x ** 2 + y"]
    print("Решаем методом Ньютона:")
    if input_mode == 1:
        while True:
            try:
                x_0 = float(input("Введите первую координату начального приближения: "))
                y_0 = float(input("Введите вторую координату начального приближения: "))
                eps = float(input("Введите точность: "))
                break
            except(ValueError, NameError, EOFError):
                print("Неверный формат")
    elif input_mode == 2:
        while True:
            try:
                with open(f"{input_file}", "r") as f:
                    x_0 = float(f.readline())
                    y_0 = float(f.readline())
                    eps = float(f.readline())
                break
            except(ValueError, NameError, EOFError):
                print("Неверный формат")
    method = n.Newton(fu, gu, x_0, y_0, eps, title)
    method.draw(title)
    if method.is_ok_status() == 1:
        print("Недопустимая точность")
        sys.exit()
    res = method.solve()
if output_mode == 1 and problem == 1:
    if res[0] < a or res[0] > b:
        print("Не удалось найти корень в указанном интервале, ближайший корень указан в ответе")
    print(f"Корень: {res[0]}")
    print(f"Значение функции в корне: {res[1]}")
    print(f"Количество итераций: {res[2]}")
elif output_mode == 2 and problem == 1:
    with open(f"{output_file}", "w") as f:
        if res[0] < a or res[0] > b:
            f.write("Не удалось найти корень в указанном интервале, ближайший корень указан в ответе\n")
        f.write(f"Корень: {res[0]}\n")
        f.write(f"Значение функции в корне: {res[1]}\n")
        f.write(f"Количество итераций: {res[2]}")
elif output_mode == 1 and problem == 2:
    print("Таблица значений на каждой итерации:\n       x       |       y")
    for i in range(res[1]):
        print(res[0][i])
    print(f"Количество итераций: {res[1]}")
    print("Таблица ошибок на каждой итерации:\n         x       |       y")
    for i in range(res[1]):
        print(res[2][i])
else:
    with open(f"{output_file}", "w") as f:
        f.write("Таблица значений на каждой итерации:\n          x       |       y\n")
        for i in range(res[1]):
            f.write(f"{res[0][i]}\n")
        f.write(f"Количество итераций: {res[1]}\n")
        f.write("Таблица ошибок на каждой итерации:\n           x       |       y\n")
        for i in range(res[1]):
            f.write(f"{res[2][i]}\n")
