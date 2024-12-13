import random
from math import gcd
from functools import reduce 

def num1(vector):
    """
    1. Вывести вектор в обратной последовательности.
    """
    print("Обратный вектор: ", vector[::-1])

def num2(vector):
    """
    2. Отсортировать вектор по возрастанию или убыванию в зависимости от ключа.
    """
    order = input("Введите '1' для сортировки по возрастанию или '-1' для сортировки по убыванию: ")
    if order == "1":
        print("Вектор отсортирован по возрастанию: ", sorted(vector))
    elif order == "-1":
        print("Вектор отсортирован по убыванию: ", sorted(vector, reverse=True))
    else:
        print("Неверный ключ сортировки.")

def num3(vector):
    """
    3. Найти минимальное или максимальное значение в векторе в зависимости от ключа.
    """
    key = input("Введите 'min' для поиска минимального значения или 'max' для поиска максимального значения: ")
    if key == "min":
        print("Минимальное значение в векторе:", min(vector))
    elif key == "max":
        print("Максимальное значение в векторе:", max(vector))
    else:
        print("Неверный ключ.")

def num4(vector):
    """
    4. Найти НОД всех элементов в векторе.
    """
    if len(vector) < 2:
        print("Вектор должен содержать хотя бы два элемента для вычисления НОД.")
    else:
        result = reduce(gcd, vector)
        print("НОД элементов вектора:", result)

def num5():
    """
    5. Считать два вектора произвольной длины, сравнить их сумму и вывести вектор с наименьшей суммой.
    """
    vector1 = list(map(int, input("Введите элементы первого вектора через пробел: ").split()))
    vector2 = list(map(int, input("Введите элементы второго вектора через пробел: ").split()))

    sum1 = sum(vector1)
    sum2 = sum(vector2)

    if sum1 < sum2:
        print("Первый вектор имеет меньшую сумму: ", vector1)
    elif sum2 < sum1:
        print("Второй вектор имеет меньшую сумму: ", vector2)
    else:
        print("Оба вектора имеют одинаковую сумму: ", vector1, "и", vector2)

def main():
    """
    Основная функция для выбора задания.
    """
    while True:
        print("\nВыберите действие:")
        print("1 - Вывести вектор в обратной последовательности")
        print("2 - Отсортировать вектор по возрастанию/убыванию")
        print("3 - Найти минимальное/максимальное значение в векторе")
        print("4 - Найти НОД в векторе")
        print("5 - Считать два вектора и сравнить их сумму")
        print("0 - Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            vector = list(map(int, input("Введите элементы вектора через пробел: ").split()))
            num1(vector)
        elif choice == "2":
            vector = list(map(int, input("Введите элементы вектора через пробел: ").split()))
            num2(vector)
        elif choice == "3":
            vector = list(map(int, input("Введите элементы вектора через пробел: ").split()))
            num3(vector)
        elif choice == "4":
            vector = list(map(int, input("Введите элементы вектора через пробел: ").split()))
            num4(vector)
        elif choice == "5":
            num5()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

main()
