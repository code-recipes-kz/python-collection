"""
Создаем функцию comp(a, b), которая принимает на вход два массива a и b.
Проверяем, если a или b равны None, в таком случае возвращаем False, так как задание гласит, что если один из массивов равен None, то возвращаем False.
Создаем словарь dict_a, который будет использоваться для хранения квадратов чисел из a в качестве ключей и количества их повторений в качестве значений.
Итерируемся по массиву a с помощью цикла for и для каждого числа num вычисляем его квадрат и добавляем его в словарь dict_a. Если квадрат числа num уже присутствует в словаре, увеличиваем значение соответствующего ключа на 1, иначе добавляем новый ключ в словарь со значением 1.
После обработки всех чисел из a, переходим к проверке массива b.
Итерируемся по массиву b с помощью цикла for и для каждого числа num из b проверяем его наличие в словаре dict_a и его количество повторений.
Если число num присутствует в словаре dict_a и его количество повторений больше 0, уменьшаем значение соответствующего ключа на 1. Это делается для того, чтобы учесть повторения чисел в массиве b.
Если число num не присутствует в словаре dict_a или его количество повторений в словаре dict_a равно 0, возвращаем False, так как это означает, что не удалось найти соответствующий квадрат числа из a в массиве b.
Если все числа из b удалось найти в квадратах чисел из a, и их количество повторений совпало, возвращаем True, так как массивы a и b удовлетворяют условию задачи.
"""

# tags: Fundamentals
# kyu: 6

def comp(a, b):
    # Проверяем, если a или b равны None, в таком случае возвращаем False
    if a is None or b is None:
        return False

    # Создаем словарь, где ключами будут квадраты чисел из a, а значениями - количество их повторений
    dict_a = {}
    for num in a:
        square = num * num
        if square in dict_a:
            dict_a[square] += 1
        else:
            dict_a[square] = 1

    # Проверяем каждое число из b
    for num in b:
        if num in dict_a and dict_a[num] > 0:
            dict_a[num] -= 1
        else:
            return False

    # Если все числа из b удалось найти в квадратах чисел из a, и их количество совпало,
    # то возвращаем True, иначе - False
    return True
