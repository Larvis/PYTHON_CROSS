#!/usr/bin/env python3
# coding=utf-8

# Из имеющегося словаря выбрать наиболее длинное слово, в котором все буквы разные, например:
# ЛЕЙКОПЛАСТЫРЬ, НЕРЯШЛИВОСТЬ, ЧЕТЫРЕХДЮЙМОВКА

import re
import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)
        self.setWindowIcon(QIcon('logo_e.png'))

        self.setWindowTitle('Работа со строками в Python')

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        txt=text.split()
        longest_word = ''
        for s in txt:
            # Задача: Из имеющегося словаря выбрать наиболее длинное слово, в котором все буквы разные, например:
            # ЛЕЙКОПЛАСТЫРЬ, НЕРЯШЛИВОСТЬ, ЧЕТЫРЕХДЮЙМОВКА

            # self.textEdit_words.insertPlainText(s + "\n")  # s.upper()[::-1]+"\n"
            is_unique = True
            for i in range(len(s) - 1):
                for j in range(i + 1, len(s)):
                    if s[i] == s[j]:
                        print("")
                        # quit()
                        is_unique = False
                        if not is_unique:
                            break
                if not is_unique:
                    break

            if is_unique:
                self.textEdit_words.insertPlainText(s + " - Уникальные буквы" + "\n")
                if len(longest_word) < len(s):
                    longest_word = s
            else:
                # pass
                self.textEdit_words.insertPlainText(s + " - Есть одинаковые" + "\n")

            is_unique = True

        self.textEdit_words.insertPlainText(" ------------------------ " + "\n")
        self.textEdit_words.insertPlainText(longest_word + " - самое длинное слово" + "\n")

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('logo_e.png'))
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
