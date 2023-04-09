"""

"""

# tags: Mathematics, Algorithms
# kyu: 6

def is_prime(n):
    if n <= 1:  # Числа <= 1 не являются простыми
        return False
    elif n <= 3:  # 2 и 3 - простые числа
        return True
    elif n % 2 == 0 or n % 3 == 0:  # Числа, кратные 2 или 3, не являются простыми
        return False
    else:
        i = 5
        while i * i <= n:  # Проверяем делители только до квадратного корня из n
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True