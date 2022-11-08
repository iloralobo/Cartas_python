"""Reproduce mediante un método el juego de cartas del 21"""

from Cartas.Juego_cartas import *
from os import system
import  time

# Definimos nuestro método para el juego del 21
def juego_el_21(num_jug):

    monton_1 = []
    puntos_monton_1 = 0
    monton_2 = []
    puntos_monton_2 = 0
    monton_3 = []
    puntos_monton_3 = 0
    monton_4 = []
    puntos_monton_4 = 0
    cartas_repartidas = []
    puntos_jugadores = []
    ganadores = []


    for jug in range(num_jug):
        puntos_jugadores.append(0)

    # Tenemos nuestra cartas en el metodo anterior (repartir_cartas)
    cartas = repartir_cartas(num_jug, int(40/num_jug))

    # Condicionamos el numero de jugadores que pueden jugar y repartimos cartas
    if num_jug != 2 and num_jug != 4 and num_jug != 5 and num_jug != 8:
        print("No es posible repartir cartas de manera equitativa, sólo se aceptan 2,4,5 u 8 jugadores")
    else:
        cartas_repartidas=repartir_cartas(num_jug,int(40/num_jug))
        #print(cartas_repartidas)

    # Iniciamos el juego mostrando por consola
    comienzo_partida = " COMIENZA EL JUEGO "
    print(comienzo_partida.center(50, "-"))
    print("Montón 1 = " + str(monton_1) + " " + str(puntos_monton_1) + " puntos ")
    print("Montón 2 = " + str(monton_2) + " " + str(puntos_monton_2) + " puntos ")
    print("Montón 3 = " + str(monton_3) + " " + str(puntos_monton_3) + " puntos ")
    print("Montón 4 = " + str(monton_4) + " " + str(puntos_monton_4) + " puntos ")
    time.sleep(1)
    system("cls")

    while puntos_monton_1 < 21 or puntos_monton_2 < 21 or puntos_monton_3 < 21 or puntos_monton_4 < 21:

        for jug in range(num_jug):
            print("----------------- TURNO JUGADOR " + str(jug+1) + "-----------------")
            cartas_jugador = cartas_repartidas[jug]

            for cartas in cartas_jugador:
                print("Tus cartas: " + str(cartas["tipo"]) + " " + cartas["palo"])
            print("Montón 1 = " + str(monton_1) + " " + str(puntos_monton_1) + " puntos ")
            print("Montón 2 = " + str(monton_2) + " " + str(puntos_monton_2) + " puntos ")
            print("Montón 3 = " + str(monton_3) + " " + str(puntos_monton_3) + " puntos ")
            print("Montón 4 = " + str(monton_4) + " " + str(puntos_monton_4) + " puntos ")
            carta_elegida = int(input("¿Qué carta quieres poner? "))
            monton_elegido = int(input("¿En qué montón? "))

            while (monton_elegido == 1 and puntos_monton_1 >=21) or (monton_elegido == 2 and puntos_monton_2 >= 21) or (monton_elegido == 3 and puntos_monton_3 >= 21) or (monton_elegido == 4 and puntos_monton_4 >= 21):
                monton_elegido = int(input("Ese montón ya tiene 21 o más puntos,diga otro montón "))

            if monton_elegido == 1:
                monton_1.append(cartas_jugador[carta_elegida])
                puntos_monton_1 +=(cartas_jugador[carta_elegida]["valor"])
                if puntos_monton_1 == 21:
                    puntos_jugadores[jug] +=1
                    print(puntos_jugadores)
            if monton_elegido == 2:
                monton_2.append(cartas_jugador[carta_elegida])
                puntos_monton_2 += (cartas_jugador[carta_elegida]["valor"])
                if puntos_monton_2 == 21:
                    puntos_jugadores[jug] +=1
                    print(puntos_jugadores)
            if monton_elegido == 3:
                monton_3.append(cartas_jugador[carta_elegida])
                puntos_monton_3 += (cartas_jugador[carta_elegida]["valor"])
                if puntos_monton_3 == 21:
                    puntos_jugadores[jug] +=1
                    print(puntos_jugadores)
            if monton_elegido == 4:
                monton_4.append(cartas_jugador[carta_elegida])
                puntos_monton_4 += (cartas_jugador[carta_elegida]["valor"])
                if puntos_monton_4 == 21:
                    puntos_jugadores[jug] +=1
                    print(puntos_jugadores)
            cartas_jugador.pop(carta_elegida)

        if puntos_monton_1 >= 21 and puntos_monton_2 >= 21 and puntos_monton_3 >= 21 and puntos_monton_4 >= 21:
            break
            break
    print("Ha ganado el jugador : " + str(ganadores[0]))



juego_el_21(2)