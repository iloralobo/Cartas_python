"""Reproduce mediante un método el juego de cartas del 7,5"""

from Cartas.Juego_cartas import *
from os import system
import  time

# Tenemos nuestra cartas en el metodo anterior (barajar_cartas)
cartas = barajar_cartas()

# Vamos a darle valor a cada carta
for carta in cartas:
    if isinstance(carta["tipo"], int):
        carta["valor"] = carta["tipo"]
    else:
        carta["valor"] = 0.5

# Declaramos ahora el metodo para nuestro juego
def juego_siete_y_medio (num_jugadores):

    cartas_repartidas = []
    puntos_totales = []

    # Queremos ir ahora jugador x jugador
    for jug in range(num_jugadores):
        puntuacion_actual = 0.0
        respuesta = "si"
        comienzo_partida = "JUGADOR " + str(jug + 1)
        print(comienzo_partida.center(50, "-"))
        print("Jugador " + str(jug+1) + " esta es tu carta:")

        # Definimos ahora un bucle en el cual, mientras el jugador conteste "si" recibirá una carta
        while respuesta == "si":
            cartas_repartidas.append(cartas[0])
            cartas.remove(cartas[0])
            print("Tu carta: " + str(cartas[0]["tipo"])+ " " + str(cartas[0]["palo"]))
            puntuacion_actual += (cartas[0]["valor"])
            print("Puntuacion actual: " + str(puntuacion_actual) + "puntos")
            respuesta = input("¿Quieres otra carta? ").lower()

        # Si la respuesta del jugador en cambio es "no", se borrará consola y comienza el turno del siguiente juugador

        else:
            time.sleep(3)
            system("cls")

        # Añadimos a una lista la puntuacion de cada jugador
        puntos_totales.append(puntuacion_actual)

    diferencias = []
    ganadores = []

    # Recorremos cada puntuación para obtener quien se acerca más a 7.5 ptos (diferencia en valores absolutos)
    for puntuacion_jug in puntos_totales:
        diferencia = 7.5 - puntuacion_jug
        valores_absolutos = abs(diferencia)
        diferencias.append(valores_absolutos)

    # Declaramos cual es la diferencia menor en la variable minimo
    minimo = min(diferencias, key=lambda x: float(x))

    # Ahora recorremos cada posición de la lista diferencias, y la añadimos a la lista ganadores en el caso que su valor sea igual al minimo
    for indice in range(0, len(diferencias)):
        if diferencias[indice] == minimo:
            ganadores.append(indice)

    # Por último realizamos un condicional para saber si existe un solo ganador o varios
    if len(ganadores) == 1:
        print("Ha ganado el jugador : " + str(ganadores[0] + 1))
    else:
        print(" Se ha producido un empate entre los jugadores ")
        for ganador in ganadores:
            print(ganador+1)


juego_siete_y_medio(2)
