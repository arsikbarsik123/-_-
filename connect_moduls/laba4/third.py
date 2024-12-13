def remove_column(matrix, col_index):
    """
    3. Вычеркнуть из матрицы столбец, индекс которого получен из файла (для мальчиков).
    """
    return [row[:col_index] + row[col_index + 1:] for row in matrix]