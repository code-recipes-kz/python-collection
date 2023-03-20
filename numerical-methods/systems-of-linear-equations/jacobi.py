# Конечно! Для решения системы линейных алгебраических уравнений методом Якоби с помощью Python 3 нам понадобится библиотека numpy.
# Вот код, который решает систему линейных алгебраических уравнений методом Якоби:
# В этом коде мы используем матрицу A, вектор b и начальное приближение x0, чтобы создать диагональную матрицу D и матрицу R. Затем мы используем эти матрицы для создания матрицы T и вектора c, которые используются для итерационного процесса.
# Мы выполняем итерационный процесс до тех пор, пока разница между текущим приближением x и предыдущим приближением x_new меньше заданной точности eps. Когда мы достигаем достаточно точного решения, мы выводим результат на экран.
# Этот код можно адаптировать для любой системы линейных алгебраических уравнений, заменив матрицу A и вектор b на соответствующие значения вашей системы.

import numpy as np

# Создаем матрицу коэффициентов
A = np.array([[4, -1, 0, 3],
              [1, 15.5, 3, 8],
              [0, -1.3, -4, 1.1],
              [14, 5, -2, 30]])

# Создаем вектор правой части
b = np.array([1, 1, 1, 1])

# Создаем начальное приближение
x0 = np.array([0, 0, 0, 0])

# Максимальное число итераций
max_iter = 1000

# Задаем точность вычислений
eps = 0.01

# Получаем размеры матрицы A
n, m = A.shape

# Создаем диагональную матрицу D и матрицу R
D = np.zeros((n, n))
R = np.zeros((n, n))

# Заполняем матрицы D и R
for i in range(n):
    for j in range(n):
        if i == j:
            D[i][j] = A[i][j]
        else:
            R[i][j] = A[i][j]

# Вычисляем обратную диагональную матрицу D_inv
D_inv = np.linalg.inv(D)

# Создаем матрицу T и вектор c
T = -D_inv.dot(R)
c = D_inv.dot(b)

# Начинаем итерационный процесс
x = x0
for i in range(max_iter):
    x_new = T.dot(x) + c
    if np.linalg.norm(x_new - x) < eps:
        break
    x = x_new

print("Решение системы:")
print(x)