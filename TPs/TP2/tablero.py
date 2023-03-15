import gamelib
from pila import Pila
def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    imagen = []
    aux_blanco = [255,255,255]
    for _ in range(alto):
        aux = []
        for _ in range(ancho):
            aux.append(aux_blanco)
        imagen.append(aux)  
    return imagen

def nombre_de_color(color_actual,paleta):
    dicc = {
        paleta[0]:"Negro",
        paleta[1]:"Blanco",
        paleta[2]:"Rojo",
        paleta[3]:"Verde",
        paleta[4]:"Azul",
        paleta[5]:"Amarillo",
        paleta[6]:"Cyan",
        paleta[7]:"Magenta"
    }
    return dicc.get(color_actual,"Nuevo Color")
        
def eleccion_color(tecla,paleta,color_anterior=False):
    dicc = {
        "n":paleta[0],
        "w":paleta[1],
        "r":paleta[2],
        "v":paleta[3],
        "b":paleta[4],
        "y":paleta[5],
        "c":paleta[6],
        "m":paleta[7]
    }
    if tecla == "a":
            while True:
                nuevo_color = gamelib.input("Añada el color a agregar en formato hexadecimal: ")
                if len(nuevo_color[1:]) != 6:
                    gamelib.say("El formato de color no es valido")
                    continue
                for c in nuevo_color[1:]:
                    if not str(c).isdigit() and c not in ["f","F","c","C"]:
                        gamelib.say("El formato de color no es valido")
                        break
                break
            lista_color = list(nuevo_color[1:])
            nuevo = []
            for i in range(0,len(lista_color),2):
                nuevo.append(int(lista_color[i]+lista_color[i+1], 16))
            return tuple(nuevo)
    return dicc.get(tecla,color_anterior)
    

def actualizar_paint(paint,x,y,w,h,color,estado_balde):
    max_x, max_y = w*20+10, h*20+10
    celda_actual1, celda_actual2 = 0,0
    if 10<x<max_x and 10<y<max_y:
        for i in range(10,max_y,20):
            for j in range(10,max_x,20):
                if j<x<j+20 and i<y<i+20:
                    if estado_balde == True:
                        balde(paint,[celda_actual1,celda_actual2],color)
                    paint[celda_actual1][celda_actual2] = color
                celda_actual2 +=1
            celda_actual2 = 0
            celda_actual1 += 1

def paint_mostrar(paint,h,nombre_color,balde):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()

    coordenadas_x,coordenadas_y=10,10      
    for i in range(len(paint)):
        for j in range(len(paint[0])):
            color2 = "#"
            for k in range(len(paint[0][0])):
                color2 += f'{int(paint[i][j][k]):02x}' 
            gamelib.draw_rectangle(coordenadas_x,coordenadas_y,coordenadas_x+20,coordenadas_y+20,fill=color2)
            coordenadas_x += 20
        coordenadas_x = 10
        coordenadas_y += 20
    gamelib.draw_text("Rojo = Presionar r",100,h*20+20,fill="#FF0000")
    gamelib.draw_text("Negro = Presionar n",100,h*20+40,fill="#FFFFFF")
    gamelib.draw_text("Azul = Presionar b",100,h*20+60,fill="#0000FF")
    gamelib.draw_text("Verde = Presionar v",100,h*20+80,fill="#00FF00")
    gamelib.draw_text("Amarillo = Presionar y",100,h*20+100,fill="#FFFF00")
    gamelib.draw_text("Cyan = Presionar c",100,h*20+120,fill="#00FFFF")
    gamelib.draw_text("Magenta = Presionar m",100,h*20+140,fill="#FF00FF")
    gamelib.draw_text("Blanco = Presionar w",100,h*20+160,fill="#FFFFFF")
    gamelib.draw_text("Agregar color = Presionar a",100,h*20+180)
    gamelib.draw_rectangle(200,h*20+20,300,h*20+40)
    gamelib.draw_text("Guardar PPM",250,h*20+30,fill="#000000")
    gamelib.draw_rectangle(200,h*20+40,300,h*20+60)
    gamelib.draw_text("Guardar PNG",250,h*20+50,fill="#000000")
    gamelib.draw_rectangle(200,h*20+60,300,h*20+80)
    gamelib.draw_text("Cargar PPM",250,h*20+70,fill="#000000")
    gamelib.draw_text(f"Color Actual: {nombre_color}",300,h*20+100)
    gamelib.draw_text(f"Deshacer: Presionar z",300,h*20+120)
    gamelib.draw_text(f"Rehacer: Presionar o",300,h*20+140)
    if not balde:
        gamelib.draw_text(f"Balde: Presionar p----Desactivado",300,h*20+160)

    else:
        gamelib.draw_text(f"Balde: Presionar p----Activado",300,h*20+160)
    gamelib.draw_end()

def copiar_tablero(tablero):
    nuevo_tablero = []
    for i in range(len(tablero)):
        aux = []
        for j in range(len(tablero[i])):
            aux2 = []
            for k in range(len(tablero[i][j])):
                aux2.append(tablero[i][j][k])
            aux.append(aux2)
        nuevo_tablero.append(aux)
    return nuevo_tablero

def deshacer(pila_anterior,pila_siguiente,paint):
    if not pila_anterior.esta_vacia():
        pila_siguiente.apilar(pila_anterior.desapilar())
        if not pila_anterior.esta_vacia():
            return copiar_tablero(pila_anterior.ver_tope())
    return paint

def rehacer(pila_anterior,pila_siguiente,paint):
    if not pila_siguiente.esta_vacia():
        pila_anterior.apilar(pila_siguiente.desapilar())
        return copiar_tablero(pila_anterior.ver_tope())
    return paint

def balde(paint,anterior,color_actual):
    i,j = anterior
    return _balde(paint,i,j,paint[i][j],color_actual)

def _balde(paint,i,j,color_anterior,color_actual):
    if i<0 or len(paint)-1<i or j<0 or len(paint[i])-1<j:
        return
    if paint[i][j] != color_anterior:
        return
    paint[i][j] = color_actual
    _balde(paint,i,j-1,color_anterior,color_actual) 
    _balde(paint,i-1,j,color_anterior,color_actual) 
    _balde(paint,i,j+1,color_anterior,color_actual) 
    _balde(paint,i+1,j,color_anterior,color_actual) 
    