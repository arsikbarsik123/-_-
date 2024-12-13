def multiply_matrices():
    """
    11. Выполнить произведение матрицы, считанной из файла, на матрицу, считанную с клавиатуры.
    """
    with open("matrix_file.txt", "r") as file:
        matrix1 = [list(map(int, line.split())) for line in file]

    print("Введите матрицу построчно. Для завершения ввода оставьте строку пустой.")
    matrix2 = []
    while True:
        line = input("Введите строку матрицы: ")
        if not line:
            break
        matrix2.append(list(map(int, line.split())))

    if len(matrix1[0]) != len(matrix2):
        print("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы.")

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result