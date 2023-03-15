from math import ulp
import random
FILAS_TABLERO = 4
COLUMNAS_TABLERO = 4
TECLAS = ("w","a","s","d")
NUMERO_FINAL = 2048

def inicializar_juego():
    "crea el tablero y asigna un numero random en una posicion random"
    tablero_inicial = []
    for f in range(FILAS_TABLERO):
        aux = []
        for c in range(COLUMNAS_TABLERO):
            aux.append(0)
        tablero_inicial.append(aux)
    return insertar_nuevo_random(tablero_inicial)

def mostrar_juego(tablero_actual):
    "imprime el tablero en la consola"
    for l in tablero_actual:
        print(l)

def juego_ganado(tablero_actual):
    "devuelve True solo si algun numero es igual al numero deseado"
    for f in range(len(tablero_actual)):
        for c in range(len(tablero_actual[0])):
            numero = tablero_actual[f][c]
            if numero == NUMERO_FINAL:
                return True
    return False

def juego_perdido(tablero):
    "devuelve true solo si los 4 movimientos posibles resultan en el mismo tablero"
    tableros_iguales = 0
    for e in TECLAS:
        if tablero == actualizar_juego(tablero,e):
            tableros_iguales += 1
    if tableros_iguales == 4:
        return True
    return False

def pedir_direccion(tablero_actual):
    "pide al usuario la direccion para mover"
    nueva_dir = input(f"Ingrese la nueva dirección {TECLAS} : ")
    while not (nueva_dir == TECLAS[0] or nueva_dir == TECLAS[1] or nueva_dir == TECLAS[2] or nueva_dir == TECLAS[3]):
        nueva_dir = input(f"Tecla invalida, ingrese una nueva dirección {TECLAS} : ")
    return nueva_dir

def llevar_num_para_izquierda(i_fila_actual):
    "hace que todos los numeros de una fila sean llevados para la izquierda"
    fila_nueva = []
    cantidad_ceros = 0
    for i in range(len(i_fila_actual)):
        if i_fila_actual[i] != 0:
            fila_nueva.append(i_fila_actual[i])
        else:
            cantidad_ceros += 1
    while cantidad_ceros > 0:
        fila_nueva.append(0)
        cantidad_ceros -= 1
    return fila_nueva

def sumar_num_iguales(fila_actual):
    "si dos numeros son iguales multiplica el numero de la izquierda por dos y el de la derecha lo tranforma en 0"
    for i in range(len(fila_actual)-1):
        if fila_actual[i]==fila_actual[i+1]:
            fila_actual[i] *= 2
            fila_actual[i+1] = 0
    llevar_num_para_izquierda(fila_actual)
    return fila_actual

def trasponer_tablero(tablero_actual):
    "Traspone al tablero"
    tablero_transpuesto = tablero_actual
    for f in range(len(tablero_transpuesto)):
        for c in range(len(tablero_transpuesto[0])):
            if f < c:
                tablero_transpuesto[f][c], tablero_transpuesto[c][f] = tablero_transpuesto[c][f], tablero_transpuesto[f][c]
    return tablero_transpuesto

def actualizar_tablero_izquierda(tablero_actual):
    "modifica el tablero asumiendo que la direccion deseada es izquierda"
    nuevo_tablero = []
    for f in range(len(tablero_actual)):
        fila_actual = []
        for c in range(len(tablero_actual[f])):
            fila_actual.append(tablero_actual[f][c])
        nueva_fila = sumar_num_iguales(llevar_num_para_izquierda(fila_actual))
        nuevo_tablero.append(nueva_fila)
    return nuevo_tablero

def dar_filas_vuelta(tablero_actual):
    "Da vuelta todas las filas del tablero"
    tablero_nuevo = []
    for f in range(len(tablero_actual)):
        tablero_nuevo.append(list(reversed(tablero_actual[f])))
    return tablero_nuevo

def actualizar_juego(tablero_actual,direccion):
    "modifica el tablero segun la direccion que se le pregunte"
    nuevo_tablero = tablero_actual
    if direccion == TECLAS[0]:
        nuevo_tablero = trasponer_tablero(nuevo_tablero)
        nuevo_tablero = actualizar_tablero_izquierda(nuevo_tablero)
        nuevo_tablero = trasponer_tablero(nuevo_tablero)


    if direccion == TECLAS[1]:
        nuevo_tablero = actualizar_tablero_izquierda(nuevo_tablero)
         
    if direccion == TECLAS[2]:
        nuevo_tablero = trasponer_tablero(nuevo_tablero)
        nuevo_tablero = dar_filas_vuelta(nuevo_tablero)
        nuevo_tablero = actualizar_tablero_izquierda(nuevo_tablero)
        nuevo_tablero = dar_filas_vuelta(nuevo_tablero)
        nuevo_tablero = trasponer_tablero(nuevo_tablero)

    if direccion == TECLAS[3]:
        nuevo_tablero = dar_filas_vuelta(nuevo_tablero)
        nuevo_tablero = actualizar_tablero_izquierda(nuevo_tablero)
        nuevo_tablero = dar_filas_vuelta(nuevo_tablero)
    return nuevo_tablero

def insertar_nuevo_random(tablero_actual):
    "Agrega un 2 o 4 aleatoriamente en una posicion aleatoria que sea = 0"
    tablero_num_random = tablero_actual
    centinela = 0
    while centinela != 1:
        fila_random = random.randint(0,FILAS_TABLERO - 1)
        columna_random = random.randint(0,COLUMNAS_TABLERO - 1)
        nuevo_num = tablero_num_random[fila_random][columna_random]
        if nuevo_num == 0:
            tablero_num_random[fila_random][columna_random] += random.randrange(2,5,2)
            centinela += 1 
            return tablero_num_random

