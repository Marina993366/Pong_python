import turtle
import random

# ===========================
# Mover las paletas
# ===========================
def mover_paleta_arriba(paleta):
    if paleta.ycor() < 250:
        y = paleta.ycor()
        y += 30
        paleta.sety(y)

def mover_paleta_abajo(paleta):
    if paleta.ycor() > -250:
        y = paleta.ycor()
        y -= 30
        paleta.sety(y)


# ===========================
# Actualizar el marcador
# ===========================
def actualizar_marcador(marcador, score_a, score_b):
    marcador.clear()
    marcador.write(f"Jugador A: {score_a}  Jugador B: {score_b}",
                    align="center",
                    font=("Courier", 24, "normal"))

# ===========================
# Resetear pelota con dirección aleatoria al anotar punto
# ==========================    
def resetear_pelota(pelota):
    pelota.goto(0, 0)
    pelota.dx = 1 * random.choice([-1, 1])
    pelota.dy = 1 * random.choice([-1, 1])

# ===========================
# Mostrar mensaje final
# ===========================
def mostrar_mensaje_final(mensaje):
    texto = turtle.Turtle()
    texto.hideturtle()
    texto.color("white")
    texto.penup()
    texto.goto(0, 0)
    texto.write(
        mensaje,
        align="center",
        font=("Courier", 20, "normal")
    )

# ===========================
# Salir del juego
# ===========================
def salir():
    turtle.bye()
