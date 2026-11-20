import math
import random
import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Задание 2 - Мишень")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

R = 5
SCALE = 60  # Масштаб для красивой отрисовки (радиус на экране = 300 пикселей)
R_px = R * SCALE
N = 10000
hits = 0

# --- 1. РИСУЕМ СЕРУЮ ЗАЛИВКУ ---
t.color("lightgray")

# Верхняя правая четверть (I четверть)
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.goto(R_px, 0)
t.setheading(90)  # Направляем черепашку строго вверх
t.circle(R_px, 90)
t.goto(0, 0)
t.end_fill()

# Нижняя левая четверть (III четверть)
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.goto(-R_px, 0)
t.setheading(270)  # Направляем черепашку строго вниз
t.circle(R_px, 90)
t.goto(0, 0)
t.end_fill()

# Треугольник в левой верхней четверти (II четверть)
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.goto(-R_px, 0)
t.goto(0, R_px)
t.goto(0, 0)
t.end_fill()

# --- 2. РИСУЕМ ОСИ И ОКРУЖНОСТЬ ---
t.color("black")
t.pensize(2)

# Ось X
t.penup()
t.goto(-R_px - 30, 0)
t.pendown()
t.goto(R_px + 30, 0)

# Ось Y
t.penup()
t.goto(0, -R_px - 30)
t.pendown()
t.goto(0, R_px + 30)

# Граница круга
t.penup()
t.goto(0, -R_px)
t.setheading(0)
t.pendown()
t.circle(R_px)

# --- 3. ГЕНЕРАЦИЯ ТОЧЕК (МЕТОД МОНТЕ-КАРЛО) ---
t.penup()
for _ in range(N):
  x = random.uniform(-R, R)
  y = random.uniform(-R, R)

  # Проверяем, что точка внутри круга
  if x * x + y * y <= R * R:
    inside = False

    # 1. Верхняя правая четверть
    if x >= 0 and y >= 0:
      inside = True
    # 2. Нижняя левая четверть
    elif x <= 0 and y <= 0:
      inside = True
    # 3. Верхняя левая четверть (ниже гипотенузы y = x + R)
    elif x <= 0 and y >= 0:
      if y <= x + R:
        inside = True

    if inside:
      hits += 1
      t.color("green")
    else:
      t.color("red")

    t.goto(x * SCALE, y * SCALE)
    t.dot(4)

# --- 4. СЧИТАЕМ И ВЫВОДИМ ПЛОЩАДЬ ---
S_rect = (2 * R) * (2 * R)
S_mc = S_rect * (hits / N)
S_true = (math.pi * R * R) / 2 + (R * R) / 2
error = abs(S_mc - S_true) / S_true * 100

t.color("black")
t.penup()
t.goto(-R_px, R_px + 45)
t.write(
    f"Площадь МК: {S_mc:.2f} | Точная: {S_true:.2f} | Ошибка: {error:.2f}%",
    font=("Arial", 12, "bold"),
)

screen.update()
turtle.done()
