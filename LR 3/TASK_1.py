import turtle


t = turtle.Turtle()
t.speed(2)


def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Рисуем лицо
draw_circle("yellow", 100, 0, -100)

# Рисуем глаза

draw_circle("red", 10, -35, 10)  # Левый глаз
draw_circle("black", 5, -35, 13)  # Левый глаз

draw_circle("red", 8, 35, 10)   # Правый глаз
draw_circle("black", 4, 35, 13)   # Правый глаз

# Рисуем злую улыбку
t.penup()
t.goto(-40, -20)


t.right(90)
t.forward(10)
t.pendown()
t.forward(10)

t.begin_fill()
t.fillcolor("black")
t.left(90)
t.forward(80)
t.left(90)
t.forward(10)
t.left(90)
t.forward(80)
t.end_fill()

t.penup()
t.goto(-20, 40)


t.pendown()
t.begin_fill()
t.fillcolor("black")
t.right(35)
t.forward(40)
t.left(90)
t.forward(8)
t.left(90)
t.forward(40)
t.end_fill()

# Завершение
t.hideturtle()
turtle.done()
