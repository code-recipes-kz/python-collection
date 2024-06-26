"""
Программа принимает на вход номер кредитной карты в виде целого числа card_number.
Номер карты преобразуется в список цифр digits с помощью функции str(card_number) для перевода числа в строку и int(d) для преобразования каждого символа строки в целое число. Это делается для того, чтобы удобнее работать с отдельными цифрами номера карты.
Далее происходит удвоение каждой второй цифры номера карты, начиная со второй цифры справа. Это делается с помощью цикла for и индексации списка digits в обратном порядке, используя range(len(digits) - 2, -1, -2). Внутри цикла каждая цифра, находящаяся на нечетной позиции, умножается на 2.
После удвоения проверяется, превышает ли результат удвоения 9. Если да, то из результата вычитается 9, что эквивалентно суммированию цифр числа после удвоения. Это делается с помощью условного оператора if и операции digits[i] -= 9.
Затем все цифры списка digits суммируются с помощью функции sum(digits) и результат сохраняется в переменной total.
Далее проверяется, делится ли сумма total на 10 без остатка, с помощью условного оператора if и операции % (оператор деления по модулю). Если да, то возвращается True, иначе - False.
"""

# tags: Algorithms
# kyu: 6

def validate_credit_card_number(card_number):
    # Преобразование номера карты в список цифр
    digits = [int(d) for d in str(card_number)]
    # Удвоение каждой второй цифры, начиная со второй цифры справа
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        # Если результат удвоения больше 9, заменяем его на сумму цифр
        if digits[i] > 9:
            digits[i] -= 9
    # Суммируем все цифры
    total = sum(digits)
    # Проверяем, делится ли сумма на 10 без остатка
    if total % 10 == 0:
        return True
    else:
        return False