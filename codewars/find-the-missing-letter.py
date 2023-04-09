"""
Функция find_missing_letter проходит по массиву chars и сравнивает коды ASCII соседних букв. Если разница между кодами ASCII больше 1, то это означает, что есть отсутствующая буква, и она возвращается в виде символа с помощью функции chr().
"""

# tags: Mathematics, Algorithms
# kyu: 6

def find_missing_letter(chars):
    """
    Функция принимает на вход массив последовательных букв и возвращает отсутствующую букву.
    """
    for i in range(len(chars)-1):
        if ord(chars[i+1]) - ord(chars[i]) > 1:
            # Если разница между ASCII кодами соседних букв больше 1, то возвращаем пропущенную букву
            return chr(ord(chars[i]) + 1)