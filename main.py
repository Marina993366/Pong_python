# importar la biblioteca turtle
import turtle

# Crear la ventana del juego
ventana = turtle.Screen()
ventana.title("Pong - Python")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)  # controlamos cuándo se actualiza la pantalla

# Mantener la ventana abierta
while True:
    ventana.update()

