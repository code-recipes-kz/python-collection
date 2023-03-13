import numpy as np

# Определяем матрицу системы уравнений
A = np.array([[2.7, 3.3, 1.3], [3.5, -1.7, 2.8], [4.1, 5.8, -1.7]])
# Определяем столбец свободных членов
B = np.array([2.1, 1.7, 0.8])

# Прямой ход метода Гаусса
n = len(B)
for i in range(n):
    # Поиск максимального элемента в столбце i
    maxEl = abs(A[i][i])
    maxRow = i
    for k in range(i + 1, n):
        if abs(A[k][i]) > maxEl:
            maxEl = abs(A[k][i])
            maxRow = k
    # Обмен строками
    for k in range(i, n):
        tmp = A[maxRow][k]
        A[maxRow][k] = A[i][k]
        A[i][k] = tmp
    tmp = B[maxRow]
    B[maxRow] = B[i]
    B[i] = tmp
    # Приведение к верхнетреугольному виду
    for k in range(i + 1, n):
        c = -A[k][i] / A[i][i]
        for j in range(i, n):
            if i == j:
                A[k][j] = 0
            else:
                A[k][j] += c * A[i][j]
        B[k] += c * B[i]

# Обратный ход метода Гаусса
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]

# Вывод результата
print("Решение системы уравнений:")
print(x)