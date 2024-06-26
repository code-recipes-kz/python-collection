"""
Функция bouncing_ball() принимает на вход три параметра: высоту окна h, коэффициент отскока bounce, и высоту окна window. Она возвращает количество отскоков мяча, видимых матерью, удовлетворяющих условиям из задания, или -1, если условия не выполняются. Функция использует цикл while, чтобы моделировать отскоки мяча и считать количество видимых отскоков.

Функция bouncing_ball() начинает с проверки условий из задания: h должно быть больше 0, bounce должно быть больше 0 и меньше 1, и window должно быть меньше h. Если хоть одно из этих условий не выполняется, функция возвращает -1 как результат и прекращает выполнение.

Если все условия выполняются, функция инициализирует переменную visible_bounces в ноль, которая будет использоваться для подсчета количества видимых отскоков мяча.

Затем функция входит в цикл while, который будет выполняться, пока высота мяча h остается выше высоты окна window.

Внутри цикла, функция увеличивает значение visible_bounces на 1, чтобы учесть текущий отскок мяча, и затем умножает h на bounce, чтобы моделировать отскок мяча и обновить его высоту.

После этого функция проверяет, если высота мяча h после отскока превышает высоту окна window. Если это так, то функция увеличивает значение visible_bounces на 1 еще раз, чтобы учесть еще один отскок мяча, который будет виден матерью.

После каждого отскока, функция повторяет шаги 4 и 5, пока высота мяча h остается выше высоты окна window.

Когда высота мяча h становится меньше или равна высоте окна window, цикл while завершается, и функция возвращает значение visible_bounces как результат, представляющий количество видимых отскоков мяча, удовлетворяющих условиям из задания.
"""

# tags: Puzzles, Algorithms, Mathematics
# kyu: 6

def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1  # Проверка условий из задания

    visible_bounces = 0  # Количество видимых отскоков
    while h > window:
        visible_bounces += 1
        h *= bounce  # Высота после отскока
        if h > window:
            visible_bounces += 1  # Добавляем еще один отскок, если высота после отскока превышает высоту окна

    return visible_bounces