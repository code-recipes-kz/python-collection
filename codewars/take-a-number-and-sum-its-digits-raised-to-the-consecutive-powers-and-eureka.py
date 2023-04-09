"""
Функция eureka_numbers принимает на вход два целых числа a и b, которые определяют диапазон [a, b] (включительно), в котором нужно найти числа, удовлетворяющие свойству, описанному в задаче. Функция проходит по всем числам в диапазоне и проверяет, выполняется ли условие sum(int(d) ** (i+1) for i, d in enumerate(str(num))) == num. Если условие выполняется, то число добавляется в результирующий список. В конце функция возвращает отсортированный список найденных чисел.
"""

# tags: Fundamentals, Mathematics
# kyu: 6

def eureka_numbers(a, b):
    result = []
    for num in range(a, b+1):
        if sum(int(d) ** (i+1) for i, d in enumerate(str(num))) == num:
            result.append(num)
    return result