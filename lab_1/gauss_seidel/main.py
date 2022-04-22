import matrix_processing as mp
import gauss_seidel as gs

import numpy as np
import sys

select = str(input("Введите режим ввода данных: файл или ввод \n"))
if select == "ввод":
    try:
        n = int(input("Введите количество уравнений в СЛАУ: "))
        print("Введите матрицу коэффициентов со свободными членами: ")
        A = [[float(i) for i in input().split()] for j in range(n)]
        eps = float(input("Введите точность: "))
        if eps <= 0:
            print("Неверная точность")
            sys.exit()
    except ValueError:
        print("\nНеверный формат ввода")
        sys.exit()
elif select == "файл":
    file_name = str(input("Введите имя файла: "))
    try:
        with open(f"{file_name}", "r") as f:
            n = int(f.readline())
            A = [[float(i) for i in f.readline().split()] for j in range(n)]
            eps = float(f.readline())
            if eps <= 0:
                print("Неверная точность")
                sys.exit()
    except(FileNotFoundError, ValueError):
        print("\nТакого файла нет или неверный формат данных")
        sys.exit()
else:
    print("Неверный режим ввода, попробуйте еще раз")
    sys.exit()
A = np.array(A)
det = mp.det(A[:, :n])
print(f"Определитель равен: {det}")
if det == 0:
    print("Вырожденная матрица коэффициентов")
    sys.exit()
if not mp.diagonal_predominance_check(A):
    print("В матрице нет диагонального преобладания")
    if not mp.diagonal_predominance_status(A[:, :n]):
        print("Диагональное преобладание в матрице не может быть достигнуто")
        sys.exit()
    print("Приводим к виду диагонального преобладания")
    A = np.array(mp.diagonal_predominance_transform(A))
A, b = A[:, :n], A[:, n]
x, iterations, error_rate_table = gs.gauss_seidel(A, b, eps)
print("Решение:\n" + f"Вектор переменных: {x}\n"
      + f"Количество итераций: {iterations}\n"
      + "Таблица погрешностей:")
for row in error_rate_table:
    print(row)
