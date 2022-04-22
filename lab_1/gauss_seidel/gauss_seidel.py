import numpy as np

def gauss_seidel(A, b, eps):
  n = len(A)
  x = np.zeros(n) # начальное приближение
  error_rate_table = []
  iterations = 0
  while True:
    iterations += 1
    x_new = np.copy(x)
    for i in range(n):
        s1 = sum(A[i][j] * x_new[j] for j in range(i))
        s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x_new[i] = (b[i] - s1 - s2) / A[i][i]
    error_rate = [abs(x_new[i] - x[i]) for i in range(n)]
    error_rate_table.append(error_rate)
    if max(error_rate) <= eps:
      break
    x = x_new
  return x, iterations, error_rate_table