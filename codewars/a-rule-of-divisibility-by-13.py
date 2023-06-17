"""
Функция thirt принимает целое число n и выполняет алгоритм, описанный в задаче, для нахождения стационарного числа. Давайте разберем каждую часть кода:

    sequence = [1, 10, 9, 12, 3, 4]: Здесь мы создаем список sequence, который содержит повторяющуюся последовательность остатков от деления на 13, как указано в задаче.

    digits = list(map(int, str(n))): Эта строка кода преобразует число n в список его цифр. Мы используем функцию str(n), чтобы преобразовать число в строку, а затем map(int, ...) для преобразования каждого символа строки в целое число. Наконец, list(...) создает список из этих цифр.

    length = len(digits): Здесь мы вычисляем длину списка digits, чтобы знать количество цифр в исходном числе n.

    total = 0: Мы инициализируем переменную total нулем, которая будет использоваться для хранения суммы произведений цифр и элементов последовательности.

    for i in range(length):: Этот цикл проходит через цифры исходного числа n справа налево.

    total += digits[length - 1 - i] * sequence[i % 6]: В этой строке мы умножаем текущую цифру числа на соответствующий элемент последовательности, используя операцию % для получения остатка от деления i на 6 (длина последовательности). Результат умножения добавляется к переменной total.

    if total == n: return total else: return thirt(total): После завершения цикла мы проверяем, равен ли total исходному числу n. Если это так, то total является стационарным числом, и мы возвращаем его. В противном случае, мы вызываем функцию thirt рекурсивно с total в качестве нового аргумента, чтобы продолжить процесс нахождения стационарного числа.

Таким образом, функция thirt выполняет последовательность операций, описанных в задаче, на каждом шаге обновляя total и продолжая до тех пор, пока не будет найдено стационарное число.
"""

# tags: Fundamentals, Algorithms, Mathematics
# kyu: 6

def thirt(n):
    sequence = [1, 10, 9, 12, 3, 4]
    digits = list(map(int, str(n)))
    length = len(digits)
    total = 0

    for i in range(length):
        total += digits[length - 1 - i] * sequence[i % 6]

    if total == n:
        return total
    else:
        return thirt(total)
