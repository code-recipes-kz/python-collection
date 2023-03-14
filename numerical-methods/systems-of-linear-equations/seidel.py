# https://math.semestr.ru/optim/zeidel.php

from math import sqrt
import numpy as np

def seidel(A, b, eps):
    n = len(A)
    x = [.0 for i in range(n)]

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.max(np.abs(x_new - x)) <= eps
        x = x_new

    return x

A = np.array([[10, 1, 1], [2, 10, 2], [1, 1, 10]])
b = np.array([12, 14, 10])
x = np.array(0)

x = seidel(A, b, x)
print(x)