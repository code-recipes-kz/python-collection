import math

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Решает нелинейное уравнение f(x) = 0
    с помощью метода Ньютона.
    f - функция, для которой ищется корень
    df - производная функции f
    x0 - начальное приближение
    tol - допустимая погрешность
    max_iter - максимальное число итераций

    Возвращает корень уравнения и число итераций.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i
        dfx = df(x)
        if dfx == 0:
            break
        x = x - fx / dfx
    return None, i

# Пример использования функции newton_method
# Решение уравнения x^2 - 2 = 0
f = lambda x: x**2 - 2
df = lambda x: 2*x
x0 = 1.0
root, num_iter = newton_method(f, df, x0)
if root is not None:
	print(f"Корень уравнения: {root}")
	print(f"Число итераций: {num_iter}")
else:
	print("Решение не найдено.")
