import gamelib
import persistencia
import tablero
from pila import Pila
PALETA_ORIGINAL = ((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))


def main():
    width = 20
    height = 20
    gamelib.title("AlgoPaint")
    gamelib.resize(420, 600)
    color = tablero.eleccion_color("n",PALETA_ORIGINAL)
    paint = tablero.paint_nuevo(width, height)
    estados_anteriores = Pila()
    estados_anteriores.apilar(tablero.paint_nuevo(width, height))
    estados_siguientes = Pila()
    paleta = list(PALETA_ORIGINAL)
    estado_balde = False
    while gamelib.is_alive():
        nombre_color = tablero.nombre_de_color(color,PALETA_ORIGINAL)
        tablero.paint_mostrar(paint,height,nombre_color,estado_balde)
        ev = gamelib.wait()
        if not ev:
            break
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1: 
            if 10 < ev.x < width*20+20 and 10 < ev.y < height*20+20:
                tablero.actualizar_paint(paint,ev.x,ev.y,width,height,color,estado_balde)
                estado_balde = False
                while not estados_siguientes.esta_vacia():
                    estados_siguientes.desapilar()
                estados_anteriores.apilar(tablero.copiar_tablero(paint))
            if 200 < ev.x <300 and height*20+20 < ev.y < height*20+40:
                persistencia.guardar_ppm(paint,width,height)
            if 200 < ev.x <300 and height*20+40 < ev.y < height*20+60:
                persistencia.guardar_png(paint,paleta)
            if 200 < ev.x <300 and height*20+60 < ev.y < height*20+80:
                width,height,paint = persistencia.cargar_ppm(width,height,paint)

        elif ev.type == gamelib.EventType.KeyPress:
            color = tablero.eleccion_color(ev.key,PALETA_ORIGINAL,color)
            if ev.key == "z":
                paint = tablero.deshacer(estados_anteriores,estados_siguientes,tablero.copiar_tablero(paint))
            if ev.key == "o":
                paint = tablero.rehacer(estados_anteriores,estados_siguientes,tablero.copiar_tablero(paint))
            if ev.key == "p":
                estado_balde = True
            paleta.append(color)
      
gamelib.init(main)
