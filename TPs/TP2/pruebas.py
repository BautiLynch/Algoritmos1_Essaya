import gamelib
import png

PALTEA_ORIGINAL = [[0,0,0],[255,255,255],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255],[255,0,255]]

def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    imagen = []
    for _ in range(alto):
        aux = []
        for _ in range(ancho):
            aux2 = []
            for k in range(3):
                aux2.append(255)
            aux.append(aux2)
        imagen.append(aux)  
    #print(imagen) #para pruebas
    return imagen

def nombre_de_color(color):
    if color == PALTEA_ORIGINAL[2]:
        return "Rojo"
    elif color == PALTEA_ORIGINAL[0]:    
        return "Negro"
    elif color == PALTEA_ORIGINAL[3]:
        return "Verde"
    elif color == PALTEA_ORIGINAL[1]:
        return "Blanco"
    elif color == PALTEA_ORIGINAL[4]:
        return "Azul"
    elif color == PALTEA_ORIGINAL[5]:
        return "Amarillo"
    elif color == PALTEA_ORIGINAL[6]:
        return "Cyan"
    elif color == PALTEA_ORIGINAL[7]:
        return "Magenta"
    else:
        return "Nuevo color"
        
def eleccion_color(tecla,color_anterior=False):
    if tecla == "a":
            while True:
                nuevo_color = gamelib.input("Añada el color a agregar en formato hexadecimal: ")
                if len(nuevo_color[1:]) != 6:
                    gamelib.say("El formato de color no es valido")
                    continue
                for c in nuevo_color[1:]:
                    if not str(c).isdigit() and c not in ["f","F","c","C"]:
                        gamelib.say("El formato de color no es valido")
                        continue
                break
            lista_color = list(nuevo_color[1:])
            nuevo = []
            for i in range(0,len(lista_color),2):
                nuevo.append(int(lista_color[i]+lista_color[i+1], 16))
            return nuevo
    if tecla == "r":
        return PALTEA_ORIGINAL[2]
    if tecla == "n":
        return PALTEA_ORIGINAL[0]
    if tecla == "v":
        return PALTEA_ORIGINAL[3]
    if tecla == "w":
        return PALTEA_ORIGINAL[1]
    if tecla == "b":
        return PALTEA_ORIGINAL[4]
    if tecla == "y":
        return PALTEA_ORIGINAL[5]
    if tecla == "c":
        return PALTEA_ORIGINAL[6]
    if tecla == "m":
        return PALTEA_ORIGINAL[7]
    else:
        return color_anterior
    


def actualizar_paint(paint,x,y,w,h,color):
    max_x, max_y = w*20+10, h*20+10
    celda_actual1, celda_actual2 = 0,0
    if 10<x<max_x and 10<y<max_y:
        for i in range(10,max_y,20):
            for j in range(10,max_x,20):
                if j<x<j+20 and i<y<i+20:
                    paint[celda_actual1][celda_actual2] = color
                celda_actual2 +=1
            celda_actual2 = 0
            celda_actual1 += 1

def paint_mostrar(paint,w,nombre_color):
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
    gamelib.draw_text("Rojo = Presionar r",100,w*20+20,fill="#FF0000")
    gamelib.draw_text("Negro = Presionar n",100,w*20+40,fill="#FFFFFF")
    gamelib.draw_text("Azul = Presionar b",100,w*20+60,fill="#0000FF")
    gamelib.draw_text("Verde = Presionar v",100,w*20+80,fill="#00FF00")
    gamelib.draw_text("Amarillo = Presionar y",100,w*20+100,fill="#FFFF00")
    gamelib.draw_text("Cyan = Presionar c",100,w*20+120,fill="#00FFFF")
    gamelib.draw_text("Magenta = Presionar m",100,w*20+140,fill="#FF00FF")
    gamelib.draw_text("Blanco = Presionar w",100,w*20+160,fill="#FFFFFF")
    gamelib.draw_text("Agregar color = Presionar a",100,w*20+180)
    gamelib.draw_rectangle(200,w*20+20,300,w*20+40)
    gamelib.draw_text("Guardar PPM",250,w*20+30,fill="#000000")
    gamelib.draw_rectangle(200,w*20+40,300,w*20+60)
    gamelib.draw_text("Guardar PNG",250,w*20+50,fill="#000000")
    gamelib.draw_rectangle(200,w*20+60,300,w*20+80)
    gamelib.draw_text("Cargar PPM",250,w*20+70,fill="#000000")
    gamelib.draw_text(f"Color Actual: {nombre_color}",300,w*20+100)
    gamelib.draw_end()

