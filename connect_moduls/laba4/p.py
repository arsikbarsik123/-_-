def create_matrix_from_vectors():
    """
    1. Создать двухмерный массив (матрицу) из нескольких полученных векторов.
    """
    print("Введите векторы, разделяя элементы пробелами. Для завершения ввода оставьте строку пустой.")
    vectors = []
    while True:
        line = input("Введите вектор: ")
        if not line:
            break
        vectors.append(list(map(int, line.split())))
    return vectors