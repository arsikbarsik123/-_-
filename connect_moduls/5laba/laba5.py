import modull

def main():
    while True:
        print("\nВыберите действие:")
        print("1 - Сортировка матрицы методом Шелла")
        print("2 - Сортировка матрицы методом пузырька")
        print("3 - Сортировка матрицы методом вставок")
        print("4 - Сортировка матрицы методом выбора")
        print("5 - Сортировка матрицы методом кучи")
        print("0 - Выход")

        choice = input("Введите номер действия: ")

        if choice in ["1", "2", "3", "4", "5"]:
            with open("matrix_file.txt", "r") as file:
                matrix = [list(map(int, line.split())) for line in file]

            if choice == "1":
                sorted_matrix = modull.shell_sort(matrix)
            elif choice == "2":
                sorted_matrix = modull.bubble_sort(matrix)
            elif choice == "3":
                sorted_matrix = modull.insertion_sort(matrix)
            elif choice == "4":
                sorted_matrix = modull.selection_sort(matrix)
            elif choice == "5":
                sorted_matrix = modull.heap_sort(matrix)

            print("Отсортированная матрица:")
            for row in sorted_matrix:
                print(row)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


main()