# utilidades.py
# Funciones de apoyo: limpiar pantalla, pausas y lectura segura de datos.
import os
import time


def limpiar_pantalla():
    """Limpia la terminal (Windows usa 'cls', el resto 'clear')."""
    os.system("cls" if os.name == "nt" else "clear")


def pausa(mensaje="  Presiona Enter para continuar..."):
    input(mensaje)


def pausa_corta(segundos=1.0):
    """Pequeña espera para que la PC 'piense' y se pueda leer lo que hace."""
    time.sleep(segundos)


def leer_opcion(mensaje, minimo, maximo):
    """Pide un número entero entre minimo y maximo. Repite hasta que sea válido."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo <= valor <= maximo:
                return valor
            print(f"  Opción inválida. Escribe un número entre {minimo} y {maximo}.")
        except ValueError:
            print("  Entrada inválida. Debes escribir un número.")


def elegir_de_lista(titulo, opciones):
    """Muestra una lista numerada. El usuario puede elegir el número
    o escribir el nombre. Devuelve el texto de la opción elegida."""
    print(titulo)
    for i in range(len(opciones)):
        print(f"   {i + 1}. {opciones[i]}")
    while True:
        texto = input("   Elige el número o escribe el nombre: ").strip()
        try:
            numero = int(texto)
            if 1 <= numero <= len(opciones):
                return opciones[numero - 1]
            print("   Número fuera de rango.")
        except ValueError:
            for opcion in opciones:
                if opcion.lower() == texto.lower():
                    return opcion
            print("   No reconozco esa opción, intenta de nuevo.")


def confirmar(mensaje):
    """Pregunta sí/no. Devuelve True o False."""
    while True:
        respuesta = input(f"  {mensaje} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("  Responde con 's' o 'n'.")
