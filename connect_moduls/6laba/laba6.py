import moduls
def main():
    while True:
        print("\nВыберите действие:")
        print("1 - Форматированный текст")
        print("2 - Псевдографика таблицы")
        print("3 - Удаление символов из строки в файле")
        print("5 - Поиск строки в файле")
        print("7 - Бегущая строка в обратном направлении")
        print("0 - Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            text = input("Введите текст: ")
            alignment = input("Выберите выравнивание (left, center, right): ")
            try:
                print(moduls.format_text(text, alignment))
            except ValueError as e:
                print(e)

        elif choice == "2":
            rows = int(input("Введите количество строк: "))
            cols = int(input("Введите количество столбцов: "))
            print(moduls.create_table(rows, cols))

        elif choice == "3":
            file_name = "example.txt"
            chars = input("Введите символы для удаления: ")
            result = moduls.remove_characters_from_file(file_name, chars)
            print("Результат:")
            print(result)

        elif choice == "5":
            file_name = "example.txt"
            query = input("Введите строку для поиска: ")
            result = moduls.search_string_in_file(file_name, query)
            print(f"Результат: {result}")

        elif choice == "7":
            file_name = "example.txt"
            print("Бегущая строка:")
            moduls.reverse_scrolling_text(file_name)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

main()