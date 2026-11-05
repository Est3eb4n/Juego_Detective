# lugares_mansion.py
# Datos de los 9 lugares de la mansión.

lugar_1 = {
    "lugar": "Lobby",
    "ubicacion": "segundo piso de la mansión",
    "caracteristicas": "un lugar amplio y elegante con un gran ventanal que permite la entrada de la luz natural."
}
lugar_2 = {
    "lugar": "Sala de estar",
    "ubicacion": "primer piso de la mansión",
    "caracteristicas": "un espacio acogedor con muebles de madera y una chimenea central."
}
lugar_3 = {
    "lugar": "Altillo",
    "ubicacion": "espacio entre el techo del último piso y el techo de la mansión",
    "caracteristicas": "un lugar tranquilo y oscuro con algunas cajas llenas de polvo."
}
lugar_4 = {
    "lugar": "Salón de banquetes",
    "ubicacion": "primer piso de la mansión",
    "caracteristicas": "un espacio amplio con una mesa grande y sillas de madera."
}
lugar_5 = {
    "lugar": "Sala de música",
    "ubicacion": "segundo piso de la mansión",
    "caracteristicas": "un lugar acogedor con un piano y una colección de instrumentos musicales."
}
lugar_6 = {
    "lugar": "Cuarto de descanso",
    "ubicacion": "segundo piso de la mansión",
    "caracteristicas": "un espacio relajante con una cama grande y muebles sencillos."
}
lugar_7 = {
    "lugar": "Patio trasero",
    "ubicacion": "parte trasera de la mansión",
    "caracteristicas": "un espacio abierto con un laberinto de pino y una mesa para comer al aire libre."
}
lugar_8 = {
    "lugar": "Jardín",
    "ubicacion": "parte delantera de la mansión",
    "caracteristicas": "un espacio verde con árboles y flores, ideal para relajarse al aire libre."
}
lugar_9 = {
    "lugar": "Sala de juegos",
    "ubicacion": "primer piso de la mansión",
    "caracteristicas": "un espacio divertido con juegos de mesa y juguetes para todas las edades."
}

LUGARES = [lugar_1, lugar_2, lugar_3, lugar_4, lugar_5,
           lugar_6, lugar_7, lugar_8, lugar_9]


def nombres_lugares():
    nombres = []
    for lugar in LUGARES:
        nombres.append(lugar["lugar"])
    return nombres


def descripcion_lugar(nombre):
    for lugar in LUGARES:
        if lugar["lugar"] == nombre:
            return lugar["ubicacion"] + ": " + lugar["caracteristicas"]
    return ""
