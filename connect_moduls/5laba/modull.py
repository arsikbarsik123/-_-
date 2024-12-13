def shell_sort(matrix):
    """
    1. Выполнить сортировку матрицы методом Шелла.
    """
    mas = [x for row in matrix for x in row]
    n = len(mas)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = mas[i]
            j = i
            while j >= gap and mas[j - gap] > temp:
                mas[j] = mas[j - gap]
                j -= gap
            mas[j] = temp
        gap //= 2
    return [mas[i:i + len(matrix[0])] for i in range(0, len(mas), len(matrix[0]))]

def bubble_sort(matrix):
    """
    2. Выполнить сортировку матрицы методом пузырька.
    """
    mas = [x for row in matrix for x in row]
    n = len(mas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    return [mas[i:i + len(matrix[0])] for i in range(0, len(mas), len(matrix[0]))]

def insertion_sort(matrix):
    """
    3. Выполнить сортировку матрицы методом вставок.
    """
    mas = [x for row in matrix for x in row]
    for i in range(1, len(mas)):
        key = mas[i]
        j = i - 1
        while j >= 0 and key < mas[j]:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = key
    return [mas[i:i + len(matrix[0])] for i in range(0, len(mas), len(matrix[0]))]

def selection_sort(matrix):
    """
    4. Выполнить сортировку матрицы методом выбора.
    """
    mas = [x for row in matrix for x in row]
    for i in range(len(mas)):
        min_idx = i
        for j in range(i + 1, len(mas)):
            if mas[j] < mas[min_idx]:
                min_idx = j
        mas[i], mas[min_idx] = mas[min_idx], mas[i]
    return [mas[i:i + len(matrix[0])] for i in range(0, len(mas), len(matrix[0]))]

def heapify(arr, n, i):
    """
    Вспомогательная функция для сортировки методом кучи.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(matrix):
    """
    5. Выполнить сортировку матрицы методом кучи.
    """
    mas = [x for row in matrix for x in row]
    n = len(mas)
    for i in range(n // 2 - 1, -1, -1):
        heapify(mas, n, i)
    for i in range(n - 1, 0, -1):
        mas[i], mas[0] = mas[0], mas[i]
        heapify(mas, i, 0)
    return [mas[i:i + len(matrix[0])] for i in range(0, len(mas), len(matrix[0]))]