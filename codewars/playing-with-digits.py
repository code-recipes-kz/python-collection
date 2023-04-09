"""
Вы можете вызывать функцию dig_pow(n, p), передавая ей числа n и p в качестве аргументов, и она вернет результат в соответствии с условиями, описанными в вашем техническом задании. Примеры использования функции dig_pow() также указаны в вашем задании.
"""

# tags: Fundamentals, Mathematics
# kyu: 6

def dig_pow(n, p):
    # Преобразование числа n в строку и разделение на отдельные цифры
    digits = [int(d) for d in str(n)]

    # Рассчет суммы цифр, возведенных в степени p, с учетом позиции
    total = sum([d**(p+i) for i, d in enumerate(digits)])

    # Проверка, является ли результат делителем числа n
    if total % n == 0:
        return total // n
    else:
        return -1
