"""
Эта функция принимает массив из 10 целых чисел и преобразует его в формат номера телефона с помощью метода join() для
соединения цифр в строку и метода format() для форматирования строки в требуемом формате.
"""

# tags: Arrays, Strings, Regular Expressions, Algorithms
# kyu: 6

def create_phone_number(numbers):
    # Получаем первые три цифры номера телефона
    first_three = "".join(map(str, numbers[:3]))
    # Получаем следующие три цифры номера телефона
    next_three = "".join(map(str, numbers[3:6]))
    # Получаем последние четыре цифры номера телефона
    last_four = "".join(map(str, numbers[6:]))
    # Соединяем полученные данные в строку в формате номера телефона
    return "({}) {}-{}".format(first_three, next_three, last_four)