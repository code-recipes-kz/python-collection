def f(x):
    # функция, которую необходимо проинтегрировать
    return x

def trapezoidal_rule(f, a, b, n):
    # метод трапеций
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    return h * sum

a = 0.5  # нижний предел интегрирования
b = 1  # верхний предел интегрирования
n = 5  # количество трапеций

integral = trapezoidal_rule(f, a, b, n)

print("Интеграл методом трапеций:", integral)
