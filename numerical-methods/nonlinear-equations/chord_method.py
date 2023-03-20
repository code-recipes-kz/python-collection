"""
В этом примере функция f(x) задается как x**3 - 2*x**2 + 4. Вы можете заменить эту функцию на свою, которую нужно решить. Обратите внимание, что метод хорд не гарантирует сходимость на всех интервалах, поэтому перед вызовом функции chord_method нужно убедиться, что функция f(x) меняет знак на интервале [a,b]. Если это не так, функция chord_method вызовет исключение ValueError.

Определяем функцию f(x), которую мы хотим решить.

Определяем функцию chord_method, которая решает нелинейное уравнение методом хорд.

Внутри функции chord_method сначала вычисляем значения функции f на концах интервала [a, b]:

Проверяем, что на интервале [a, b] функция f меняет знак. Если это не так, то метод хорд не гарантирует сходимость, и мы вызываем исключение ValueError.

Запускаем цикл, в котором вычисляем новую точку пересечения с осью x, используя формулу для метода хорд:

Вычисляем значение функции f в новой точке c:

Если значение функции в новой точке c достаточно близко к нулю (точность задана параметром tol), то мы считаем, что мы нашли решение, и возвращаем эту точку:

Если знак функции f в точке a совпадает со знаком функции f в точке c, то мы заменяем точку a на точку c и пересчитываем значение функции f в новой точке a:

Если знак функции f в точке a совпадает со знаком функции f в точке c, то мы заменяем точку a на точку c и пересчитываем значение функции f в новой точке a:

Если же знак функции f в точке a не совпадает со знаком функции f в точке c, то мы заменяем точку b на точку c и пересчитываем значение функции f в новой точке b:

Если мы дошли до конца цикла и не нашли решения, значит, мы превысили максимальное число итераций, и мы вызываем исключение RuntimeError.

В конце кода мы можем вызвать функцию chord_method и передать ей интервал, на котором мы ищем решение, а также задать точность вычислений и максимальное число итераций:
"""

def f(x):
    # Здесь нужно вставить функцию, которую нужно решить
    return x**3 - 4*x - 9

def chord_method(a, b, tol=1e-6, maxiter=1000):
    """
    Решает нелинейное уравнение f(x)=0 на интервале [a,b] с помощью метода хорд.
    tol - точность вычислений (абсолютная погрешность)
    maxiter - максимальное число итераций
    """
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("Метод хорд не гарантирует сходимость на данном интервале")
    for i in range(maxiter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        fc = f(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    raise RuntimeError("Достигнуто максимальное число итераций")

# Пример использования:
a = -10
b = 10
x = chord_method(a, b)
print("x =", x)
print("f(x) =", f(x))
