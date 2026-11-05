# juego.py
# Preparación y ciclo principal de una partida.
import random
from personajes import nombres_personajes, descripcion_personaje
from armas import descripcion_arma
from lugares_mansion import descripcion_lugar
from cartas import crear_sobre_secreto, repartir_cartas
from hoja_detective import crear_hoja
from ia_pc import crear_memoria
from menus import menu_total_jugadores, menu_cantidad_humanos
from turnos import turno_humano, turno_pc
from utilidades import elegir_de_lista, limpiar_pantalla, pausa


def crear_jugador(nombre, es_pc):
    return {"nombre": nombre, "es_pc": es_pc, "mano": [], "hoja": {},
            "memoria": {}, "activo": True}


def configurar_modo(opcion):
    """Convierte la opción del menú principal en una configuración de partida."""
    if opcion == 1:
        return {"humanos": 2, "total": 2}
    if opcion == 2:
        return {"humanos": 1, "total": 2}
    total = menu_total_jugadores()
    humanos = menu_cantidad_humanos(total)
    return {"humanos": humanos, "total": total}


def crear_jugadores(config):
    """Cada humano elige un personaje; la PC ocupa los personajes que quedan libres."""
    disponibles = nombres_personajes()
    if "avatares" not in config:  # solo se pregunta la primera vez (el replay los reutiliza)
        elegidos = []
        for i in range(config["humanos"]):
            print(f"\nJugador humano {i + 1}:")
            nombre = elegir_de_lista("Elige tu personaje:", disponibles)
            disponibles.remove(nombre)
            elegidos.append(nombre)
        config["avatares"] = elegidos
    else:
        for nombre in config["avatares"]:
            disponibles.remove(nombre)

    jugadores = []
    for nombre in config["avatares"]:
        jugadores.append(crear_jugador(nombre, False))
    random.shuffle(disponibles)
    for i in range(config["total"] - config["humanos"]):
        jugadores.append(crear_jugador("PC " + disponibles[i], True))
    return jugadores


def preparar_partida(config):
    sobre = crear_sobre_secreto()
    jugadores = crear_jugadores(config)
    manos, descartadas = repartir_cartas(sobre, len(jugadores))
    for i in range(len(jugadores)):
        jugadores[i]["mano"] = manos[i]
        jugadores[i]["hoja"] = crear_hoja(manos[i])
        if jugadores[i]["es_pc"]:
            jugadores[i]["memoria"] = crear_memoria()
    return {"jugadores": jugadores, "sobre": sobre, "descartadas": descartadas,
            "ganador": None, "num_humanos": config["humanos"]}


def mostrar_introduccion(partida):
    print("\n" + "=" * 62)
    print("  MISTERIO EN LA MANSIÓN SÁNCHEZ")
    print("=" * 62)
    print("  El amo de llaves apareció asesinado tras la reunión.")
    print("  Debes descubrir QUIÉN lo hizo, con QUÉ ARMA y en QUÉ LUGAR.")
    print("\n  Jugadores (en orden de turno):")
    for jugador in partida["jugadores"]:
        tipo = "controlado por la computadora" if jugador["es_pc"] else "humano"
        print(f"   - {jugador['nombre']} ({tipo}) - {len(jugador['mano'])} cartas")
    print(f"\n  Cartas descartadas fuera de juego: {len(partida['descartadas'])}")
    print("=" * 62)
    pausa()


def anunciar_final(partida):
    ganador = partida["jugadores"][partida["ganador"]]
    sobre = partida["sobre"]
    print("\n" + "*" * 62)
    print(f"  GANADOR: {ganador['nombre']}")
    print("*" * 62)
    print("  La solución del caso era:")
    print(f"   Asesino: {sobre['personaje']} - {descripcion_personaje(sobre['personaje'])}")
    print(f"   Arma:    {sobre['arma']} - {descripcion_arma(sobre['arma'])}")
    print(f"   Lugar:   {sobre['lugar']} - {descripcion_lugar(sobre['lugar'])}")
    print("*" * 62)


def jugar_partida(config):
    """Ciclo principal: turnos hasta que haya un ganador."""
    partida = preparar_partida(config)
    jugadores = partida["jugadores"]
    mostrar_introduccion(partida)

    indice = 0
    while partida["ganador"] is None:
        jugador = jugadores[indice]
        if jugador["activo"]:
            if jugador["es_pc"]:
                turno_pc(partida, indice)
            else:
                if partida["num_humanos"] > 1:  # que el otro humano no vea la pantalla
                    limpiar_pantalla()
                    pausa(f"\n  Turno de {jugador['nombre']}. Pasa el equipo y presiona Enter...")
                turno_humano(partida, indice)
                if partida["num_humanos"] > 1 and partida["ganador"] is None:
                    pausa("\n  Presiona Enter para terminar tu turno (se limpiará la pantalla)...")
                    limpiar_pantalla()
        indice = (indice + 1) % len(jugadores)

    anunciar_final(partida)
