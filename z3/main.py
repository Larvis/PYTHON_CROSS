#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m=8, max_value=21):
    array = []  # основной массив
    for i in range(0, n):
        sub_array = []  # подмассив с числами
        for j in range(m):
            # от минимального числа (-10) до максимального -1 (max_value - 1 = 20) с шагом (1)
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number)  # добавление случайного числа в подмассив
        array.append(sub_array)  # добавление подмассива в массив
    return array  # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array:  # перебор по подмассивам(строкам)
        for j in i:  # перебор по элементам строк
            print("%5.1f\t" % j, end='')
        print()


# функция для нахождения элементов условия (в этом случае максимум и минимум,
# может быть количество нулей, количество отрицательных числе и т.д.)
def counting(array):
    print()
    # как начальное значение для макс/мин берется первый элемент массива
    max_value = array[0][0]
    min_value = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            e = array[i][j]
            if e > max_value:
                max_value = e
            if e < min_value:
                min_value = e
    print("Максимум: %d, минимум: %d" % (max_value, min_value))
    print()
    return max_value, min_value


def main():
    rowCount = 4
    colCount = 5
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(rowCount, colCount)  # можно изменить размер
    print("Условие задания:\n"
          "Если сумма наибольшего и наименьшего чисел больше нуля,\n"
          "то увеличить максимальный элемент в два раза,\n"
          "а наименьший уменьшить в два раза")
    # вызов функции вывода массива
    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    max_value, min_value = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            print_array(array)
            max_value, min_value = counting(array)
        elif key == '2':
            # проверка выполнения условия
            if (max_value + min_value) <= 0:
                print("Сумма наибольшего и наименьшего чисел (%d) не больше нуля " % (max_value + min_value))
                print("Задание не будет выполнено.")
            else:
                # выполнения результата совпадения условия,
                # в данном случае макс * 2, а мин / 2
                print("Cумма наибольшего и наименьшего чисел больше нуля (%d)" % (max_value + min_value))
                for i in range(len(array)):  # перебор каждую строку
                    while True:  # цикл нужен, так как макс/мин не одни в массиве
                        try:
                            index_max = array[i].index(max_value)  # положение макс в строке
                            array[i][index_max] *= 2
                        except ValueError:
                            break
                for i in range(len(array)):
                    while True:
                        try:
                            index_min = array[i].index(min_value)  # положение мин в строке
                            array[i][index_min] /= 2
                        except ValueError:
                            break

                print("Макс. элемент таблицы (все, если их больше одного) был(и) увеличен(ы) в два раза.")
                print("Мин. элемент таблицы (все, если их больше одного) был(и) уменьшен(ы) в два раза.")
                print_array(array)
                break  # выход из цикла
        elif key == '3':
            exit(0)  # выход из программы


if __name__ == '__main__':
    main()