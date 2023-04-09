# tags: Strings, ASCII Art, Fundamentals
# kyu: 6

def tower_builder(n):
    tower = []
    width = n * 2 - 1 # Ширина основания пирамиды
    for i in range(n):
        stars = '*' * (i * 2 + 1) # Количество звездочек на текущем этаже
        spaces = ' ' * (width // 2 - i) # Количество пробелов перед и после звездочек на текущем этаже
        floor = spaces + stars + spaces # Звездочки с пробелами на текущем этаже
        tower.append(floor)
    return tower