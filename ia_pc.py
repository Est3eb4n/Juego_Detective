# ia_pc.py
# Inteligencia del jugador automático (PC). Funciona por deducción lógica:
#   - Su "Hoja del Detective" marca con X las cartas que sabe que NO están en el sobre.
#   - Guarda "pistas": cuando alguien refuta sin mostrarle la carta, sabe que esa
#     persona tiene AL MENOS UNA de las 3 cartas. Si descarta 2, la tercera es suya.
#   - Acusa solo cuando ya no puede descubrir nada más (o tiene la solución).
import random
from cartas import todas_las_cartas, categoria_de


def crear_memoria():
    return {
        "pistas": [],       # lista de [nombre_jugador, [carta1, carta2, carta3]]
        "no_posee": {},     # nombre_jugador -> cartas que sabemos que NO tiene
        "posee": {},        # carta -> nombre del jugador que sabemos que la tiene
        "historial": [],    # cartas ya usadas en sus suposiciones
        "turnos": 0,
        "sin_info": 0,      # suposiciones seguidas que no aportaron nada
    }


def marcar_descartada(pc, carta, dueno):
    """Anota X en la hoja de la PC: esa carta la tiene otro jugador."""
    if pc["hoja"][carta] != "M":
        pc["hoja"][carta] = "X"
    pc["memoria"]["posee"][carta] = dueno


def ia_registrar_suposicion(pc, quien, suposicion, refutador, carta_vista, pasaron):
    """La PC aprende de una suposición (suya o de otro jugador).
    quien: nombre de quien supuso | refutador: nombre de quien refutó (o None)
    carta_vista: carta mostrada (solo si la PC fue quien supuso) | pasaron: nombres que no pudieron refutar"""
    mem = pc["memoria"]

    # Quienes no pudieron refutar NO tienen ninguna de las 3 cartas.
    for nombre in pasaron:
        if nombre == pc["nombre"]:
            continue
        if nombre not in mem["no_posee"]:
            mem["no_posee"][nombre] = []
        for carta in suposicion:
            if carta not in mem["no_posee"][nombre]:
                mem["no_posee"][nombre].append(carta)

    if refutador is None:
        if quien == pc["nombre"]:
            mem["sin_info"] += 1
    elif carta_vista is not None:
        # La PC supuso y vio la carta.
        nueva = carta_vista not in mem["posee"] and pc["hoja"][carta_vista] != "M"
        marcar_descartada(pc, carta_vista, refutador)
        if nueva:
            mem["sin_info"] = 0
        else:
            mem["sin_info"] += 1
    elif refutador != pc["nombre"]:
        # Otro jugador refutó a un tercero: tiene al menos una de las 3 cartas.
        mem["pistas"].append([refutador, list(suposicion)])

    ia_deducir(pc)


def ia_deducir(pc):
    """Revisa las pistas hasta que no se pueda deducir nada más."""
    mem = pc["memoria"]
    cambio = True
    while cambio:
        cambio = False
        for pista in mem["pistas"]:
            jugador = pista[0]
            posibles = []
            for carta in pista[1]:
                if carta in pc["mano"]:
                    continue  # yo la tengo, así que ese jugador no
                if carta in mem["no_posee"].get(jugador, []):
                    continue  # ya sé que no la tiene
                if carta in mem["posee"] and mem["posee"][carta] != jugador:
                    continue  # otro jugador la tiene
                posibles.append(carta)
            if len(posibles) == 1 and posibles[0] not in mem["posee"]:
                marcar_descartada(pc, posibles[0], jugador)
                cambio = True


def ia_candidatos(pc):
    """Cartas que aún podrían estar en el sobre, separadas por categoría."""
    candidatos = {"personaje": [], "arma": [], "lugar": []}
    for carta in todas_las_cartas():
        if pc["hoja"][carta] not in ("X", "M"):
            candidatos[categoria_de(carta)].append(carta)
    return candidatos


def elegir_menos_usada(lista, historial):
    """De la lista, elige al azar entre las cartas menos usadas en suposiciones previas."""
    mejores = []
    minimo = None
    for carta in lista:
        veces = historial.count(carta)
        if minimo is None or veces < minimo:
            minimo = veces
            mejores = [carta]
        elif veces == minimo:
            mejores.append(carta)
    return random.choice(mejores)


def ia_decidir(pc, num_descartadas):
    """Decide si acusar o suponer. Devuelve ("acusar"/"suponer", [personaje, arma, lugar])."""
    mem = pc["memoria"]
    mem["turnos"] += 1
    ia_deducir(pc)

    cand = ia_candidatos(pc)
    combinaciones = len(cand["personaje"]) * len(cand["arma"]) * len(cand["lugar"])
    total_candidatas = len(cand["personaje"]) + len(cand["arma"]) + len(cand["lugar"])

    acusar = False
    if combinaciones == 1:
        acusar = True  # solo queda una solución posible
    elif total_candidatas <= 3 + num_descartadas:
        # Ya no hay más cartas por descubrir: las que quedan son el sobre + las descartadas.
        # Si hay pocas opciones acusa; si no, a veces arriesga y a veces sigue suponiendo.
        if combinaciones <= 2 or random.random() < 0.35:
            acusar = True
    elif mem["turnos"] >= 25:
        acusar = True  # seguro anti-partidas eternas

    if acusar:
        return "acusar", [random.choice(cand["personaje"]),
                          random.choice(cand["arma"]),
                          random.choice(cand["lugar"])]

    suposicion = [elegir_menos_usada(cand["personaje"], mem["historial"]),
                  elegir_menos_usada(cand["arma"], mem["historial"]),
                  elegir_menos_usada(cand["lugar"], mem["historial"])]
    for carta in suposicion:
        mem["historial"].append(carta)
    return "suponer", suposicion
