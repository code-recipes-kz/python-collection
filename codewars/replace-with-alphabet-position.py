"""
Создаем строку alphabet, которая содержит все буквы английского алфавита в нижнем регистре. Это будет использоваться для проверки, является ли символ буквой из алфавита.

Создаем пустой список result, который будет использоваться для сохранения позиций букв в алфавите.

Используем цикл for для перебора каждого символа char в исходной строке text, приведенной к нижнему регистру с помощью метода lower().

Внутри цикла проверяем, является ли символ char буквой из алфавита с помощью условия if char in alphabet. Если символ является буквой, выполняем следующие действия:

Находим позицию символа char в алфавите с помощью метода index(), добавляем 1, так как индексы в Python начинаются с 0, и сохраняем результат в переменную position.

Преобразуем position в строку с помощью функции str(), чтобы можно было добавить его в список result.

Добавляем position в список result с помощью метода append().

По завершении цикла, возвращаем результат, объединив элементы списка result в строку с помощью метода join(), разделяя их пробелами.

В итоге функция alphabet_position() возвращает строку, содержащую позиции букв в алфавите для всех букв из исходной строки text, игнорируя все остальные символы.
"""

# tags: Strings, Fundamentals
# kyu: 6

def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Создаем строку с алфавитом
    result = []  # Создаем пустой список для результата
    for char in text.lower():  # Перебираем каждый символ в строке (приводим его к нижнему регистру)
        if char in alphabet:  # Проверяем, является ли символ буквой из алфавита
            position = alphabet.index(char) + 1  # Находим позицию символа в алфавите и прибавляем 1, так как индексы в Python начинаются с 0
            result.append(str(position))  # Добавляем позицию в список результата, преобразовав ее в строку
    return ' '.join(result)  # Возвращаем результат, объединив элементы списка в строку через пробел
