"""

"""

# tags: Fundamentals, Geometry, Puzzles
# kyu: 6

def sq_in_rect(length, width):
    if length == width:
        return None # Если длина и ширина равны, возвращаем None, так как из такого прямоугольника невозможно вырезать квадраты
    elif length < 1 or width < 1:
        return None # Если длина или ширина меньше 1, возвращаем None, так как это недопустимый прямоугольник
    else:
        squares = [] # Создаем пустой список для хранения размеров квадратов

		while length != width: # Продолжаем вырезать квадраты до тех пор, пока длина и ширина не станут равными
            if length > width:
                squares.append(width) # Добавляем меньшую сторону в список размеров квадратов
                length -= width # Уменьшаем длину на ширину
            else:
                squares.append(length) # Добавляем меньшую сторону в список размеров квадратов
                width -= length # Уменьшаем ширину на длину
        squares.append(length) # Добавляем последний квадрат, который будет иметь стороны, равные оставшейся длине/ширине

		return squares