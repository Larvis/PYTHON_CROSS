#!/usr/bin/env python3
# coding=utf-8

while True:
    try:
        a = float(input('Введи А = '))
        b = float(input('Введи B = '))
        x = float(input('Введи X = '))
        if x < 8:
            answer = 6 * ((a ** 2) + x + (b ** 2)) / (a * b * x)
        else:
            answer = 4 * (a ** 2 - x + (b ** 2))
        print('Ответ: ' + str(format(answer, '.2f')))

        re = input('Повторить? (Y/n) ')
        if re == 'n':
            break
    except:
        print('Ошибка!')

        re = input('Повторить? (Y/n) ')
        if re == 'n':
            break
