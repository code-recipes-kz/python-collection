"""
Данная функция "smash" принимает список слов в качестве аргумента "words" и объединяет их в одну строку, разделяя слова пробелами. Для этого используется метод "join", который применяется к строке "sentence".

Затем функция удаляет все пробельные символы с начала и конца строки при помощи метода "strip()" и возвращает полученную строку.

Таким образом, данная функция выполняет операцию конкатенации списка слов в одну строку с пробелами между словами и возвращает полученную строку без пробельных символов в начале и конце строки.
"""

def smash(words):
    sentence = " ".join(words)
    return sentence.strip()