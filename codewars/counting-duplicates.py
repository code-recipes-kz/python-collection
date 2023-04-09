"""
Функция count_duplicates() принимает в качестве аргумента строку и возвращает количество символов, которые встречаются более одного раза. Сначала мы приводим все символы строки к нижнему регистру, чтобы не учитывать регистр при сравнении символов. Затем мы считаем количество повторений каждого символа, используя словарь char_count. Наконец, мы проходимся по значениям словаря char_count и подсчитываем количество символов, которые встречаются более одного раза, в переменной duplicate_count.
"""

# tags: Strings, Fundamentals
# kyu: 6

def count_duplicates(input_string):
    # приводим все символы к нижнему регистру
    input_string = input_string.lower()
    # создаем пустой словарь для хранения количества повторений каждого символа
    char_count = {}
    # считаем количество повторений каждого символа
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # подсчитываем количество символов, которые встречаются более одного раза
    duplicate_count = 0
    for count in char_count.values():
        if count > 1:
            duplicate_count += 1
    return duplicate_count