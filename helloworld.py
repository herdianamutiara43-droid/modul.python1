import turtle

# mengatur layar
screen =  turtle.screen()
screen.title("Gambar Bangun Datar - python Turtle")
screen.bgcolor("white")

# Membuat objek turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# --- Fungsi untuk Menggambar Bangun datar ---

# 1. persegi panjang 
def draw_rectangle(x, y, width, height, color):
t.penup()
t.goto(x, y)
t.pendown()
t.color(color)
t.begin_fill()
for _ in range(2)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
t.end_fill()

#