def guardar_ppm(paint,w,h):
    try:
        while True:
            nombre_archivo = gamelib.input("Ingrese nombre del archivo con .ppm: ")
            comprobar_nombre = nombre_archivo.split(".")
            if len(comprobar_nombre) != 2 or comprobar_nombre[1] != "ppm":
                gamelib.say("Nombre invalido")
                continue
            break
        with open(nombre_archivo,"w") as guardar:
            guardar.write("P3\n")
            guardar.write(f"{w} {h}\n")
            guardar.write(f"255\n")
            contador = 1
            for i in range(len(paint)):
                for j in range(len(paint[i])):
                    for color in paint[i][j]:
                        if contador == w*h*3:
                            guardar.writelines(f"{color}")
                        else:
                            guardar.writelines(f"{color} ")
                            contador += 1
                guardar.write("\n")
    except:
        gamelib.say("No se guardo el archivo")
        Exception("Cancelar Guardado")

def guardar_png(paint,paleta):
    try:
        while True:
            nombre_archivo = gamelib.input("Ingerese el nombre del archivo con .png: ")
            comprobar_nombre = nombre_archivo.split(".")
            if len(comprobar_nombre) != 2 or comprobar_nombre[1] != "png":
                gamelib.say("Nombre invalido")
                continue
            break
        imagen = []
        for i in range(len(paint)):
            aux = []
            for j in range(len(paint[i])):
                for k in range(len(paleta)):
                    if paint[i][j] == paleta[k]:
                        aux.append(k)
            imagen.append(aux)
        png.escribir(nombre_archivo,paleta,imagen)
    except:
        gamelib.say("No se guardo el archivo")
        Exception("Cancelar Guardado")
def cargar_ppm():
    try:
        while True:
                nombre_archivo = gamelib.input("Ingerese el nombre del archivo: ")
                comprobar_nombre = nombre_archivo.split(".")
                if len(comprobar_nombre) != 2 or comprobar_nombre[1] != "ppm":
                    gamelib.say("Nombre invalido")
                    continue
                break
        with open(nombre_archivo,"r") as imagen:
            imagen_nueva = ""
            contador = 0
            for linea in imagen:
                imagen_nueva += linea.rstrip("\n")
                if contador < 3:
                    imagen_nueva += " "
                    contador += 1
            lista_elementos = imagen_nueva.split(" ")
            width_nuevo,height_nuevo = int(lista_elementos[1]),int(lista_elementos[2])
            nuevo_paint = []
            aux=[]
            for i in range(4,len(lista_elementos),3):
                aux.append(lista_elementos[i:i+3])
            for i in range(0,len(aux),height_nuevo):
                nuevo_paint.append(aux[i:i+height_nuevo])
            return width_nuevo,height_nuevo,nuevo_paint
    except FileNotFoundError:
        gamelib.say("File not found error: Archivo no encontrado, revise el nombre")
        Exception("Archivo no encontrado")


def main():
    width = 10
    height = 10
    gamelib.title("AlgoPaint")
    gamelib.resize(420, 600)
    color = eleccion_color("n")
    paint = paint_nuevo(width, height)
    paleta = PALTEA_ORIGINAL
    while gamelib.is_alive():
        nombre_color = nombre_de_color(color)
        paint_mostrar(paint,width,nombre_color)
        ev = gamelib.wait()
        if not ev:
            break
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            actualizar_paint(paint,ev.x,ev.y,width,height,color)
            if 200 < ev.x <300 and width*20+20 < ev.y < width*20+40:
                guardar_ppm(paint,width,height)
            if 200 < ev.x <300 and width*20+40 < ev.y < width*20+60:
                guardar_png(paint,paleta)
            if 200 < ev.x <300 and width*20+60 < ev.y < width*20+80:
                try:
                    width,height,paint = cargar_ppm()
                except:
                    gamelib.say("No se guardo el archivo")
                    Exception("Cancelar Guardado")
        elif ev.type == gamelib.EventType.KeyPress:
            try:
                color = eleccion_color(ev.key,color)
                paleta.append(color)
            except:
                gamelib.say("No se añadio un color")
                Exception("Cancelar añadido")

            
gamelib.init(main)
