def remove_main_diagonal(matrix):
    """
    5. Вычеркнуть главную диагональ матрицы (для мальчиков).
    """
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return matrix