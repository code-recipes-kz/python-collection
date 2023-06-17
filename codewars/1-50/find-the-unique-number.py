"""
Создаем функцию find_uniq(arr), которая принимает на вход список чисел arr в качестве аргумента.
Создаем словарь counts для подсчета количества вхождений каждого числа в массиве. Словарь будет использоваться для хранения чисел в качестве ключей и их счетчиков в качестве значений.
Проходим по каждому числу num в массиве arr с помощью цикла for.
Внутри цикла проверяем, есть ли число num уже в словаре counts с помощью условного оператора if num in counts:.
Если число num уже есть в словаре counts, то увеличиваем его счетчик на 1 с помощью оператора counts[num] += 1. Это выполняется для подсчета количества вхождений каждого числа в массиве.
Если числа num нет в словаре counts, то добавляем его в словарь с счетчиком равным 1, используя оператор counts[num] = 1. Это выполняется для начальной инициализации счетчика числа, если оно встречается впервые.
После завершения цикла, у нас есть словарь counts, содержащий количество вхождений каждого числа в массиве arr.
Проходим по словарю counts с помощью цикла for и проверяем, какое число имеет счетчик равный 1. Это означает, что данное число встречается только один раз и является уникальным числом в массиве.
Как только находим число с счетчиком равным 1, возвращаем это число в качестве результата функции с помощью оператора return num.
В основной части кода примеры использования функции find_uniq(arr) с разными массивами arr1 и arr2 выводят уникальное число на экран.
"""

# tags: Fundamentals, Algorithms, Arrays
# kyu: 6

def find_uniq(arr):
    """
    Функция находит уникальное число в массиве, где все числа равны, за исключением одного.

    Аргументы:
    arr -- список чисел (массив)

    Возвращаемое значение:
    Уникальное число в массиве.
    """
    # Создаем словарь для подсчета количества вхождений каждого числа в массиве
    counts = {}
    # Проходим по каждому числу в массиве
    for num in arr:
        # Если число уже есть в словаре, увеличиваем его счетчик на 1
        if num in counts:
            counts[num] += 1
        # Иначе добавляем число в словарь с счетчиком равным 1
        else:
            counts[num] = 1
    # Проходим по словарю и находим число с счетчиком равным 1, это и будет уникальное число
    for num, count in counts.items():
        if count == 1:
            return num