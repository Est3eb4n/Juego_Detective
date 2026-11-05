# cartas.py
# Manejo de la baraja: sobre secreto y reparto de cartas.
import random
from personajes import nombres_personajes
from armas import nombres_armas
from lugares_mansion import nombres_lugares

# Cartas que recibe cada jugador según cuántos jugadores haya.
# Con 2 jugadores: 8 cada uno y 3 descartadas (lo pide la guía).
CARTAS_POR_JUGADOR = {2: 8, 3: 6, 4: 4}


def todas_las_cartas():
    """Las 22 cartas del juego: 6 personajes + 7 armas + 9 lugares."""
    return nombres_personajes() + nombres_armas() + nombres_lugares()


def categoria_de(carta):
    """Devuelve 'personaje', 'arma' o 'lugar' según la carta."""
    if carta in nombres_personajes():
        return "personaje"
    if carta in nombres_armas():
        return "arma"
    return "lugar"


def crear_sobre_secreto():
    """Elige al azar 1 personaje, 1 arma y 1 lugar: la solución del caso."""
    return {
        "personaje": random.choice(nombres_personajes()),
        "arma": random.choice(nombres_armas()),
        "lugar": random.choice(nombres_lugares()),
    }


def repartir_cartas(sobre, num_jugadores):
    """Baraja las 19 cartas que no están en el sobre y las reparte.
    Devuelve (lista_de_manos, cartas_descartadas)."""
    restantes = []
    for carta in todas_las_cartas():
        if carta not in sobre.values():
            restantes.append(carta)
    random.shuffle(restantes)

    por_jugador = CARTAS_POR_JUGADOR[num_jugadores]
    manos = []
    for i in range(num_jugadores):
        inicio = i * por_jugador
        manos.append(restantes[inicio:inicio + por_jugador])
    descartadas = restantes[num_jugadores * por_jugador:]
    return manos, descartadas
