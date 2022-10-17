#!/usr/bin/env python3
# coding=utf-8

import sys, os

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Создание простейшей визуальной '
                            'программы на Python')



        # Задание иконки окна
        # app = QApplication(sys.argv)
        # path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'favicon.png')
        # app.setWindowIcon(QtGui.QIcon(path))

        # self.setWindowIcon(QtGui.QIcon(QPixmap('favicon.png')))

        # Задание картинки с заданием с масштабированием в компоненте
        self.label_img.setPixmap(QPixmap('screenshot.png'))
        self.label_img.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    # Процедура решения примера
    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x < 8:
                answer = 6 * ((a ** 2) + x + (b ** 2)) / (a * b * x)
            else:
                answer = 4 * ((a ** 2 - x + (b ** 2)))
            self.label_answer.setText('Ответ: ' + str(format(answer, '.2f')))
        except:
            self.label_answer.setText(
                'Ошибка!')

    # Процедура очистки данных
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')


# Основная часть программы
app = QApplication(sys.argv)
app.setWindowIcon(QIcon('favicon.png'))
window = Main()  # базовый класс окна
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения
