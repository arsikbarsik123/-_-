def num1():
    """
    1. Считать информацию с клавиатуры и вывести на экран.
    """
    text = input("Введите текст: ")
    print(f"Вы ввели: {text}")

def num2(filename):
    """
    2. Считать информацию с клавиатуры и записать в файл.
    """
    text = input("Введите текст: ")
    with open(filename, "w") as file:
        file.write(text)
    print(f"Текст записан в файл: {filename}")

def num3(filename):
    """
    3. Считать информацию из файла и вывести на экран.
    """
    with open(filename, "r") as file:
        content = file.read()
    print(f"Содержимое файла {filename}:")
    print(content)

def num4(filename):
    """
    4. Считать информацию с клавиатуры и записать в начало файла.
    """
    text = input("Введите текст: ")
    s = ""
    
    with open(filename, "r") as file:
        s = file.read()
    with open(filename, "w") as file:
        file.write(text + "\n" + s)
    print(f"Текст успешно добавлен в начало файла: {filename}")

def main():
    """
    Основная функция для выбора задания.
    """
    filename = "text_1_laba.txt"
    while True:
        print("\nВыберите действие:")
        print("1 - Считать информацию с клавиатуры и вывести на экран")
        print("2 - Считать информацию с клавиатуры и записать в файл")
        print("3 - Считать информацию из файла и вывести на экран")
        print("4 - Считать информацию с клавиатуры и записать в начало файла")
        print("0 - Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            num1()
        elif choice == "2":
            num2(filename)
        elif choice == "3":
            num3(filename)
        elif choice == "4":
            num4(filename)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
main()# запуск заданий