def transpose_matrix(matrix):
    """
    4. Транспонировать матрицу.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]