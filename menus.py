# menus.py
# Todos los menús del juego. Cada función dibuja el menú y devuelve la opción elegida.
from utilidades import leer_opcion

ANCHO = 39


def dibujar_menu(titulo, opciones):
    print()
    print(" " + "_" * ANCHO)
    print("|" + (" " + titulo + " ").center(ANCHO, "=") + "|")
    print("|" + " " * ANCHO + "|")
    for i in range(len(opciones)):
        texto = f"{i + 1}. {opciones[i]}"
        print("|" + ("     " + texto).ljust(ANCHO) + "|")
        print("|" + " " * ANCHO + "|")
    print("|" + "_" * ANCHO + "|")
    print()


def pedir_menu(titulo, opciones):
    dibujar_menu(titulo, opciones)
    return leer_opcion("  Elige una opción: ", 1, len(opciones))


def menu_principal():
    return pedir_menu("Bienvenido al juego", [
        "Dos jugadores",
        "Jugar contra la PC",
        "Hasta 4 jugadores (BONUS)",
        "Salir"])


def menu_total_jugadores():
    """Devuelve 2, 3 o 4."""
    opcion = pedir_menu("Total de jugadores", ["2 jugadores", "3 jugadores", "4 jugadores"])
    return opcion + 1


def menu_cantidad_humanos(total):
    """Cuántos de los jugadores son personas (el resto lo ocupa la PC)."""
    opciones = []
    for h in range(1, total + 1):
        opciones.append(f"{h} humano(s), {total - h} PC")
    return pedir_menu("Jugadores humanos", opciones)


def menu_acciones_turno():
    return pedir_menu("Opciones de turno", [
        "Realizar suposición",
        "Realizar acusación",
        "Ver hoja del detective"])


def menu_post_suposicion():
    return pedir_menu("Hoja del detective", [
        "Anotar en la hoja",
        "Continuar jugando"])


def menu_anotar():
    return pedir_menu("Anotar en la hoja", [
        "Un personaje",
        "Un arma",
        "Un lugar",
        "Los tres a la vez",
        "Terminar de anotar"])


def menu_estado():
    return pedir_menu("Estado de la carta", [
        "Descartada (X)",
        "Sospechosa (?)",
        "Confirmada (OK)",
        "Borrar anotación (-)"])


def menu_fin_partida():
    return pedir_menu("Fin de la partida", [
        "Reintentar (mismo modo)",
        "Volver al menú principal"])
