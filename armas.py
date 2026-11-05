# armas.py
# Datos de las 7 armas encontradas en la mansión.

arma_1 = {
    "nombre": "Espada",
    "tipo": "arma blanca",
    "caracteristica": "arma larga y afilada, perfecta para ataques rápidos"
}
arma_2 = {
    "nombre": "C4",
    "tipo": "arma de fuego",
    "caracteristica": "arma explosiva, ideal para destruir obstáculos"
}
arma_3 = {
    "nombre": "Soga con púas",
    "tipo": "arma de agarre",
    "caracteristica": "una soga resistente con picos, perfecta para asfixiar a los enemigos"
}
arma_4 = {
    "nombre": "Serpiente cascabel",
    "tipo": "arma venenosa",
    "caracteristica": "un animal leal y peligroso, capaz de inyectar veneno mortal a sus enemigos"
}
arma_5 = {
    "nombre": "Maza",
    "tipo": "arma contundente",
    "caracteristica": "un arma pesada y poderosa, capaz de causar daño significativo a sus enemigos"
}
arma_6 = {
    "nombre": "Lanza",
    "tipo": "arma blanca",
    "caracteristica": "un arma larga y afilada, ideal para atacar a distancia y mantener a los enemigos a raya"
}
arma_7 = {
    "nombre": "Ácido",
    "tipo": "arma química",
    "caracteristica": "un líquido corrosivo que puede destruir materiales y causar daño a los enemigos"
}

ARMAS = [arma_1, arma_2, arma_3, arma_4, arma_5, arma_6, arma_7]


def nombres_armas():
    nombres = []
    for arma in ARMAS:
        nombres.append(arma["nombre"])
    return nombres


def descripcion_arma(nombre):
    for arma in ARMAS:
        if arma["nombre"] == nombre:
            return arma["caracteristica"]
    return ""
