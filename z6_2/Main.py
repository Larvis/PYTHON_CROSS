#!/usr/bin/env python3
# coding=utf-8

import turtle
import math

bob = turtle.Turtle()


def draw_bob(left_or_right, angle, length):
    if left_or_right == "right":
        bob.right(angle)
    else:
        bob.left(angle)

    bob.forward(length)


def draw_turtle(left_or_right, angle, length):
    if left_or_right == "right":
        turtle.right(angle)
    else:
        turtle.left(angle)

    turtle.forward(length)




# (1) --- Фронатальная сторона коробки ---
# Начинаем окрашивать фронатальную сторону коробки
bob.fillcolor("#0028b8")
bob.begin_fill()

# Верхняя часть шапки 260х95 dots

draw_bob("right", 20, 140)
draw_bob("right", 140, 140)
draw_bob("right", 40, 140)
draw_bob("right", 140, 140)

# Заканчиваем окрашивать Верхняя часть шапки
bob.end_fill()

# Перемещение и маскировка до след. слоя
bob.color("#0028b8")
bob.back(140)
bob.right(20)

draw_bob("right", 0, 200) ## 65

bob.left(90)
bob.forward(15)
bob.color("#000000")

# Конец Перемещение и маскировка до след. слоя

## Окружность для головы
bob.fillcolor("#2453ff")
bob.begin_fill()

bob.left(69)
bob.circle(190, 45)

bob.left(65)
bob.forward(40)
bob.left(115)

bob.circle(-195, 45)

bob.left(112)
bob.forward(40)
bob.end_fill()

## Конец Окружность для головы
bob.left(180)
bob.forward(40)
bob.left(-66)
bob.fillcolor("#000")
bob.begin_fill()


bob.circle(-195, 46)
bob.left(-135)
bob.circle(-195, 46)
bob.end_fill()
## Конец Окружность для головы

bob.left(115)
bob.forward(40)

bob.fillcolor("#fbff00")
bob.begin_fill()

bob.circle(15)

bob.back(140)
bob.left(45)
bob.forward(15)
bob.right(90)
bob.back(15)
bob.left(37)
bob.forward(140)

bob.end_fill()

turtle.done()

