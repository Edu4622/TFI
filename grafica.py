
from colorama import Fore, Back, Style, init

"""
Nombre del modulo: grafica.py.
Descripcion: contiene funciones que dibujan recuadros, como encabezados y menus
Autor: egf
"""
init()

SUPIZQ = chr(0x2554)
SUPDER = chr(0x2557)
INFIZQ = chr(0x255A)
INFDER = chr(0x255D)
HORIZ  = chr(0x2550)
VERT   = chr(0x2551)
LINEA_VERT = chr(0x2502)
JUNTA_SUP = chr(0x2564)
JUNTA_INF = chr(0x2567)
JUNTA_MED = chr(0x256A)
ESPACIO = " "
SANGRIA = ESPACIO * 10
RESET = "\033[0m"
CURSIVA = "\033[3m"
CERRAR_CURSIVA = "\033[23m"
FIRMA = "by egf c205"

def encabezado(ancho=100,alto=5,titulo=""):
    
    """
    Esta funcion dibuja un recuadro con un titulo en el medio
    Parametros: 
        ancho: el ancho del rectangulo
        alto: la cantidad de lineas del rectangulo
        titulo: el titulo que se muestra en el medio del rectangulo

    Devuelve: None
    """

    
    FILASUP = SUPIZQ + HORIZ * (ancho-2) + SUPDER
    FILAINF = INFIZQ + HORIZ *(ancho-2-len(FIRMA)-2) + CURSIVA +FIRMA + CERRAR_CURSIVA + HORIZ*2 + INFDER
    FILAINTER = f"{VERT}{ESPACIO:^{ancho-2}}{VERT}"

   

    print(Fore.LIGHTBLUE_EX)

    print(FILASUP)
    #print(SUPIZQ + HORIZ * (ancho-2) + SUPDER)
    fila_titulo = (alto - 2) // 2

    for fila in range(alto-2):
        if fila == fila_titulo:
            #print(Fore.LIGHTGREEN_EX)
            print(f"{VERT}{Fore.LIGHTGREEN_EX}{titulo:^{ancho-2}}{Fore.LIGHTBLUE_EX}{VERT}")
            #print(Fore.BLUE)
        else:
            print(FILAINTER)

    #print(INFIZQ + HORIZ *(ancho-2) + INFDER)
    print(FILAINF)


#  Fin de funcion encabezado.
# ---------------------------------------------------------------------------------------
def genera_menu(opciones, titulo = "", ancho=100):

    FILASUP = SUPIZQ + HORIZ * (ancho-2) + SUPDER
    FILAINF = INFIZQ + HORIZ *(ancho-2) + INFDER
    FILAINTER = f"{VERT}{ESPACIO:^{ancho-2}}{VERT}"

    print(Fore.LIGHTBLUE_EX)

    print(FILASUP)
    print(f"{VERT}{titulo:^{ancho-2}}{VERT}")
    for indice, opcion in enumerate(opciones, start=1): 
        linea_opc = f"{indice}.- {opcion}"
        print(f"{VERT}{SANGRIA}{linea_opc}{ESPACIO*(ancho-len(linea_opc)-2-len(SANGRIA))}{VERT}")
    print(FILAINTER)
    print(FILAINF)

    # fin de funcion genera_menu
    # ----------------------------------------------------------------------------------------
    # inicio función listados

# def listados(ancho=100, lista=[]):
def listados(lista=[]):

    FILASUP = SUPIZQ + HORIZ * 6 + JUNTA_SUP + HORIZ * 22 + JUNTA_SUP + HORIZ * 28 + JUNTA_SUP + HORIZ * 12 + JUNTA_SUP + HORIZ * 12 + JUNTA_SUP + HORIZ * 13 + SUPDER
    FILAINF = INFIZQ + HORIZ * 6 + JUNTA_INF + HORIZ * 22 + JUNTA_INF + HORIZ * 28 + JUNTA_INF + HORIZ * 12 + JUNTA_INF + HORIZ * 12 + JUNTA_INF + HORIZ * 13 + INFDER
    FILAMED = VERT + HORIZ * 6 + JUNTA_MED + HORIZ * 22 + JUNTA_MED + HORIZ * 28 + JUNTA_MED + HORIZ * 12 + JUNTA_MED + HORIZ * 12 + JUNTA_MED + HORIZ * 13 + VERT
    # if not lista:
    #              print(f"{Fore.YELLOW} La lista de productos está vacia")

    print(Fore.LIGHTBLUE_EX)
    
    print(FILASUP)
    print(f"{VERT}{'Id':>5} {LINEA_VERT} {'Nombre':<20} {LINEA_VERT} {'Descripción':<26} {LINEA_VERT} {'Cantidad':>10} {LINEA_VERT} {'Precio ($)':>10} {LINEA_VERT} {'Categoría':<12}{VERT}")
    print(FILAMED)

    for producto in lista:
        id, nombre, descripcion, cantidad, precio, categoria = producto
        if len(nombre) > 19:
            nombre = nombre[:16] + "..."
        if len(descripcion) > 25:
            descripcion = (descripcion[:22]) + "..."
        precio = f"{precio:,.2f}"
        print(f"{VERT} {id:>4} {LINEA_VERT} {nombre:<20} {LINEA_VERT} {descripcion:<26} {LINEA_VERT} {cantidad:>10} {LINEA_VERT} {precio:>10} {LINEA_VERT} {categoria:<12}{VERT}")
    print(FILAINF)

def recuadro_txt(ancho=100, lista_txt=[]):

    FILASUP = SUPIZQ + HORIZ * (ancho-2) + SUPDER
    FILAINF = INFIZQ + HORIZ *(ancho-4) + CURSIVA + CERRAR_CURSIVA + HORIZ*2 + INFDER
    FILAINTER = f"{VERT}{ESPACIO:^{ancho-2}}{VERT}"

    print(FILASUP)
    print(FILAINTER)

    for linea_txt in lista_txt:
        print(f"{VERT}{SANGRIA}{linea_txt}{ESPACIO*(ancho-len(linea_txt)-2-len(SANGRIA))}{VERT}")
        print(FILAINTER)

    print(FILAINF)    

def aviso(txt=[]):
    print(Fore.LIGHTGREEN_EX)
    recuadro_txt(100,txt)
    print(Fore.LIGHTBLUE_EX)
    
def precaucion(txt=[]):
    print(Fore.LIGHTYELLOW_EX) 
    recuadro_txt(100,txt)
    print(Fore.LIGHTBLUE_EX)

def alerta(txt=[]):
    print(Fore.LIGHTRED_EX)
    recuadro_txt(100,txt)
    print(Fore.LIGHTBLUE_EX)

if __name__ == "__main__":
     
    lista_txt = (["todo bien"])
    aviso(lista_txt)
    precaucion(lista_txt)
    alerta(lista_txt)
    #recuadro_txt(100, lista_txt)


    
    
    # encabezado(titulo = "ProManSys")
    # # opciones = ["Almacen","Carniceria", "Verduleria"]
    # # opcion = genera_menu(opciones, "Menu")
    # # genera_menu(opciones, "Categorias")
    # # print(opcion)
    # #    opcion = input(f"\n{SANGRIA}{INGR_OPC}")
    #  #   return opcion
    # listados()
