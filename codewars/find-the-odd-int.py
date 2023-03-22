def find_it(arr):
    """
    Функция находит число, которое встречается в массиве нечётное число раз.
    """
    for num in arr:
        if arr.count(num) % 2 != 0:
            return num