import turtle
import time

# Ekranı ayarla
ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.title("Kaplumbağa Şekilli Kalp")

# Kaplumbağa oluştur
kalem = turtle.Turtle()
kalem.shape("turtle")   # kaplumbağa şekli
kalem.color("red")
kalem.pensize(4)
kalem.speed(2)           # çizim hızı

# Başlangıç pozisyonu (hafif sola kaydırıldı)
kalem.penup()
kalem.goto(-5, -200)      # alt uç için hafif kaydırma
kalem.pendown()

# Kalp çizimi
kalem.begin_fill()
kalem.left(140)             # hafif açı düzeltmesiyle daha düzgün alt uç
kalem.forward(220)          # gövde uzunluğu
kalem.circle(-112, 200)     # sol üst yuvarlak
kalem.left(120)
kalem.circle(-112, 200)     # sağ üst yuvarlak
kalem.forward(221)          # alt gövde
kalem.end_fill()

# Kaplumbağayı gizle
kalem.hideturtle()

# Pencereyi açık tut
turtle.done()
