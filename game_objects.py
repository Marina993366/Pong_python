import turtle

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
    pelota.dx = 1  # velocidad en x
    pelota.dy = -1  # velocidad en y
    return pelota

# ===========================
# Crear el marcador
# ===========================
def crear_marcador():
    marcador = turtle.Turtle()
    marcador.speed(0)
    marcador.color("white")
    marcador.penup()
    marcador.hideturtle()
    marcador.goto(0, 260)
    marcador.write("Jugador A: 0  Jugador B: 0",
                    align="center",
                    font=("Courier", 24, "normal"))
    return marcador
