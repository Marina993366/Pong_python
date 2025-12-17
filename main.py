# importaciones
import time
from game_objects import (
    crear_ventana, crear_paleta, crear_pelota, crear_marcador
)
from game_utils import (
    mover_paleta_arriba, mover_paleta_abajo,
    actualizar_marcador, resetear_pelota,
    mostrar_mensaje_final, salir
)

# ===========================
# Función principal del juego
# ===========================
def main():
    ventana= crear_ventana()
    paleta_a = crear_paleta(-350, 0)
    paleta_b = crear_paleta(350, 0)
    pelota = crear_pelota()
    marcador = crear_marcador()

    # Teclas para mover las paletas
    ventana.listen()
    ventana.onkeypress(lambda: mover_paleta_arriba(paleta_a), "w")
    ventana.onkeypress(lambda: mover_paleta_arriba(paleta_a), "W")
    ventana.onkeypress(lambda: mover_paleta_abajo(paleta_a), "s")
    ventana.onkeypress(lambda: mover_paleta_abajo(paleta_a), "S")
    ventana.onkeypress(lambda: mover_paleta_arriba(paleta_b), "Up")
    ventana.onkeypress(lambda: mover_paleta_abajo(paleta_b), "Down")

    # Marcador
    score_a = 0
    score_b = 0

    # Puntaje maximo
    puntaje_maximo = 5

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

        # Anotar puntos
        if pelota.xcor() > 390:
            score_a += 1
            marcador.clear()
            actualizar_marcador(marcador, score_a, score_b)
            resetear_pelota(pelota)

        if pelota.xcor() < -390:
            score_b += 1
            marcador.clear()
            actualizar_marcador(marcador, score_a, score_b)
            resetear_pelota(pelota)

        # Rebotar en las paletas
        if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_b.ycor() + 50 and pelota.ycor() > paleta_b.ycor() - 50):
            pelota.dx *= -1.5

        if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_a.ycor() + 50 and pelota.ycor() > paleta_a.ycor() - 50):
            pelota.dx *= -1.5

        # Verificar si alguien ganó
        if score_a >= puntaje_maximo:
            marcador.clear()
            marcador.write("Jugador A gana!",
                            align="center",
                            font=("Courier", 36, "normal"))
            break
        if score_b >= puntaje_maximo:
            marcador.clear()
            marcador.write("Jugador B gana!",
                            align="center",
                            font=("Courier", 36, "normal"))
            break
    
    mostrar_mensaje_final("Fin del juego\nPresioná R para volver a jugar\nPresioná Q para salir")
    ventana.onkeypress(main, "r")
    ventana.onkeypress(main, "R")
    ventana.onkeypress(salir, "q")
    ventana.onkeypress(salir, "Q")
    ventana.mainloop()

if __name__ == "__main__":
    main()
