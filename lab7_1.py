import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Задание 1 - График функции")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Масштаб (чтобы график влез в экран: X от -5 до 11, Y от -3 до 2)
# Умножаем координаты на scale
scale = 40

# Центр экрана будет началом координат (0,0)
# Сдвигаем черепашку, чтобы график был по центру
t.penup()
t.goto(-350, 0)
t.pendown()
t.goto(350, 0)  # Ось X
t.penup()
t.goto(0, -250)
t.pendown()
t.goto(0, 250)  # Ось Y

# Рисуем график по точкам
t.penup()
first = True
x = -4.0
while x <= 10.0:
    if x < -2:
        y = 1.5 * x + 4
    elif x < 4:
        y = -0.5 * x
    elif x < 6:
        y = -2
    else:
        if 4 - (x - 8) ** 2 >= 0:
            y = -2 + (4 - (x - 8) ** 2) ** 0.5
        else:
            y = -2  # если вылезли за дугу

    # переводим в координаты экрана (ось Y в turtle смотрит вверх, поэтому просто умножаем)
    # сдвигаем по X на -300, чтобы график был виден
    px = x * scale - 100
    py = y * scale

    if first:
        t.goto(px, py)
        t.pendown()
        first = False
    else:
        t.goto(px, py)
    x += 0.05

turtle.done()