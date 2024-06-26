"""
Эта функция принимает два аргумента: a и b. Она возвращает новый список, который содержит все значения из списка a, которые не присутствуют в списке b.

Чтобы решить задачу, мы используем генератор списков и условное выражение. Генератор списков создает новый список на основе элементов списка a, которые удовлетворяют условию в условном выражении. Условное выражение проверяет, присутствует ли элемент списка a в списке b. Если элемент присутствует в списке b, то он не включается в новый список.
"""

# tags: Arrays, Fundamentals, Algorithms
# kyu: 6

def array_diff(a, b):
    return [x for x in a if x not in b]