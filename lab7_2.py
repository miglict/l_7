import turtle
import random
import math

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Задание 2 - Мишень")
screen.tracer(0)  # без анимации

t = turtle.Turtle()
t.hideturtle()

R = 5
N = 10000
hits = 0

# масштаб (рисуем от -6 до 6 по обеим осям)
screen.setworldcoordinates(-R - 1, -R - 1, R + 1, R + 1)

# --- РИСУЕМ ГРАНИЦЫ ---
t.penup()
t.color("black")

# 1. Внешняя окружность (радиус R)
t.goto(0, -R)
t.pendown()
t.circle(R)

# 2. Прямая y = -x (диагональ из левого верхнего в правый нижний)
# (в turtle координаты (x, y) задаются напрямую)
t.penup()
t.goto(-R, R)
t.pendown()
t.goto(R, -R)

# 3. Ось X (чтобы видеть, где четверти)
t.penup()
t.goto(-R, 0)
t.pendown()
t.goto(R, 0)

# 4. Ось Y
t.penup()
t.goto(0, -R)
t.pendown()
t.goto(0, R)

# --- ГЕНЕРАЦИЯ ТОЧЕК ---
t.penup()
for _ in range(N):
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)

    # Проверяем попадание в круг
    if x * x + y * y <= R * R:
        inside = False
        # Верхняя правая четверть (x>0, y>0)
        if x >= 0 and y >= 0:
            inside = True
        # Нижняя левая четверть (x<0, y<0)
        elif x <= 0 and y <= 0:
            inside = True
        # Верхняя левая четверть, но только ТРЕУГОЛЬНИК (y <= -x)
        elif x <= 0 and y >= 0 and y <= -x:
            inside = True

        if inside:
            hits += 1
            t.color("green")
        else:
            t.color("red")
        t.goto(x, y)
        t.dot(4)  # чуть крупнее точки

screen.update()

# --- СЧИТАЕМ ПЛОЩАДЬ ---
# Площадь всего квадрата
S_rect = (2 * R) * (2 * R)  # = 100

# Площадь по Монте-Карло
S_mc = S_rect * (hits / N)

S_true = (math.pi * R * R) / 4 + (math.pi * R * R) / 4 + (R * R) / 2

error = abs(S_mc - S_true) / S_true * 100

# Выводим текст
t.color("black")
t.penup()
t.goto(-R, R + 0.5)
t.write(f"Площадь МК: {S_mc:.2f} | Точная: {S_true:.2f} | Ошибка: {error:.2f}%", font=("Arial", 12, "bold"))

turtle.done()