"""
Объявление функции secant_method, которая принимает в качестве аргументов функцию f, два начальных приближения x0 и x1, а также точность вычисления eps и максимальное количество итераций max_iter.

Создание цикла for i in range(max_iter), который повторяется max_iter раз.

Вычисление значения функции в x0 с помощью fx0 = f(x0).

Вычисление значения функции в x1 с помощью fx1 = f(x1).

Вычисление нового приближения x2 по методу секущих: x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0). Здесь мы используем формулу (x1 - x0) / (f(x1) - f(x0)) для нахождения углового коэффициента секущей, а затем вычитаем эту величину из x1 для получения нового приближения.

Проверяем, достигнута ли нужная точность: if abs(x2 - x1) < eps. Если это так, мы нашли корень и возвращаем его: return x2.

Перемещаем первое начальное приближение на место второго: x0 = x1.

Перемещаем второе начальное приближение на место нового приближения: x1 = x2.

Если не удалось найти корень за максимальное количество итераций, возбуждаем исключение с помощью raise ValueError("Метод не сошелся за {} итераций".format(max_iter)).

В конце концов, если весь цикл завершился без ошибок и без возврата результата на шаге 6, метод не сошелся, и возбуждено исключение.
"""

def secant_method(f, x0, x1, eps=1e-8, max_iter=100):
    """
    Решает нелинейное уравнение f(x) = 0 методом секущих.

    :param f: функция, для которой ищется корень
    :param x0: начальное приближение
    :param x1: другое начальное приближение
    :param eps: точность вычисления (по умолчанию 1e-8)
    :param max_iter: максимальное количество итераций (по умолчанию 100)
    :return: корень уравнения f(x) = 0
    """
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        if abs(x2 - x1) < eps:
            return x2
        x0 = x1
        x1 = x2
    raise ValueError("Метод не сошелся за {} итераций".format(max_iter))

f = lambda x: x**2 - 3
x0 = 1.0
x1 = 2.0
root = secant_method(f, x0, x1)
print("Корень уравнения: {}".format(root))