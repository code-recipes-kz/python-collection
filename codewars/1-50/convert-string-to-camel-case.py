"""
Данная функция преобразует текстовую строку в формат "Camel Case". Это означает, что каждое слово в строке начинается с заглавной буквы, за исключением первого слова, которое начинается с маленькой буквы. В функции используется знак подчеркивания («_») или дефис («-») в качестве разделителя между словами.

Алгоритм функции следующий:

Заменяем дефисы на знаки подчеркивания с помощью метода replace().
Разбиваем строку на список слов, используя знак подчеркивания в качестве разделителя, с помощью метода split().
Создаем новый список слов, начиная с первого слова. Первое слово оставляем без изменений, а для каждого последующего слова вызываем метод capitalize(), чтобы первая буква стала заглавной.
Объединяем слова из списка в строку, используя метод join().
Возвращаем полученную строку в формате Camel Case.
Например, если мы передадим строку "hello_world-how_are_you", функция вернет строку "helloWorldHowAreYou".
"""

# tags: Regular Expressions, Algorithms, Strings
# kyu: 6

def to_camel_case(text):
    words = text.replace('-', '_').split('_')
    # Первое слово должно начинаться с маленькой буквы, если исходное слово начиналось с маленькой буквы,
    # и с большой буквы, если исходное слово начиналось с большой буквы.
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    return ''.join(camel_case_words)