"""
В этом примере мы определяем функцию gauss_chebyshev, которая принимает в качестве аргументов функцию f, границы интегрирования a и b, а также порядок n формулы Гаусса-Чебышева. Функция вычисляет узлы Чебышева на интервале [-1, 1], переводит их на интервал [a, b], вычисляет соответствующие веса и суммирует взвешенные значения функции f в узлах. Возвращается результат умноженный на половину длины интервала [a, b].

В примере мы также определяем функцию f, которая мы будем интегрировать. Мы вычисляем определенный интеграл функции f на интервале [0, pi/2] с помощью формулы Гаусса-Чебышева порядка 10 и выводим результат на экран.
"""

import numpy as np

def gauss_chebyshev(f, a, b, n):
    """Вычисляет определенный интеграл функции f на интервале [a, b]
       с помощью формулы Гаусса-Чебышева порядка n.
    """
    x = np.cos(np.pi * (np.arange(1, n+1) - 0.5) / n) # вычисляем узлы Чебышева
    t = 0.5 * (b - a) * x + 0.5 * (b + a)              # переводим узлы на интервал [a, b]
    w = np.pi / n                                     # вычисляем веса
    integral = np.sum(w * f(t))                       # вычисляем сумму взвешенных значений функции
    return 0.5 * (b - a) * integral                    # умножаем на половину длины интервала

def f(x):
    return x  # Функция, которую мы будем интегрировать

a = 0.5  # Нижний предел интегрирования
b = 1  # Верхний предел интегрирования
n = 5  # Количество интервалов

integral = gauss_chebyshev(f, a, b, n)
print("Результат интегрирования:", integral)