#!/usr/bin/env python3
# coding=utf-8

import turtle

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
bob.fillcolor("#d6935d")
bob.begin_fill()

# Начинаем построение фронатальной стороны коробки
draw_bob("left", 155, 100)
draw_bob("right", 65, 100)
draw_bob("right", 115, 100)

# Заканчиваем окрашивать фронатальную сторону коробки
bob.end_fill()

# --- Боковая сторона коробки ---
# Начинаем окрашивать боковую сторону коробки
bob.fillcolor("#cb8953")
bob.begin_fill()

# Начинаем построение боковой стороны коробки
draw_bob("right", 65, 100)
draw_bob("left", 115, 100)
draw_bob("left", 65, 100)
draw_bob("left", 115, 100)

# Заканчиваем окрашивать фронатальную сторону коробки
bob.end_fill()

# --- Крышка коробки ---
# Начинаем окрашивать крышку коробки
bob.fillcolor("#d2935f")
bob.begin_fill()

# Начинаем построение крышки коробки
draw_bob("left", 100, 30)
draw_bob("left", 80, 100)
draw_bob("left", 100, 30)

# Заканчиваем окрашивать крышку коробки
bob.end_fill()

# --- Внутренняя задняя стенка коробки ---
# Начинаем окрашивать внутреннюю заднюю стенку коробки
bob.fillcolor("#9e693d")
bob.begin_fill()

# Начинаем построение внутренней задней стенки коробки
draw_bob("left", 30, 100)
draw_bob("left", 115, 85)

# Заканчиваем окрашивать внутренней задней стенки коробки
bob.end_fill()

# --- Внутренняя левая стенка коробки ---
# Начинаем окрашивать внутреннюю левую стенку коробки
bob.fillcolor("#9e693d")
bob.begin_fill()

# Начинаем построение внутренней левой стенки коробки
bob.back(85)
draw_bob("right", 65, 100)

# Заканчиваем окрашивать внутреннюю левую стенку коробки
bob.end_fill()

# --- Внутренняя обшивка левой стенки коробки ---
# Начинаем окрашивать внутреннюю обшивку левой стенки коробки
bob.fillcolor("#d6935d")
bob.begin_fill()

# Начинаем построение внутренней обшивки левой стенки коробки
draw_bob("left", 130, 29)

bob.color("#d6935d")
draw_bob("left", 49, 69)
draw_bob("left", 65, 27)

bob.up()
bob.right(90)
bob.up()
bob.forward(2)

# Заканчиваем окрашивать внутреннюю обшивку левой стенки коробки
bob.end_fill()

# --- Внутренняя обшивка правой стенки коробки ---
# Начинаем окрашивать внутреннюю обшивку правой стенки коробки
bob.fillcolor("#d6935d")
bob.begin_fill()

# Начинаем построение внутренней обшивки правой стенки коробки
draw_bob("right", 90, 26)
draw_bob("left", 67, 72)
draw_bob("left", 45, 28)

# Заканчиваем окрашивать внутреннюю обшивку правой стенки коробки
bob.end_fill()

# (2) --- Фронатальная сторона коробки ---
draw_turtle("left", 155, 100)
draw_turtle("right", 65, 100)
draw_turtle("right", 115, 100)

# --- Боковая сторона коробки ---
draw_turtle("right", 65, 100)
draw_turtle("left", 115, 100)
draw_turtle("left", 65, 100)
turtle.width(2)
draw_turtle("left", 115, 100)
turtle.width(1)

# --- Крышка коробки ---
# Начинаем окрашивать крышку коробки
turtle.fillcolor("#d2935f")
turtle.begin_fill()

draw_turtle("left", 100, 30)
draw_turtle("left", 80, 100)
draw_turtle("left", 100, 30)

# Заканчиваем окрашивать крышку коробки
turtle.end_fill()

# --- Внутренняя задняя стенка коробки ---
draw_turtle("left", 30, 100)
draw_turtle("left", 115, 85)

# --- Внутренняя левая стенка коробки ---
turtle.back(85)
draw_turtle("right", 65, 100)

turtle.done()
