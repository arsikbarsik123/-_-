def calculate_determinant(matrix):
    """
    10. Найти детерминант матрицы, считанной с клавиатуры.
    """
    if len(matrix) != len(matrix[0]):
        print("Матрица должна быть квадратной для вычисления детерминанта.")
        return

    def determinant_recursive(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        det = 0
        for c in range(len(mat)):
            minor = [row[:c] + row[c+1:] for row in mat[1:]]
            det += ((-1) ** c) * mat[0][c] * determinant_recursive(minor)
        return det

    return determinant_recursive(matrix)