# tags: Regular Expressions, Strings, Algorithms
# kyu: 6

def solution(s):
    # Проверяем, что длина строки s больше 0
    if len(s) == 0:
        return []

    # Если длина строки s нечетная, то добавляем в конец строки символ '_'
    if len(s) % 2 != 0:
        s += "_"

    # Разбиваем строку на пары символов
    pairs = [s[i:i+2] for i in range(0, len(s), 2)]

    return pairs