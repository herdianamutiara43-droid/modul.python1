import turtle

t = turtle.Turtle()
t.speed(5)

# Persegi Panjang
t.penup()
t.goto(-250, 100)
t.pendown()
for i in range(2):
    t.forward(120)
    t.left(90)
    t.forward(70)
    t.left(90)

# Segitiga
t.penup()
t.goto(-50, 100)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)

# Trapesium
t.penup()
t.goto(150, 100)
t.pendown()
t.forward(140)
t.left(120)
t.forward(70)
t.left(60)
t.forward(80)
t.left(60)
t.forward(70)

# Jajar Genjang
t.penup()
t.goto(-200, -100)
t.pendown()
t.forward(120)
t.left(60)
t.forward(70)
t.left(120)
t.forward(120)
t.left(60)
t.forward(70)

# Belah Ketupat
t.penup()
t.goto(150, -100)
t.pendown()
for i in range(2):
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)

turtle.done()