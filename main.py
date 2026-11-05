# main.py
# Punto de entrada del juego.  Ejecutar con:  python main.py
from menus import menu_principal, menu_fin_partida
from juego import configurar_modo, jugar_partida


def main():
    while True:
        opcion = menu_principal()
        if opcion == 4:
            print("\n  Gracias por jugar. ¡Hasta pronto, detective!\n")
            break

        config = configurar_modo(opcion)
        jugando = True
        while jugando:
            jugar_partida(config)
            if menu_fin_partida() == 2:  # 1 = reintentar, 2 = menú principal
                jugando = False


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  Juego interrumpido. ¡Hasta pronto!\n")
