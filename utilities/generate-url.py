import re

def transform_string(input_string):
    # Удаляем все знаки препинания
    cleaned_string = re.sub(r'[^\w\s]','',input_string)
    # Приводим все символы к нижнему регистру
    lowercase_string = cleaned_string.lower()
    # Словарь для замены кириллических символов на латинские
    cyrillic_to_latin = {'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'yo', 'ж':'zh', 'з':'z', 'и':'i', 'й':'j', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'h', 'ц':'c', 'ч':'ch', 'ш':'sh', 'щ':'shch', 'ъ':'', 'ы':'y', 'ь':'', 'э':'e', 'ю':'yu', 'я':'ya'}
    # Заменяем кириллические символы на латинские
    transliterated_string = ''.join([cyrillic_to_latin.get(c, c) for c in lowercase_string])
    # Заменяем пробелы на "-"
    result_string = re.sub(r'\s+', '-', transliterated_string)
    return result_string

text = transform_string('метод Гаусса для решения СЛАУ')

print(text)