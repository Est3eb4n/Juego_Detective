# turnos.py
# Acciones de un turno: suposición, acusación, turno humano y turno de la PC.
import random
from personajes import nombres_personajes
from armas import nombres_armas
from lugares_mansion import nombres_lugares
from menus import menu_acciones_turno, menu_post_suposicion
from hoja_detective import mostrar_hoja, editar_hoja
from ia_pc import ia_decidir, ia_registrar_suposicion
from utilidades import elegir_de_lista, confirmar, pausa, pausa_corta


def pedir_combinacion(tipo):
    """Pide personaje, arma y lugar. Devuelve [personaje, arma, lugar]."""
    print(f"\n--- Tu {tipo} ---")
    personaje = elegir_de_lista("Personaje:", nombres_personajes())
    arma = elegir_de_lista("Arma:", nombres_armas())
    lugar = elegir_de_lista("Lugar:", nombres_lugares())
    return [personaje, arma, lugar]


def resolver_suposicion(jugadores, indice, suposicion):
    """Recorre a los demás jugadores en orden. El primero que tenga alguna de las
    3 cartas refuta. Devuelve (indice_refutador, carta_mostrada, indices_que_pasaron)."""
    pasaron = []
    for paso in range(1, len(jugadores)):
        j = (indice + paso) % len(jugadores)
        coincidencias = []
        for carta in suposicion:
            if carta in jugadores[j]["mano"]:
                coincidencias.append(carta)
        if len(coincidencias) > 0:
            return j, random.choice(coincidencias), pasaron
        pasaron.append(j)
    return None, None, pasaron


def notificar_pcs(partida, indice, suposicion, refutador, carta, pasaron):
    """Todas las PC aprenden de la suposición. Solo la que supuso ve la carta."""
    jugadores = partida["jugadores"]
    nombres_pasaron = []
    for j in pasaron:
        nombres_pasaron.append(jugadores[j]["nombre"])
    nombre_refutador = None
    if refutador is not None:
        nombre_refutador = jugadores[refutador]["nombre"]

    for k in range(len(jugadores)):
        if jugadores[k]["es_pc"]:
            vista = carta if k == indice else None
            ia_registrar_suposicion(jugadores[k], jugadores[indice]["nombre"],
                                    suposicion, nombre_refutador, vista, nombres_pasaron)


def hacer_acusacion(partida, indice, acusacion):
    """Compara la acusación con el sobre secreto. Acierta = gana; falla = queda eliminado."""
    jugadores = partida["jugadores"]
    jugador = jugadores[indice]
    sobre = partida["sobre"]
    print(f"\n  {jugador['nombre']} ACUSA a {acusacion[0]}, con {acusacion[1]}, en {acusacion[2]}.")
    pausa_corta(1.0)

    if (acusacion[0] == sobre["personaje"] and acusacion[1] == sobre["arma"]
            and acusacion[2] == sobre["lugar"]):
        print("  ¡Acusación CORRECTA! El caso está resuelto.")
        partida["ganador"] = indice
        return

    jugador["activo"] = False
    print(f"  ¡Acusación INCORRECTA! {jugador['nombre']} PIERDE y queda eliminado.")
    activos = []
    for i in range(len(jugadores)):
        if jugadores[i]["activo"]:
            activos.append(i)
    if len(activos) == 1:
        partida["ganador"] = activos[0]
    else:
        print("  La partida continúa con los demás jugadores.")


def mostrar_resultado_humano(partida, refutador, carta, pasaron):
    jugadores = partida["jugadores"]
    for j in pasaron:
        print(f"  {jugadores[j]['nombre']} NO tiene ninguna de esas cartas.")
    if refutador is None:
        print("  Nadie tiene ninguna de las cartas de tu suposición.")
        print("  (Están en el sobre secreto o entre las cartas descartadas.)")
    else:
        print(f"  {jugadores[refutador]['nombre']} tiene una carta y te la muestra:  >>> {carta} <<<")


def turno_humano(partida, indice):
    jugador = partida["jugadores"][indice]
    print(f"\n>>> Turno de {jugador['nombre']} <<<")

    while True:
        opcion = menu_acciones_turno()

        if opcion == 3:  # Ver hoja (no gasta el turno)
            mostrar_hoja(jugador["hoja"], "HOJA DE " + jugador["nombre"].upper())
            if confirmar("¿Quieres editarla?"):
                editar_hoja(jugador["hoja"])
            continue

        if opcion == 1:  # Suposición
            suposicion = pedir_combinacion("suposición")
            refutador, carta, pasaron = resolver_suposicion(partida["jugadores"], indice, suposicion)
            print()
            mostrar_resultado_humano(partida, refutador, carta, pasaron)
            notificar_pcs(partida, indice, suposicion, refutador, carta, pasaron)
            if menu_post_suposicion() == 1:
                editar_hoja(jugador["hoja"])
            return

        # Acusación
        acusacion = pedir_combinacion("acusación")
        if confirmar("Si fallas pierdes la partida. ¿Seguro que quieres acusar?"):
            hacer_acusacion(partida, indice, acusacion)
            return


def turno_pc(partida, indice):
    jugadores = partida["jugadores"]
    pc = jugadores[indice]
    print(f"\n>>> Turno de {pc['nombre']} <<<")
    print("  Está pensando...")
    pausa_corta(1.5)

    accion, combinacion = ia_decidir(pc, len(partida["descartadas"]))

    if accion == "acusar":
        hacer_acusacion(partida, indice, combinacion)
    else:
        print(f"  {pc['nombre']} supone: {combinacion[0]}, con {combinacion[1]}, en {combinacion[2]}.")
        refutador, carta, pasaron = resolver_suposicion(jugadores, indice, combinacion)
        for j in pasaron:
            print(f"  {jugadores[j]['nombre']} no pudo refutar.")
        if refutador is None:
            print("  Nadie pudo refutar la suposición.")
        else:
            print(f"  {jugadores[refutador]['nombre']} refutó mostrando una carta en secreto.")
            # Con un solo humano en pantalla es seguro decirle qué carta mostró.
            if not jugadores[refutador]["es_pc"] and partida["num_humanos"] == 1:
                print(f"  (Mostraste: {carta})")
        notificar_pcs(partida, indice, combinacion, refutador, carta, pasaron)
    pausa()
