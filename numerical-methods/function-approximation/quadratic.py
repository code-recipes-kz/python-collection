import numpy as np
import matplotlib.pyplot as plt

def quadratic_approximation(x, y):
    # Создаем матрицу A для нашей системы уравнений
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    # Вычисляем вектор коэффициентов
    a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]
    # Возвращаем функцию вида ax^2 + bx + c
    return lambda x: a*x**2 + b*x + c

# Задаем нашу функцию
x = np.linspace(-5, 5, num=50)
y = x**2 + np.random.normal(0, 1, len(x))

# Аппроксимируем функцию
f = quadratic_approximation(x, y)

# Строим графики исходной функции и аппроксимации
plt.plot(x, y, 'o', label='Data')
plt.plot(x, f(x), label='Quadratic approximation')
plt.legend()
plt.show()