import turtle
import math

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Задание 3 - График через ряд")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# Функция подсчета ряда
def calc_ln(x, eps=0.001):
    s = 0.0
    n = 0
    term = x
    while abs(term) >= eps:
        s += term
        k = (x * x) * (2 * n + 1) / (2 * n + 3)
        term = term * k
        n += 1
    return 2 * s


# Оси
t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)  # X
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)  # Y

# Масштаб
scale_x = 250  # по X от -1 до 1
scale_y = 40  # по Y

t.penup()
first = True
x = -0.95
while x <= 0.95:
    y = calc_ln(x)

    px = x * scale_x
    py = y * scale_y

    if first:
        t.goto(px, py)
        t.pendown()
        first = False
    else:
        t.goto(px, py)
    x += 0.01

turtle.done()