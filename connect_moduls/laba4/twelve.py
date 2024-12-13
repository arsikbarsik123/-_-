def swap_rows_in_file_matrix():
    """
    12. В матрице, считанной из файла, поменять местами строку с номером, считанным с клавиатуры.
    """
    with open("matrix_swap.txt", "r") as file:
        matrix = [list(map(int, line.split())) for line in file]

    row1 = int(input("Введите номер первой строки: "))
    row2 = int(input("Введите номер второй строки: "))

    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix