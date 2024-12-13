# Подключаем нужные модули
import p

import third
import four
import five


import eight
import nine
import ten
import eleven
import twelve

def main():
    """
    Основная функция для выбора задания.
    """
    while True:
        print("\nВыберите действие:")
        print("1 - Создать двухмерный массив из векторов")
        print("3 - Удалить столбец из матрицы")
        print("4 - Транспонировать матрицу")
        print("5 - Удалить главную диагональ")
        print("8 - Заменить столбец матрицы на столбец из другой матрицы")
        print("9 - Заменить строку или столбец матрицы на нули")
        print("10 - Найти детерминант матрицы")
        print("11 - Умножить две матрицы")
        print("12 - Поменять строки матрицы местами")
        print("0 - Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            global matrix
            matrix = p.create_matrix_from_vectors()
            print("Матрица создана:")
            for row in matrix:
                print(row)

        elif choice == "3":
            col_index = int(input("Введите индекс столбца для удаления: "))
            matrix = third.remove_column(matrix, col_index)
            print("Матрица после удаления столбца:")
            for row in matrix:
                print(row)

        elif choice == "4":
            matrix = four.transpose_matrix(matrix)
            print("Транспонированная матрица:")
            for row in matrix:
                print(row)

        elif choice == "5":
            matrix = five.remove_main_diagonal(matrix)
            print("Матрица после удаления главной диагонали:")
            for row in matrix:
                print(row)

        elif choice == "8":
            col_index = int(input("Введите индекс столбца для замены: "))
            other_matrix = [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ]
            other_col_index = int(input("Введите индекс столбца из другой матрицы: "))
            matrix = eight.replace_column_with_another(matrix, col_index, other_matrix, other_col_index)
            print("Матрица после замены столбца:")
            for row in matrix:
                print(row)

        elif choice == "9":
            value = int(input("Введите значение для проверки кратности: "))
            matrix = nine.replace_with_zeros(matrix, value)
            print("Матрица после замены на нули:")
            for row in matrix:
                print(row)

        elif choice == "10":
            det = ten.calculate_determinant(matrix)
            print(f"Детерминант матрицы: {det}")

        elif choice == "11":
            result = eleven.multiply_matrices()
            print("Результат умножения матриц:")
            for row in result:
                print(row)

        elif choice == "12":
            matrix = twelve.swap_rows_in_file_matrix()
            print("Матрица после замены строк:")
            for row in matrix:
                print(row)


        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


with open("column_index.txt", "w") as file:
    file.write("5")
    # Файл для задания 11 и 12 (матрицы)
with open("matrix_file.txt", "w") as file:
    file.write("1 2 3\n4 5 6\n7 8 9\n")
with open("matrix_swap.txt", "w") as file:
    file.write("10 20 30\n40 50 60\n70 80 90\n")
main()