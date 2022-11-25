#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []
max_pos_1 = 0
max_elem_1 = float('-inf')

max_pos_2 = 0
max_elem_2 = float('-inf')

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.read()
            # выводим считанные данные на экран
            self.plainTextEdit.appendPlainText("Полученные данные: \n" + data + "\n")

            global list_of_numbers
            list_of_numbers = []

            # \b -- ищет границы слов
            # [0-9] -- описывает что ищем
            # + -- говорит, что искать нужно минимум от 1 символа
            for num in re.findall(r'\b[0-9]+\b', data):
                list_of_numbers.append(num)

    # Поменять местами максимальные элементы первой и второй строк таблицы,
    # если сумма элементов больше 100, а третью строку заменить единицами
    def process_data(self):
        global max_pos_1
        global max_elem_1

        global max_pos_2
        global max_elem_2

        if validation_of_data():
            max_num_1row = find_max(1)
            max_num_2row = find_max(2)

            # sum_of_first_row = find_sum_of_first_row()
            sum_of_rows = max_num_1row + max_num_2row

            # -*- выполнение задания -*-
            if sum_of_rows >= 100:
                complete_task() # Финальная обработка

                self.plainTextEdit.appendPlainText("Данные обработаны! " + '\n')

                # выводим список на экран
                for k, i in enumerate (list_of_numbers):
                    self.plainTextEdit.insertPlainText(str(i) + " ")
                    # чтобы текст был в виде таблицы, делаем отступ после
                    # 6 элемента
                    if ((k + 1) % 5) == 0:
                        self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText("Макс элемент первой строки + макс элем. второй строки меньше 100! \n")
                print(max_elem_1, max_elem_2, max_pos_1, max_pos_2)
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл
        :return:
        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for k, i in enumerate(list_of_numbers):
                file.write(str(i) + " ")
                if ((k+1) % 5) == 0:
                    file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def find_max(rowCount):
    """
    находим максимальное число в списке
    :return: максимальное число
    """

    global max_pos_1
    global max_elem_1

    global max_pos_2
    global max_elem_2

    start = 0
    end = 5
    if rowCount == 1:
        start = 0
        end = 5
    elif rowCount == 2:
        start = 5
        end = 10

    max_num = float('-inf')
    # print(start, end)
    # for idx, elem list_of_numbers:
    for i in range(len(list_of_numbers)):
        x = int(list_of_numbers[i])
        if start <= i < end:
            print(i, x)
            # print(x)
            if rowCount == 1:
                if max_elem_1 < x:
                    max_elem_1 = x
                    max_pos_1 = i
            elif rowCount == 2:
                if max_elem_2 < x:
                    max_elem_2 = x
                    max_pos_2 = i


    print(max_elem_1, max_elem_2)

    if rowCount == 1:
        return max_elem_1
    elif rowCount == 2:
        return max_elem_2
    else:
        return float('-inf')

        # if max_num < int(i):
        #     max_num = int(i)


def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """
    if len(list_of_numbers) == 30:
        for i in list_of_numbers:
            try:
                float(i)
            except Exception:
                return False
        return True
    else:
        return False


def increasing_max_num_of_double(max_num):
    """
    увеличение максимального числа в два раза
    :param max_num: максимальное число
    :return: pass
    """
    for n, i in enumerate(list_of_numbers):
        if int(i) == max_num:
            list_of_numbers[n] = str(max_num * 2)
            break
    pass



def complete_task():
    """
    выполнение задания - поменять местами и заполнить третью строку единицами
    :param max_num: максимальное число
    :return: pass
    """

    global max_pos_1
    global max_elem_1

    global max_pos_2
    global max_elem_2
    list_of_numbers[max_pos_1] = max_elem_2
    list_of_numbers[max_pos_2] = max_elem_1

    for n, i in enumerate(list_of_numbers):
        if 10 <= n < 15:
            list_of_numbers[n] = 1
    pass


def find_sum_of_first_row():
    """
    находим сумму чисел из первой строки таблицы
    :return: сумму чисел из первой строки
    """
    sum = 0
    i = 0
    while i < 6:  # в строке должно быть ровно 6 чисел
        sum += int(list_of_numbers[i])
        i += 1

    return sum


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
