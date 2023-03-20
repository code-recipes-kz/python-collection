"""
В этом примере мы решаем уравнение sin(x) = x/2 с помощью метода простых итераций. Начальное приближение равно 1, а максимальное число итераций равно 100. Мы используем функцию g(x) = sin(x)/2 для итерационного процесса. Если разница между текущим значением и предыдущим значением меньше 1e-6, то мы считаем, что достигнута требуемая точность, и останавливаем итерационный процесс. В противном случае мы продолжаем итерации до тех пор, пока не достигнем максимального числа итераций. После окончания итерационного процесса мы выводим результат на экран.
"""

# Импортируем математическую библиотеку
import math

# Задаем уравнение, которое мы будем решать
def f(x):
    return math.sin(x)

# Задаем функцию, которую мы будем использовать для простых итераций
def g(x):
    return math.cos(x)

# Задаем начальное приближение и максимальное число итераций
x0 = 1
max_iter = 100
accuracy = 1e-6

# Итерационный процесс
for i in range(max_iter):
    x1 = g(x0)
    if abs(x1 - x0) < accuracy: # Проверяем, достигнута ли требуемая точность
        break
    x0 = x1

# Выводим результат
print("Корень уравнения: ", x0)