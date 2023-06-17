"""
Функция to_weird_case принимает входную строку и возвращает строку с применением странного регистра, как указано в техническом задании. Она разделяет входную строку на отдельные слова, затем для каждого слова применяет логику изменения регистра на основе индекса символа. Результат объединяется обратно в строку с использованием пробелов между словами.
"""

# tags: Strings, Algorithms
# kyu: 6

def to_weird_case(string):
    words = string.split()  # Разделяем строку на слова
    result = []  # Создаем список для сохранения результата

    for word in words:
        weird_word = ''  # Создаем переменную для сохранения слова в странном регистре
        for i in range(len(word)):
            if i % 2 == 0:  # Если индекс четный, то делаем символ в верхнем регистре
                weird_word += word[i].upper()
            else:
                weird_word += word[i].lower()  # Иначе делаем символ в нижнем регистре
        result.append(weird_word)  # Добавляем странное слово в результат
    return ' '.join(result)  # Возвращаем результат, объединяя слова через пробел