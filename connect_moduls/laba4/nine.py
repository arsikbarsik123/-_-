def replace_with_zeros(matrix, value):
    """
    9. Найти в матрице элемент, кратный значению, считанному с клавиатуры, 
       и заменить строку или столбец на нули в зависимости от чётности следующего элемента.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % value == 0:
                if j + 1 < len(matrix[i]) and matrix[i][j + 1] % 2 == 0:
                    matrix[i] = [0] * len(matrix[i])
                else:
                    for row in matrix:
                        row[j] = 0
                return matrix
    return matrix