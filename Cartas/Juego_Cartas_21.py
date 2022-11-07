"""Reproduce mediante un método el juego de cartas del 21"""

from Cartas.Juego_cartas import *


# Definimos nuestro método para el juego del 21
def juego_el_21(num_jug):

    monton_1 = []
    monton_2 = []
    monton_3 = []
    monton_4 = []
    puntos_monton = 0
    cartas_repartidas = []
    puntos_jugadores = []

    # Tenemos nuestra cartas en el metodo anterior (repartir_cartas)
    cartas = repartir_cartas(num_jug, int(40/num_jug))

    # Condicionamos el numero de jugadores que pueden jugar y repartimos cartas
    if num_jug != 2 and num_jug != 4 and num_jug != 5 and num_jug != 8:
        print("No es posible repartir cartas de manera equitativa, sólo se aceptan 2,4,5 u 8 jugadores")
    else:
        cartas_repartidas=repartir_cartas(num_jug,int(40/num_jug))
        print(cartas_repartidas)

    # Iniciamos el juego mostrando por consola
    comienzo_partida = " COMIENZA EL JUEGO "
    print(comienzo_partida.center(50, "-"))
    print(" Montón 1 = " + str(monton_1) + " " + str(puntos_monton) + " puntos ")
    print(" Montón 2 = " + str(monton_2) + " " + str(puntos_monton) + " puntos ")
    print(" Montón 3 = " + str(monton_3) + " " + str(puntos_monton) + " puntos ")
    print(" Montón 4 = " + str(monton_4) + " " + str(puntos_monton) + " puntos ")

    for jug in range(num_jug):
        print("----------------- TURNO JUGADOR " + str(jug+1) + "-----------------")
        cartas_jugador = cartas_repartidas[jug]
        for cartas in cartas_jugador:
            print("Tus cartas:" + str(cartas["tipo"]) + cartas["palo"])
        carta_elegida = int(input("¿Qué carta quieres poner? "))
        monton_elegido = int(input("¿En qué montón? "))

        if monton_elegido == 1:
            monton_1.append(cartas[jug][carta_elegida]["tipo"]["palo"])
        print(monton_1)




juego_el_21(8)