import moduls
import random
import numpy as np
def main():
    """
    Основная функция для выбора задания.
    """
    while True:
        print("\nВыберите действие:")
        print("1 - Квадрат")
        print("2 - Треугольник в круге")
        print("3 - Круг на треугольнике")
        print("4 - Гистограмма")
        print("5 - Матрица с выделением мин/макс")
        print("6 - Раскраска строк матрицы")
        print("7 - Раскраска столбцов матрицы")
        print("8 - Градиентная матрица")
        print("0 - Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            moduls.draw_square()

        elif choice == "2":
            moduls.draw_triangle_in_circle()

        elif choice == "3":
            moduls.overlay_circle_on_triangle()

        elif choice == "4":
            moduls.draw_histogram()

        elif choice == "5":
            moduls.highlight_min_max()

        elif choice == "6":
            moduls.color_rows_by_index()

        elif choice == "7":
            moduls.color_columns_by_index()

        elif choice == "8":
            moduls.gradient_matrix()

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

with open("matrix.txt", "w") as file:
    for _ in range(5):
        row = " ".join(map(str, [random.randint(1, 20) for _ in range(5)]))
        file.write(row + "\n")
with open("matrix.txt", "r") as file:
    matrix = [list(map(int, line.split())) for line in file]
    np.array(matrix)
main()