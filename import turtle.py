import turtle

# Setup layar
screen = turtle.Screen()
screen.title("Gambar Bangun Datar")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)
pen.pensize(2)

# =========================
# Fungsi Bangun Datar
# =========================

# Persegi Panjang
def persegi_panjang(panjang, lebar):
    for i in range(2):
        pen.forward(panjang)
        pen.left(90)
        pen.forward(lebar)
        pen.left(90)

# Segitiga Sama Sisi
def segitiga(sisi):
    for i in range(3):
        pen.foward(sisi)
        pen .left(120)

# Trapesium trapesium(atas, bawah, tinggi):
  pen.forward(bawah)
  pen. left(120)
  pen.forward(tinggi)
  pen.left(60)
