import logica
def main():
    juego = logica.inicializar_juego()
    while True:
        logica.mostrar_juego(juego)
        if logica.juego_ganado(juego):
            print("Felicidades! Sos lo mas")
            return
        if logica.juego_perdido(juego):
            print("Lola, volvé a intentar")
            return
        dir = logica.pedir_direccion(juego)
        nuevo_juego = logica.actualizar_juego(juego, dir)
        if nuevo_juego != juego:
            juego = logica.insertar_nuevo_random(nuevo_juego)

main()