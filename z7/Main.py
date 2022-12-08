#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

answers = ['', '', '']  # 1 - form2, 2 - form3, 3 - form4
twoFormChecked = ' '


class Form1(QtWidgets.QMainWindow):
    # аргумент str говорит о том, что сигнал должен быть сторокового типа
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form1, self).__init__()
        uic.loadUi('uis/form1.ui', self)

        self.setWindowTitle('Приветсвтие')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_exit.clicked.connect(self.close)
        self.btn_begin.clicked.connect(self.next)

    def next(self):
        self.switch_window.emit('1>2')


class Form2(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form2, self).__init__()
        uic.loadUi('uis/form2.ui', self)


        self.setWindowTitle('Детство')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        # устанавливаем картинку label_img
        self.label_img.setPixmap(QPixmap('images/car.jpg'))
        # подгоняем картинку под размер label_img
        self.label_img.setScaledContents(True)

        # если ранее ответ был уже выбран, то показываем его заново
        if answers[0] is not None:
            self.label_selected.setText('Выбрано!1: ' + answers[0])
            # print(answers)
        # radioButton_1
        # ставим события на radioButtons
        self.checkBox_1.toggled.connect(
            lambda: self.onToggled(self.checkBox_1))
        self.checkBox_2.toggled.connect(
            lambda: self.onToggled(self.checkBox_2))
        self.checkBox_3.toggled.connect(
            lambda: self.onToggled(self.checkBox_3))
        self.checkBox_4.toggled.connect(
            lambda: self.onToggled(self.checkBox_4))

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

        # self.onToggled(self.checkBox_1)

    def onToggled(self, radiobutton):
        twoFormChecked = ' '
        if self.checkBox_1.isChecked():
            twoFormChecked += ' ' + self.checkBox_1.text()
        if self.checkBox_2.isChecked():
            twoFormChecked += ' ' + self.checkBox_2.text()
        if self.checkBox_3.isChecked():
            twoFormChecked += ' ' + self.checkBox_3.text()
        if self.checkBox_4.isChecked():
            twoFormChecked += ' ' + self.checkBox_4.text()

        answers[0] = twoFormChecked
        self.label_selected.setText('Выбрано: ' + answers[0])

    def back(self):
        self.switch_window.emit('1<2')

    def next(self):
        self.switch_window.emit('2>3')


class Form3(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form3, self).__init__()
        uic.loadUi('uis/form3.ui', self)

        self.setWindowTitle('Отрочество')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/work.png'))
        self.label_img.setScaledContents(True)

        # если ранее ответ был уже выбран, то показываем его заново
        if answers[1] is not None:
            # print(answers)
            self.label_selected.setText('Выбрано: ' + answers[1])

        # ставим события на radioButtons
        self.radioButton_1.toggled.connect(
            lambda: self.onToggled(self.radioButton_1))
        self.radioButton_2.toggled.connect(
            lambda: self.onToggled(self.radioButton_2))
        self.radioButton_3.toggled.connect(
            lambda: self.onToggled(self.radioButton_3))
        self.radioButton_4.toggled.connect(
            lambda: self.onToggled(self.radioButton_4))


        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

        self.onToggled(self.radioButton_1)

    def onToggled(self, radiobutton):
        if radiobutton.isChecked():
            answers[1] = radiobutton.text()
            self.label_selected.setText('Выбрано: ' + answers[1])

    def back(self):
        self.switch_window.emit('2<3')

    def next(self):
        self.switch_window.emit('3>4')


class Form4(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form4, self).__init__()
        uic.loadUi('uis/form4.ui', self)

        self.setWindowTitle('Юность')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/education.png'))
        self.label_img.setScaledContents(True)

        if answers[2] is not None:
            self.label_selected.setText('Выбрано: ' + answers[2])

        # self.tableWidget.cellClicked
        self.tableWidget.cellClicked.connect(self.handleActivated)
        # self.tableWidget.cellClicked(1, 1).connect(self.handleActivated)
        # self.comboBox.activated.connect(self.handleActivated)

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

        self.handleActivated(0)

    def handleActivated(self, index):
        # row = self.tableWidget.currentRow()
        answers[2] = self.tableWidget.item(index, 0).text()
        # print(row)
        self.label_selected.setText('Выбрано: ' + answers[2])

    def back(self):
        self.switch_window.emit('3<4')

    def next(self):
        self.switch_window.emit('4>5')


class Form5(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form5, self).__init__()
        uic.loadUi('uis/form5.ui', self)

        self.setWindowTitle('Результат')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        # запрещаем редактирование таблицы
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # присваиваем значение ячейкам таблицы
        self.label_q_1.setText('Марка машиныу: ' + answers[0])
        self.label_q_2.setText('Профессия: ' + answers[1])
        self.label_q_3.setText('Удовлетворенность обучения: ' + answers[2])

        self.btn_back.clicked.connect(self.back)
        self.btn_exit.clicked.connect(self.close)

    def back(self):
        self.switch_window.emit("4<5")


'''
Класс управления переключения окон
'''


class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()

        if text == '1>2':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = Form5()
            self.form5.switch_window.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '4<5':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '3<4':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '2<3':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form3.close()

        if text == '1<2':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
