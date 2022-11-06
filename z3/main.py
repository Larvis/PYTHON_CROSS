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
            number = -1#random.randrange(-10, max_value, 1)
            sub_array.append(number)  # добавление случайного числа в подмассив
        array.append(sub_array)  # добавление подмассива в массив
    array[0][0] = 1
    array[-1][-1] = 2
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
    next_aft_max = min_value = array[0][0]

    for i in range(len(array)):
        for j in range(len(array[i])):
            e = array[i][j]

            if e > max_value:
                max_value = e
                ## Если конец строки - то след. строка
                if (len(array[i]) - 1) == j: # если последний элемент
                    if (len(array) - 1) == i:  # если последний элемент в последней строке
                        next_aft_max = array[0][0]
                    else:  ## Если элемент последний, но строка не последняя
                        next_aft_max = array[i + 1][0]
                else: ## Если не последний элемент, то + 1
                    next_aft_max = array[i][j + 1]
                # print(i,j)
                # print(next_aft_max)

            ## Если конец столбца и строки - 0 0
            if e < min_value:
                min_value = e
    print("Максимум: %d, минимум: %d, след. после макс:%d" % (max_value, min_value, next_aft_max))
    print()
    return max_value, min_value, next_aft_max


def main():
    rowCount = 4
    colCount = 5
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(rowCount, colCount)  # можно изменить размер
    print("Условие задания:\n"
          "Если сумма наибольшего и наименьшего чисел больше нуля,\n"
          "то увеличить максимальный элемент в два раза,\n"
          "а наименьший уменьшить в два раза")
    print('========================================================')
    # вызов функции вывода массива
    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    max_value, min_value, next_aft_max = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        print('========================================================')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            print_array(array)
            max_value, min_value, next_aft_max = counting(array)
        elif key == '2':
            # проверка выполнения условия
            if next_aft_max == 0:
                print("Следующее число после (%d) равно нулю (%d)" %(max_value, next_aft_max))
                print("Условия не выполнены.")
                print('========================================================')
            else:
                # выполнения результата совпадения условия,
                # в данном случае макс * 2, а мин / 2
                print('========================================================')
                print("Следующее число после (%d) не равно нулю (%d)" % (max_value, next_aft_max))
                print("Условие выполнено, все положительные значения будут увеличены в 2 раза.")
                print('========================================================')
                for i in range(len(array)):  # перебор каждую строку
                    for j in range(len(array[i])):  # перебор каждую строку
                        if array[i][j] > 0:
                            array[i][j] *= 2

                print("Все положительные элементы таблицы был увеличены в два раза.")
                print_array(array)
                break  # выход из цикла
        elif key == '3':
            exit(0)  # выход из программы


if __name__ == '__main__':
    main()