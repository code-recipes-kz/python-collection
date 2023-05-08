# tags: Regular expressions, Algorithms
# kyu: 6

def valid_phone_number(phone_number):
    if len(phone_number) != 14:  # Проверяем длину строки (должна быть 14 символов)
        return False
    if phone_number[0] != '(':  # Проверяем наличие открывающей скобки в начале строки
        return False
    if phone_number[4] != ')':  # Проверяем наличие закрывающей скобки на 5-й позиции
        return False
    if phone_number[5] != ' ':  # Проверяем наличие пробела на 6-й позиции
        return False
    if phone_number[9] != '-':  # Проверяем наличие дефиса на 10-й позиции
        return False
    if not phone_number[1:4].isdigit() or not phone_number[6:9].isdigit() or not phone_number[10:].isdigit():
        # Проверяем, что символы между скобками, после пробела и после дефиса - это только цифры
        return False
    return True