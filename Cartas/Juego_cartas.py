"""Ejercicio 1 - Crear Baraja Española
Se desea realizar un método que a partir de las tres listas que se van a mostrar a continuación,
devuelva una lista de diccionario de cartas. Las listas que toma como partida son:
tipo = [1,2,3,4,5,6,7, Sota, Caballo, Rey] (Cadenas)
palos= [“Oro”, “Basto”, “Copa”, “Espadas”]
El diccionario que compondría la carta sería el siguiente:
carta = {
tipo: “1”,
palo: “Oro”,
valor: 0.0
}
Se tiene que devolver una lista de diccionarios, con todas las cartas de los 4 palos de la baraja."""
import random


def crear_baraja():

    tipos = [1, 2, 3, 4, 5, 6, 7, "Sota", "Caballo", "Rey"]
    palos = ["Oro", "Basto", "Copa", "Espadas"]
    cartas = []

    plantilla_carta = {
        "tipo": "",
        "palo": "",
        "valor": ""
    }
    for tipo in tipos:
        for palo in palos:
            carta = plantilla_carta.copy()
            carta["tipo"] = tipo
            carta["palo"] = palo
            cartas.append(carta)

    for carta in cartas:
        if isinstance(carta["tipo"], int):
            carta["valor"] = carta["tipo"]
        elif carta["tipo"] == "Sota":
            carta["valor"] = 10
        elif carta["tipo"] == "Caballo":
            carta["valor"] = 11
        elif carta["tipo"] == "Rey":
            carta["valor"] = 12

    return (cartas)

crear_baraja()

"""Ejercicio 2 - Barajar
Se desea realizar un método que reciba una lista de diccionarios de cartas y ponga las cartas
en posiciones aleatorias, simulando la acción de barajar. El método también devuelve una
lista de diccionarios con las cartas barajadas."""

def barajar_cartas():
    cartas = crear_baraja()
    cartas_barajadas = []

    for carta in cartas:
        orden = random.randint(0,len(cartas_barajadas))
        cartas_barajadas.insert(orden, carta)
    return (cartas_barajadas)

barajar_cartas()

"""Ejercicio 3 - Repartir cartas
Se desea realizar un método que simule la acción de repartir. Para ello el método recibe tres
parámetros:
● num_jugadores (int)
● num_cartas_por_jugador (int)
● baraja (list[diccionario])
El método debe devolver tantas listas como jugadores, y cada lista con el número de cartas
por jugador, sin repetir ninguna carta entre los jugadores. Además nada más empezar el
método hay que comprobar que el número de jugadores y las cartas que toca a cada jugador,
no supere el tamaño de la baraja. En el caso de no cumplirse la condición el método
devolverá un mensaje diciendo “Número de jugadores y cartas no válido”."""

def repartir_cartas (num_jug, num_cartas_jugador):

    cartas_barajadas = barajar_cartas()
    mazos_repartidos = []


    if num_jug*num_cartas_jugador > len(cartas_barajadas):
        print("Número de jugadores y cartas no válido")

    for jugador in range(num_jug):
        mazo_jugador = []
        for i in range(num_cartas_jugador):
            mazo_jugador.append(cartas_barajadas[0])
            cartas_barajadas.remove(cartas_barajadas[0])
        mazos_repartidos.append(mazo_jugador)
        #print(mazo_jugador)
    return mazos_repartidos

repartir_cartas(2,8)
