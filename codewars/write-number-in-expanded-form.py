# tags: Strings, Mathematics, Algorithms, Fundamentals
# kyu: 6

def expanded_form(number):
    # Преобразуем число в строку, чтобы получить количество цифр
    num_str = str(number)
    # Инициализируем пустую строку для расширенной формы числа
    expanded_form_str = ''
    # Переменная-флаг для определения, нужно ли добавлять "+" перед следующим слагаемым
    add_plus = False

    # Проходим по каждой цифре числа, начиная с самой левой
    for i in range(len(num_str)):
        # Если текущая цифра не равна 0
        if num_str[i] != '0':
            # Если нужно добавить "+" перед следующим слагаемым, добавляем его
            if add_plus:
                expanded_form_str += ' + '
            # Добавляем текущую цифру, умноженную на 10, в степени, соответствующую ее позиции
            expanded_form_str += num_str[i] + '0' * (len(num_str) - 1 - i)
            # Устанавливаем флаг "add_plus" в значение True, чтобы добавить "+" перед следующим слагаемым
            add_plus = True

    return expanded_form_str