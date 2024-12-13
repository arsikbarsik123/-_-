import random
import matplotlib.pyplot as plt
import numpy as np

def create_example_matrix_file():
    """
    Создать файл с примерной матрицей для работы.
    """
    with open("matrix.txt", "w") as file:
        for _ in range(5):
            row = " ".join(map(str, [random.randint(1, 20) for _ in range(5)]))
            file.write(row + "\n")

def read_matrix_from_file():
    """
    Считать матрицу из файла.
    """
    with open("matrix.txt", "r") as file:
        matrix = [list(map(int, line.split())) for line in file]
    return np.array(matrix)

def draw_square():
    """
    1. Создать графический объект - квадрат (для мальчиков).
    """
    plt.figure()
    square = plt.Rectangle((0.1, 0.1), 0.8, 0.8, fill=None, edgecolor='blue', linewidth=2)
    plt.gca().add_patch(square)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title("Квадрат")
    plt.show()

def draw_triangle_in_circle():
    """
    2. Вписать треугольник в круг с радиусом, считанным с клавиатуры.
    """
    radius = float(input("Введите радиус круга: "))
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = radius * np.cos(theta)
    y_circle = radius * np.sin(theta)

    triangle = np.array([
        [0, radius],
        [-radius * np.sqrt(3) / 2, -radius / 2],
        [radius * np.sqrt(3) / 2, -radius / 2],
        [0, radius]
    ])

    plt.figure()
    plt.plot(x_circle, y_circle, label="Круг")
    plt.plot(triangle[:, 0], triangle[:, 1], label="Треугольник", color="red")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title("Треугольник в круге")
    plt.show()

def overlay_circle_on_triangle():
    """
    3. Наложить на треугольник круг, с радиусом равным четверти радиуса круга,
       в который можно было бы вписать треугольник. Случайный выбор вершины в качестве центра.
    """
    radius = float(input("Введите радиус круга: "))
    vertices = np.array([
        [0, radius],
        [-radius * np.sqrt(3) / 2, -radius / 2],
        [radius * np.sqrt(3) / 2, -radius / 2]
    ])
    center = vertices[random.randint(0, 2)]
    overlay_radius = radius / 4

    plt.figure()
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = radius * np.cos(theta)
    y_circle = radius * np.sin(theta)
    plt.plot(x_circle, y_circle, label="Круг")
    plt.plot(vertices[:, 0], vertices[:, 1], label="Треугольник", color="red")
    overlay_x = center[0] + overlay_radius * np.cos(theta)
    overlay_y = center[1] + overlay_radius * np.sin(theta)
    plt.plot(overlay_x, overlay_y, label="Наложенный круг", color="green")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title("Круг на треугольнике")
    plt.show()

def draw_histogram():
    """
    4. Построить гистограмму, соответствующую вектору, считанному с клавиатуры.
    """
    vector = list(map(int, input("Введите элементы вектора через пробел: ").split()))
    plt.figure()
    plt.bar(range(len(vector)), vector, color="blue", alpha=0.7)
    plt.title("Гистограмма")
    plt.xlabel("Индексы")
    plt.ylabel("Значения")
    plt.show()

def highlight_min_max():
    """
    5. Вывести матрицу, пометив цветом только максимальное и минимальное значение.
    """
    matrix = read_matrix_from_file()
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    plt.figure()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            color = "red" if matrix[i, j] == min_val else ("green" if matrix[i, j] == max_val else "white")
            plt.text(j, -i, str(matrix[i, j]), color=color, ha="center", va="center")
    plt.xlim(-0.5, len(matrix[0]) - 0.5)
    plt.ylim(-len(matrix) + 0.5, 0.5)
    plt.gca().axis("off")
    plt.title("Матрица с выделением мин/макс")
    plt.show()

def color_rows_by_index():
    """
    6. Вывести матрицу, раскрасив строки в соответствии с индексом плюс значение, считанное с клавиатуры.
    """
    matrix = read_matrix_from_file()
    value = int(input("Введите значение для раскраски строк: "))
    plt.figure()
    for i, row in enumerate(matrix):
        color = plt.cm.viridis((i + value) / (len(matrix) + value))
        plt.text(0, -i, " ".join(map(str, row)), color=color, ha="left", va="center")
    plt.gca().axis("off")
    plt.title("Матрица с раскраской строк")
    plt.show()

def color_columns_by_index():
    """
    7. Вывести матрицу, раскрасив столбцы в соответствии с индексом с конца вектора цветов минус значение первого элемента матрицы.
    """
    matrix = read_matrix_from_file()
    color_offset = matrix[0, 0]
    plt.figure()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            color = plt.cm.plasma((len(matrix[0]) - j - color_offset) / len(matrix[0]))
            plt.text(j, -i, str(matrix[i, j]), color=color, ha="center", va="center")
    plt.gca().axis("off")
    plt.title("Матрица с раскраской столбцов")
    plt.show()

def gradient_matrix():
    """
    8. Вывести отсортированную матрицу, раскрасив градиентом. Цвет строки определяется элементом главной диагонали.
    """
    matrix = read_matrix_from_file()
    sorted_matrix = np.sort(matrix, axis=1)
    plt.figure()
    for i, row in enumerate(sorted_matrix):
        color = plt.cm.cool(matrix[i, i] / np.max(matrix))
        for j, val in enumerate(row):
            plt.text(j, -i, str(val), color=color, ha="center", va="center")
    plt.gca().axis("off")
    plt.title("Матрица с градиентом по диагонали")
    plt.show()