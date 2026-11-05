# personajes.py
# Datos de los 6 personajes (invitad@s a la reunión en la mansión Sánchez).

personaje_1 = {
    "nombre": "Yusepe Nuñes",
    "animal": "escorpion",
    "caracteristicas": "hombre delgado, con ojos verdes y un aura misteriosa"
}
personaje_2 = {
    "nombre": "Rias Gremory",
    "animal": "fénix",
    "caracteristicas": "una hermosa mujer de cabello rojizo, contextura delgada, orgullosa, ambiciosa y poderosa"
}
personaje_3 = {
    "nombre": "Armando Mendosa",
    "animal": "loro",
    "caracteristicas": "un hombre de contextura media, con cabello castaño y ojos marrones, muy hablador y carismático"
}
personaje_4 = {
    "nombre": "Rafel Mendez",
    "animal": "águila",
    "caracteristicas": "un hombre de contextura fuerte, con cabello negro y ojos azules, muy valiente y protector"
}
personaje_5 = {
    "nombre": "Karen Sarmiento",
    "animal": "zorro",
    "caracteristicas": "una mujer de contextura delgada, con cabello rubio y ojos verdes, muy inteligente y astuta"
}
personaje_6 = {
    "nombre": "Diego Ramírez",
    "animal": "lobo",
    "caracteristicas": "un hombre de contextura fuerte, con cabello negro y ojos amarillos, muy leal y protector"
}

PERSONAJES = [personaje_1, personaje_2, personaje_3,
              personaje_4, personaje_5, personaje_6]


def nombres_personajes():
    """Devuelve una lista NUEVA con los nombres de los personajes."""
    nombres = []
    for personaje in PERSONAJES:
        nombres.append(personaje["nombre"])
    return nombres


def descripcion_personaje(nombre):
    for personaje in PERSONAJES:
        if personaje["nombre"] == nombre:
            return personaje["caracteristicas"]
    return ""
