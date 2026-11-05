# hoja_detective.py
# La "Hoja del Detective": un diccionario {carta: estado} por jugador.
# Estados:  M = en mi mano | X = descartada | ? = sospechosa | OK = confirmada | - = sin anotar
from personajes import nombres_personajes
from armas import nombres_armas
from lugares_mansion import nombres_lugares
from cartas import todas_las_cartas
from menus import menu_anotar, menu_estado
from utilidades import elegir_de_lista

SIMBOLOS_ESTADO = ["X", "?", "OK", "-"]


def crear_hoja(mano):
    """Hoja nueva: todo sin anotar, y las cartas de la mano marcadas con M."""
    hoja = {}
    for carta in todas_las_cartas():
        hoja[carta] = "-"
    for carta in mano:
        hoja[carta] = "M"
    return hoja


def linea_tabla(c1, c2, c3, ancho):
    return ("|" + (" " + c1).ljust(ancho) + "|" + (" " + c2).ljust(ancho)
            + "|" + (" " + c3).ljust(ancho) + "|")


def texto_celda(hoja, lista, i):
    if i < len(lista):
        return f"[{hoja[lista[i]]:^3}] {lista[i]}"
    return ""


def mostrar_hoja(hoja, titulo="HOJA DEL DETECTIVE"):
    """Imprime la hoja en forma de tabla de 3 columnas."""
    personajes = nombres_personajes()
    armas = nombres_armas()
    lugares = nombres_lugares()
    ancho = 28
    borde = ("+" + "-" * ancho) * 3 + "+"

    print()
    print(titulo.center(len(borde)))
    print(borde)
    print(linea_tabla("PERSONAJES", "ARMAS", "LUGARES", ancho))
    print(borde)
    for i in range(len(lugares)):  # 9 filas (la columna más larga)
        print(linea_tabla(texto_celda(hoja, personajes, i),
                          texto_celda(hoja, armas, i),
                          texto_celda(hoja, lugares, i), ancho))
    print(borde)
    print("  M = en tu mano | X = descartada | ? = sospechosa | OK = confirmada | - = sin anotar")


def anotar_carta(hoja, carta, estado):
    """Cambia el estado de una carta (las de tu mano no se pueden cambiar)."""
    if hoja[carta] == "M":
        print(f"   '{carta}' está en tu mano, no se puede cambiar.")
        return
    hoja[carta] = estado


def pedir_estado():
    opcion = menu_estado()
    return SIMBOLOS_ESTADO[opcion - 1]


def editar_hoja(hoja):
    """Interfaz para anotar: una carta por categoría o las tres a la vez."""
    while True:
        mostrar_hoja(hoja)
        opcion = menu_anotar()
        if opcion == 1:
            carta = elegir_de_lista("Personajes:", nombres_personajes())
            anotar_carta(hoja, carta, pedir_estado())
        elif opcion == 2:
            carta = elegir_de_lista("Armas:", nombres_armas())
            anotar_carta(hoja, carta, pedir_estado())
        elif opcion == 3:
            carta = elegir_de_lista("Lugares:", nombres_lugares())
            anotar_carta(hoja, carta, pedir_estado())
        elif opcion == 4:
            p = elegir_de_lista("Personajes:", nombres_personajes())
            a = elegir_de_lista("Armas:", nombres_armas())
            l = elegir_de_lista("Lugares:", nombres_lugares())
            estado = pedir_estado()
            for carta in [p, a, l]:
                anotar_carta(hoja, carta, estado)
        else:
            break
