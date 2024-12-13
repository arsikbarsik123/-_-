def replace_column_with_another(matrix, col_index, other_matrix, other_col_index):
    """
    8. Произвести замену указанного столбца матрицы, указанного из другой матрицы (для мальчиков).
    """
    for i in range(len(matrix)):
        matrix[i][col_index] = other_matrix[i][other_col_index]
    return matrix