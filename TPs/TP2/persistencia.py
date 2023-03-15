import gamelib
import png
def es_archivo(tipo_archivo):
    while True:
            nombre_archivo = gamelib.input(f"Ingrese nombre del archivo con .{tipo_archivo}: ")
            comprobar_nombre = nombre_archivo.split(".")
            if len(comprobar_nombre) != 2 or comprobar_nombre[1] != tipo_archivo:
                gamelib.say("Nombre invalido")
                continue
            return nombre_archivo

def guardar_ppm(paint,w,h):
    try:
        nombre_archivo = es_archivo("ppm")
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

def guardar_png(paint,paleta):
    try:
        nombre_archivo = es_archivo("png")
        imagen = []
        nueva_paleta = []
        for i in range(len(paint)):
            aux = []
            for j in range(len(paint[i])):
                color = tuple(paint[i][j])
                if color not in nueva_paleta:
                    nueva_paleta.append(color) 
                aux.append(nueva_paleta.index(color))
            imagen.append(aux)
        png.escribir(nombre_archivo,nueva_paleta,imagen)
    except:
        gamelib.say("No se guardo el archivo")
def cargar_ppm(width,height,paint):
    try:
        nombre_archivo = es_archivo("ppm")
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
        return width,height,paint
    except:
        gamelib.say("Error inesperado, no se cargo el archivo")
        return width,height,paint
 