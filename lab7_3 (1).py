import math
import turtle

# --- 1. ИСХОДНЫЕ ДАННЫЕ ---
x_min = -0.99
x_max = 0.99
eps = 1e-3  # Точность 10^-3


# --- 2. РЕКУРРЕНТНОЕ ВЫЧИСЛЕНИЕ РЯДА ---
def calc_series(x, eps=1e-3):
  s = 0.0
  # Начальные значения (n = 0)
  num = x  # Числитель p_0 = x
  den = 1.0  # Знаменатель d_0 = 1
  term = num / den  # Нулевой член ряда a_0
  x2 = x * x  # Константа для рекуррентного шага

  while abs(2 * term) >= eps:
    s += term
    # Рекуррентный переход к следующему члену ряда:
    num = num * x2
    den = den + 2.0
    term = num / den

  return 2 * s


# --- 3. НАСТРОЙКА ОКНА БЕЗ ПРИВЯЗКИ К РАЗРЕШЕНИЮ ---
screen = turtle.Screen()
screen.setup(width=0.85, height=0.85)  # 85% любого экрана
screen.title("Задание 3 — Вариант 5")
screen.tracer(0)

W = screen.window_width()
H = screen.window_height()

margin_left = W * 0.08
margin_right = W * 0.08
margin_top = H * 0.12
margin_bottom = H * 0.08

# --- 4. РАСЧЁТ ТОЧЕК И ЕДИНЫЙ МАСШТАБ (1:1 КАК В DESMOS) ---
points = []
steps_count = 600
step = (x_max - x_min) / steps_count

for i in range(steps_count + 1):
  x = x_min + i * step
  y = calc_series(x, eps)
  points.append((x, y))

y_vals = [y for _, y in points]

max_abs_y = max(abs(min(y_vals)), abs(max(y_vals)), 6.0)
y_limit = math.ceil(max_abs_y / 2) * 2

plot_w = W - margin_left - margin_right
plot_h = H - margin_top - margin_bottom

scale = plot_h / (2 * y_limit)
x_limit = math.floor((plot_w / 2) / scale)
if x_limit < 2:
  x_limit = 2

scale = min(plot_w / (2 * x_limit), plot_h / (2 * y_limit))


def to_screen(x, y):
  return x * scale, y * scale


t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# --- 5. ЗАГОЛОВОК ---
t.penup()
t.goto(0, H / 2 - margin_top * 0.65)
t.write(
    f"График функции y = ln((1+x)/(1-x)) через ряд (точность {eps})",
    align="center",
    font=("Arial", 14, "bold"),
)

# --- 6. КООРДИНАТНАЯ СЕТКА ---
t.color("#E0E0E0")
t.pensize(1)

for gx in range(-x_limit, x_limit + 1):
  if gx == 0:
    continue
  px, _ = to_screen(gx, 0)
  _, py_top = to_screen(0, y_limit)
  _, py_bot = to_screen(0, -y_limit)
  t.penup()
  t.goto(px, py_bot)
  t.pendown()
  t.goto(px, py_top)

for gy in range(-y_limit, y_limit + 1):
  if gy == 0:
    continue
  _, py = to_screen(0, gy)
  px_left, _ = to_screen(-x_limit, 0)
  px_right, _ = to_screen(x_limit, 0)
  t.penup()
  t.goto(px_left, py)
  t.pendown()
  t.goto(px_right, py)

# --- 7. ОСИ КООРДИНАТ, СТРЕЛКИ И НАИМЕНОВАНИЯ ---
t.color("black")
t.pensize(2)

px_left, _ = to_screen(-x_limit, 0)
px_right, _ = to_screen(x_limit, 0)
_, py_bot = to_screen(0, -y_limit)
_, py_top = to_screen(0, y_limit)

# Ось X
t.penup()
t.goto(px_left, 0)
t.pendown()
t.goto(px_right + 15, 0)
t.goto(px_right + 5, 5)
t.penup()
t.goto(px_right + 15, 0)
t.pendown()
t.goto(px_right + 5, -5)

t.penup()
t.goto(px_right + 20, -8)
t.write("X", font=("Arial", 12, "bold"))

# Ось Y
t.penup()
t.goto(0, py_bot)
t.pendown()
t.goto(0, py_top + 15)
t.goto(-5, py_top + 5)
t.penup()
t.goto(0, py_top + 15)
t.pendown()
t.goto(5, py_top + 5)

t.penup()
t.goto(10, py_top + 10)
t.write("Y", font=("Arial", 12, "bold"))

# --- 8. ГРАДАЦИИ ОСЕЙ ---
font_ticks = ("Arial", 9, "normal")
t.pensize(1)

step_x = 2 if x_limit >= 4 else 1
for gx in range(-x_limit, x_limit + 1, step_x):
  if gx == 0:
    continue
  px, _ = to_screen(gx, 0)
  t.penup()
  t.goto(px, -4)
  t.pendown()
  t.goto(px, 4)
  t.penup()
  t.goto(px, -18)
  t.write(str(gx), align="center", font=font_ticks)

step_y = 2 if y_limit >= 4 else 1
for gy in range(-y_limit, y_limit + 1, step_y):
  if gy == 0:
    continue
  _, py = to_screen(0, gy)
  t.penup()
  t.goto(-4, py)
  t.pendown()
  t.goto(4, py)
  t.penup()
  t.goto(-10, py - 6)
  t.write(str(gy), align="right", font=font_ticks)

t.penup()
t.goto(-10, -16)
t.write("0", align="center", font=font_ticks)

# --- 9. САМ ГРАФИК ФУНКЦИИ ---
t.color("#C74440")
t.pensize(2.5)
t.penup()

for i, (x, y) in enumerate(points):
  px, py = to_screen(x, y)
  if i == 0:
    t.goto(px, py)
    t.pendown()
  else:
    t.goto(px, py)

screen.update()
turtle.done()
