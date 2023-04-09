"""
Эта программа принимает массив integers и возвращает "выброс" N. Программа работает следующим образом:

Создаем два пустых списка: even_numbers для четных чисел и odd_numbers для нечетных чисел.
Проходимся по каждому элементу массива integers.
Если число четное, добавляем его в список even_numbers. Если число нечетное, добавляем его в список odd_numbers.
Проверяем, имеет ли список even_numbers длину 1. Если да, то это означает, что выброс является четным числом, поэтому мы возвращаем это число. В противном случае выброс является нечетным числом, поэтому мы возвращаем первый элемент списка odd_numbers.
"""

# tags: Algorithms
# kyu: 6

def find_outlier(integers):
    even_numbers = []
    odd_numbers = []

    for number in integers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    if len(even_numbers) == 1:
        return even_numbers[0]
    else:
        return odd_numbers[0]
