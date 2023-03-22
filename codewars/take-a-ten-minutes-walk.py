def is_valid_walk(walk):
    # Проверяем, что длина маршрута равна 10
    if len(walk) != 10:
        return False

    # Инициализируем начальную точку
    x, y = 0, 0

    # Проходимся по всем направлениям и изменяем координаты соответственно
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1

    # Проверяем, что мы вернулись в начальную точку
    return x == 0 and y == 0