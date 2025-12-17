# importaciones
import turtle
import time


# ===========================
# Crear la ventana del juego
# ===========================
def crear_ventana():
    ventana = turtle.Screen()
    ventana.title("Pong - Python")
    ventana.bgcolor("black")
    ventana.setup(width=800, height=600)
    ventana.tracer(0)  # controlamos cuándo se actualiza la pantalla
    return ventana

# ===========================
# Crear las paletas
# ===========================

def crear_paleta(x, y):
    paleta = turtle.Turtle()
    paleta.speed(0)
    paleta.shape("square")
    paleta.color("white")
    paleta.shapesize(stretch_wid=5, stretch_len=1)
    paleta.penup()
    paleta.goto(x, y)
    return paleta

# ===========================
# Crear la pelota
# ===========================
def crear_pelota():
    pelota = turtle.Turtle()
    pelota.speed(0)
    pelota.shape("square")
    pelota.color("white")
    pelota.penup()
    pelota.goto(0, 0)
    pelota.dx = 0.1  # velocidad en x
    pelota.dy = -0.1  # velocidad en y
    return pelota

# ===========================
# Mover las paletas
# ===========================
def mover_paleta_arriba(paleta):
    y = paleta.ycor()
    y += 30
    paleta.sety(y)

def mover_paleta_abajo(paleta):
    y = paleta.ycor()
    y -= 30
    paleta.sety(y)

# ===========================
# Función principal del juego
# ===========================
def main():
    ventana= crear_ventana()
    paleta_a = crear_paleta(-350, 0)
    paleta_b = crear_paleta(350, 0)
    pelota = crear_pelota()

# ===========================    
# Teclas para mover las paletas
# ===========================
    ventana.listen()
    ventana.onkeypress(lambda: mover_paleta_arriba(paleta_a), "w")
    ventana.onkeypress(lambda: mover_paleta_abajo(paleta_a), "s")
    ventana.onkeypress(lambda: mover_paleta_arriba(paleta_b), "Up")
    ventana.onkeypress(lambda: mover_paleta_abajo(paleta_b), "Down")

# ===========================
# Bucle principal del juego
# ===========================
    while True:
        ventana.update()
        time.sleep(0.01)

        # Mover la pelota
        pelota.setx(pelota.xcor() + pelota.dx)
        pelota.sety(pelota.ycor() + pelota.dy)

        # Rebotar en los bordes
        if pelota.ycor() > 290:
            pelota.sety(290)
            pelota.dy *= -1

        if pelota.ycor() < -290:
            pelota.sety(-290)
            pelota.dy *= -1

        if pelota.xcor() > 390:
            pelota.goto(0, 0)
            pelota.dx *= -1

        if pelota.xcor() < -390:
            pelota.goto(0, 0)
            pelota.dx *= -1

        # Rebotar en las paletas
        if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_b.ycor() + 50 and pelota.ycor() > paleta_b.ycor() - 50):
            pelota.dx *= -1

        if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_a.ycor() + 50 and pelota.ycor() > paleta_a.ycor() - 50):
            pelota.dx *= -1

if __name__ == "__main__":
    main()