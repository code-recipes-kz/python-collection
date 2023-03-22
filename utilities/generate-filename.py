import re

def transform_string(s):
    s = s.lower()  # Преобразуем строку к lower case
    s = s.replace(" ", "-")  # Заменяем пробелы на "-"
    s = s.replace("_", "-")  # Заменяем знаки "_" на "-"
    s = re.sub(r'[^\w-]', '', s)  # Удаляем все знаки препинания, кроме "-", "_" и буквенно-цифровых символов
    s += ".py"  # Добавляем ".py" в конец строки
    return s

s = transform_string('Stop gninnipS My sdroW!')
print(s)