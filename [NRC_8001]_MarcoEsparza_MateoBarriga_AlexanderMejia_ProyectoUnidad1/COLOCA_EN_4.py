"""
JUEGO DE COLOCA EN 4 
Este juego consiste en colocar 4 fichas del mismo color, en este caso de la misma forma para poder ganar el juego estas podran ser tanto filas como columnas,
hay cierta cantidad de veces que se puede usar una columna. dependera de la cantidad que quiera jugar los usuarios
o el usuario

Autor: Mateo Barriga, Marco Esparza, Alexander Mejia 

Version: 1.0
(no se usara tildes en direntes palabras del programa o coentado, ya que es una mala practica de programacion)
"""

import random
from copy import deepcopy
from colorama import init, Fore, Style 

"""
Para oder nosotros hacer funcionar nuestro programa, debemos primero descargar una nueva libreria que no vino en el 
paquete de instalcion que usamos en clase, la nueva librea es colorama en para que esta pueda scar colores en al
momento de ejecutar. 

La libreria tkinter funciona para la creacion y desarrollo de aplicaciones de escritorio. Al igual que facilita 
el posicionamiento y desarrollo de una interfaz grafica de escritorio con python.

librearia de igual forma la imporatmos ya que con eso usaremos el turno de cada uno de los participantes cuando iniie el juego 

Copy verifica y hace simulaciones del tablero, solo copia el tablero en si 
"""

init()

#tenemos variables de inicializacion en la cual vamos a ir usando en el programa 
MINIMO_FILAS = 5 #validacion de la cantidad minima de filas que tendra la tabla del juego 
MAXIMO_FILAS = 10 #validacion de la cantidad maxima de filas que tendra la tabal del juego 
MINIMO_COLUMNAS = 6# validacion de las cantida minima de columnas que tendra la tabal del juego
MAXIMO_COLUMNAS = 10# validacion de las cantida maxima de columnas que tendra la tabal del juego
ESPACIO_VACIO = "" #nos va adecri si pudeo poner una pieza 
COLOR_1 = "x"#color y forma del jugador 1
COLOR_2 = "o"#color y forma del jugador 2
JUGADOR_1 = 1

#la cpu tambiem es le jugador 2
JUGADOR_2 = 2
CONECTA = 4
ESTA_JUGANDO_CPU = False#constante de si esat jugando la CPU 

def solicitar_entero_valido(mensaje):
    """
    En este procedimiento lo que hacemos es solictar un numero entero y lo siguiente 
    solicitando mientras no sea un entero valido, hacemos un ciclo infinito hasta que el entero sea valido
    parametros: 
    mensaje 

    retorna:
    posible_entero
    """
    #ciclo de repeticion infinito hasta que el entero sea valido
    while True:
        #ejecutamos el bloque con las sentencias que vamos a ejecutar 
        try:
            #variable donde vamos a guadar 
            posible_entero = int(input(mensaje))
            #retorno de variable 
            return posible_entero
        #sentancia de excepcion, se va a rompar cuando el entero sea valido
        except ValueError:
            continue 


def solicitar_columnas():
    """
    Esat funcion valida que el nmumero de columnas este dentor del rango del min y max, igual pide el numero 
    que va a ingresar 
    parametros: 
    -----
    retorna:
    columnas 
    """
    #ciclo de repeticion por si entra ingresa mal el numero de max y min de la validacion de enteros 
    while True:
        #parametro donde se va a guardar el numero ingresado
        columnas = solicitar_entero_valido("Ingresa el numero de columnas:")
        #condicional de min y max de columnas
        if columnas < MINIMO_COLUMNAS or columnas > MAXIMO_COLUMNAS:
            #imprime el siguiente mensaje
            print(f"El minimo de columnas es {MINIMO_COLUMNAS} y el maximo {MAXIMO_COLUMNAS}")
        else:
            return columnas


def solicitar_filas():
    """
    Esat funcion valida que el nmumero de filas este dentro del rango del min y max, igual pide el numero 
    que va a ingresar 
    parametros: 
    -----
    retorna:
    filas 
    """
    #ciclo de repeticion infinito hasta que cumpla la condicion
    while True:
        #guarda en una variable el dato 
        filas = solicitar_entero_valido("ingresa el numero de filas:")
        #condicional de validacion 
        if filas < MINIMO_FILAS or filas > MAXIMO_FILAS:
            #imprimir la cantidad de filas 
            print (f"El minimo de filas es {MINIMO_FILAS} y el maximo {MAXIMO_FILAS}")
        else:
            #retorno de dato
            return filas


def crear_tablero(filas, columnas):
    """
    Esta funcion inicializa la matriz 
    parametros: 
    filas y columnas
    retorna:
    tablero
    """
    #creamos parametro 
    tablero = []
    #realiza un ciclo y agreag filas a la matriz 
    for fila in range (filas):
        #agrega el elemnto completo al final de la lista 
        tablero.append ([])
        #otro ciclo de repeticon para las colomnas
        for columna in range (columnas):
            #agrega espacion vacios a la matriz igual 
            tablero[fila].append(ESPACIO_VACIO)
    #retorno tablero 
    return tablero

def imprimir_tablero(tablero):
    """
    Esat funcion imprime los separdores y la creacion en si del tablero para que vaya tomadno forma 
    parametros: 
    tablero
    retorna:
    ------
    """
    #imprime numeros de columnas 
    print ("|", end="")
    #ciclo de repricion imprimimer dependiedno la longitud del tablero 
    for f in range(1, len(tablero[0])+1):
        #imprime depedneidno la longitud del tablero 
        print(f, end="|")
    #imprime espacios 
    print(" ")
    #ciclo de repeticion de los datos  
    for fila in tablero:
        #imprimero el tablero por el numero de filas
        print("|", end="")
        #ciclo de repeticion de los datos 
        for valor in fila:
            #designamos el color de pisa 
            color_terminal=Fore.GREEN
            # va ir pintando del color asignado a la ficha por medio de un condicional
            if valor == COLOR_2:
                #define otro color para la otra pieza 
                color_terminal=Fore.RED
            #imprime la ficha ya pintada 
            print(color_terminal + valor, end="")
            print(Style.RESET_ALL, end="")
            #imprime el tablero 
            print("|", end="")
        #imprime espacio del tablero
        print(" ")
    #imprime con que figuras vamos a tener el tablero 
    print("+", end="")
    #cliclo de repeticion de el rango del tablero 
    for f in range(1, len(tablero[0])+1):
        #imprime la cantidad de veces del rango 
        print ("-", end="+")
    #imprime espacio
    print (" ")



def obtener_fila_valida_en_columna(columna, tablero):
    """
    Esta valida la fila valida de la columna esta nos retorna eso, queire decir que si una fila esta basia 
    me va a regresar una que este basia y dentro del rango
    parametros: 
    columna, tablero
    retorna:
    indice o -1
    """
    # guardamos el parametro y la funcion len me devuelve un valor entero que indica la cantidad de caracteres en 
    #la cadena de entrada
    indice=len(tablero)-1
    #cilo condicional 
    while indice >= 0:
        #condiciones para el retorno 
        if tablero[indice][columna]==ESPACIO_VACIO:
            #retorna indice 
            return indice
        #disminuye 
        indice -= 1
    return -1


def solicitar_columna(tablero):
    """
    Solicita la columan y devuelve la columna ingresada -1 para ser usada facilmente como indice 
    parametros: 
    tablero
    retorna:
    columnas 

    """
    #ciclo de repeticion hasta que sea verdadero
    while True:
        #se ayuda de entero valido y solo ingersa la columna 
        columna = solicitar_entero_valido("Ingresar la columna para colocar la pieza: ")
        #condicon de que si ingresa un numero mas de los sleccionados para el tablero
        if columna <= 0 or columna > len(tablero[0]):
            #imprime un mensaje
            print ("columna no valida")
        #condicon de que si ingresa un numero mas de los sleccionados para el tablero
        elif tablero[0][columna -1]!= ESPACIO_VACIO:
            #imprimer una mansaje 
            print("esa columna ya esta llena")
        #condicion
        else:
            #retorna falso
            return columna-1


def colocar_pieza(columna, jugador, tablero):
    """
    coloca una pieza en el tablero. La columna debe comenzar en 0
    parametros: 
    columna, jugador, tablero
    Retorna:
    verdaero o falso
    """
    #defina el la pieza en el tablero
    color=COLOR_1
    #condicional si es e� jugador 2 
    if jugador == JUGADOR_2:
        #defina la pieza del tablero y la pinta
        color=COLOR_2
    #esat fila valida nos va dar un menos 1 si esta lleno y nos da un falso
    fila = obtener_fila_valida_en_columna(columna, tablero)
    #si nos da -1 esta llena 
    if fila == -1:
        return False 
    #aqui ya esta modificada la pieza y y damos un true para decir que la colcacion esta exitosa 
    tablero[fila][columna]=color 
    return True 

def obtener_conteo_derecha(fila, columna, color, tablero):
    """
    inicia unas columnas, mas son cordenadas que cuenta si tenemos piezas juntas del misno color, es en una linea
    recta hacia la derecha de la matriz no vamos en Y 
    parametros: 
    fila, columnas, color, tablero 
    retorno: 
    contador
    """
    #guardamos el parametro y la funcion len nos devuelve un valor entero que eindica la cantidad de caracteres en la cadena
    #de entrada
    fin_columnas=len(tablero[0])
    #inicamos una variable contador
    contador=0
    #ciclo de repeticion deonde utilizamos range para representar una secuancia inmutable de numeros
    for i in range(columna, fin_columnas):
        #condicion para el retorno
        if contador >= CONECTA:
            return contador 
        #condicion para el tablero 
        if tablero[fila][i]==color:
            #aumenta contador
            contador+=1
        else:
           contador = 0
    #retrono del contador 
    return contador

def obtener_conteo_izquierda(fila, columna ,color, tablero):
    """
    inicia unas columnas, mas son cordenadas que cuenta si tenemos piezas juntas del misno color, es en una linea
    recta hacia la izquierda de la matriz no vamos en Y 
    parametros: 
    fila, columnas, color, tablero 
    retorno: 
    contador
    """
    contador=0
    #-1 porque no es inclusivo
    for i in range(columna,-1,-1):
        #condicion para el retorno
        if contador >= CONECTA:
            return contador
        #condicion para el tablero 
        if tablero[fila][i]==color:
            #aumenta contador
            contador+=1
        else:
            contador=0
    #retorno del contador 
    return contador


def obtener_conteo_abajo(fila, columna, color, tablero):
    """
    inicia unas columnas, mas son cordenadas que cuenta si tenemos piezas juntas del misno color, es en una linea
    recta hacia abajo 
    parametros: 
    fila, columnas, color, tablero 
    retorno: 
    contador
    """
    #guardamos el parametro y la funcion len nos devuelve un valor entero que eindica la cantidad de caracteres en la cadena
    #de entrada
    fin_filas=len(tablero)
    #contador en 0
    contador=0
    #ciclo de repeticion deonde utilizamos range para representar una secuancia inmutable de numeros
    for i in range(fila, fin_filas):
        #condicion para el retorno
        if contador >= CONECTA:
            #retorno del contador
            return contador
        #condicion para el tablero 
        if tablero[i][columna]==color:
            #aumenta el contador 
            contador += 1
        #caso contrario 
        else: 
            contador = 0
    #retorno del contador 
    return contador 


def obtener_conteo_arriba(fila, columna, color, tablero):
    """
    inicia unas columnas, mas son cordenadas que cuenta si tenemos piezas juntas del misno color, es en una linea
    recta hacia abajo 
    parametros: 
    fila, columnas, color, tablero 
    retorno: 
    contador
    """
    #contador en 0 
    contador=0
    #-1 porque no es inclusivo
    for i in range (fila,-1,-1):
        #condicion para el retorno
        if contador >= CONECTA:
            #retorno del contador 
            return contador 
        #condicion para el contador 
        if contador >= CONECTA:
            #retorno del contador 
            return contador
        #condicion para el tablero 
        if tablero[i][columna]==color:
            #aumenta el contador si cumple 
            contador +=1
        #caso contrario 
        else:
            contador=0
    #retorno del contador 
    return contador 


def obtener_conteo_arriba_derecha(fila,columna,color,tablero):
    """
    aqui lo que se hace debemos ya tener filas  columnas y debemos ir aumentando en uno la fila y la columna este algoritmo 
    recorre cada celda 
    parametros: 
    filas, columnas, color, tablero 
    retorno: 
    contador 
    """
    #creamos un contador 
    contador =0
    #guardamos paramtros 
    numero_fila=fila
    #guardamos parametros
    numero_columna=columna
    #ciclo de repetcion condicional para el numero de filas y columans 
    while numero_fila >= 0 and numero_columna < len(tablero[0]):
        #condicional de contador 
        if contador >= CONECTA:
            #retorno contador 
            return contador
        #condicional del tablero 
        if tablero[numero_fila][numero_columna]==color:
            #aumento del contador 
            contador +=1
        #caso contrario 
        else:
            #contador que este en 0
            contador=0
        #disminuye  el numero filas 
        numero_fila -=1
        #aumenta el numero de filas 
        numero_columna +=1
    #retorna el contador
    return contador

def obtener_conteo_arriba_izquierda(fila, columna, color, tablero):
    """
    aqui lo que se hace debemos ya tener filas  columnas y debemos ir aumentando en uno la fila y la columna este algoritmo 
    recorre cada celda 
    parametros: 
    filas, columnas, color, tablero 
    retorno: 
    contador 
    """
    #contador inicia en 0 
    contador=0
    #creamos parametro y guardamos fila
    numero_fila=fila
    #creamos parametro y guardamos columna
    numero_columna=columna 
    #ciclo repetitivo con condicional 
    while numero_fila >= 0 and numero_columna >= 0:
        #condicion para que retorne contador 
        if contador >= CONECTA:
            #retorno del contador 
            return contador
        #condicion para que el contador aumente o caso contrario el contador quede en 0 
        if tablero[numero_fila][numero_columna]==color:
            #contador aumenta 1
            contador += 1
        else:
            #contador queda en 0
            contador = 0
        #numero de filas disminuye
        numero_fila -=1
        #numermo de columnas disminuye 
        numero_columna -=1
    #retorno del contador 
    return contador 


def obtener_conteo_abajo_izquierda(fila, columna, color, tablero):
    """
    aqui lo que se hace debemos ya tener filas  columnas y debemos ir aumentando en uno la fila y la columna este algoritmo 
    recorre cada celda 
    parametros: 
    filas, columnas, color, tablero 
    retorno: 
    contador 
    """
    #contador inicia en 0 
    contador=0
    #creamos uan variable y guardamos 
    numero_fila=fila 
    #creamos variable y guardamos 
    numero_columna=columna 
    #crea ciclo de reteticion con condicon que nos va adevolver un valor entero que inidica la cantidad de caracteteres 
    #en una cadena entrada
    while numero_fila < len(tablero) and numero_columna >= 0:
        #condicion para cntador para realizar el retorno
        if contador >= CONECTA:
            #retona contador 
            return contador
        #condicion para el tablero y aumento del contador 
        if tablero[numero_fila][numero_columna]==color:
            #aulmento del contador 
            contador += 1
        #caso contrario 
        else:
            contador =0
        #aumenta el numero de de las filas 
        numero_fila += 1
        #disminuye el numero de filas 
        numero_columna -= 1
    return contador


def obtener_conteo_abajo_derecha(fila, columna, color, tablero):
    """
    aqui lo que se hace debemos ya tener filas  columnas y debemos ir aumentando en uno la fila y la columna este algoritmo 
    recorre cada celda 
    parametros: 
    filas, columnas, color, tablero 
    retorno: 
    contador 
    """
    #inicia el contador en 0 
    contador =0
    #crea y guarda la variable de fila 
    numero_fila=fila 
    #crea y guarada la varieble columna 
    numero_columna=columna
    #crea ciclo de reteticion con condicon que nos va adevolver un valor entero que inidica la cantidad de caracteteres 
    #en una cadena entrada
    while numero_fila < len(tablero) and numero_columna < len(tablero[0]):
        #condicion para el retorno del contador 
        if contador >= CONECTA:
            #retorno del contador 
            return contador 
        #condicion del tablero para que el contador 
        if tablero[numero_fila][numero_columna]==color:
            #contador aumenta 
            contador += 1
        #caso contario 
        else:
            #contador en 0 
            contador=0
        #aumento del numero de las filas 
        numero_fila+=1
        #aumento del numero de las columnas 
        numero_columna+=1
    return contador

def obtener_direcciones():
    """
    aqui va atenr una de las direcciones creadas en la aprte de arriba para que sea una sola, solo nos va a dar el nombre
    de uan funcion dada ya en la parte de arriba 
    parametros:
    ------------
    retorna :
    'izquierda',
        'arriba',
        'abajo',
        'derecha',
        'arriba_derecha',
        'abajo_derecha',
        'arriba_izquierda',
        'abajo_izquierda',
    """
    return[
        'izquierda',
        'arriba',
        'abajo',
        'derecha',
        'arriba_derecha',
        'abajo_derecha',
        'arriba_izquierda',
        'abajo_izquierda',
    ]


def obtener_conteo(fila, columna, color, tablero):
    """
    aqui vamos a obtener el conteo general de saber si en cualquier direccion ya conectada invocamos a una funcion
    en cadena 
    parametros:
    fila, columan, color, tablero
    retorna:
    conteo y un 0 
    """
    direcciones=obtener_direcciones()
    for direccion in direcciones:
        #obtengo las funciones globales as varibales, de igual forma invocamos a las direcciones 
        funcion = globals()['obtener_conteo_' +direccion]
        #invocamos a funcion y nos ahorramos un if y de todas as variables 
        conteo=funcion(fila, columna, color, tablero)
        #realizamos un conteo va a ser mayor o igual a las piezas que falta conectar 
        if conteo >= CONECTA:
            #retorna el conteo 
            return conteo
    #si no retorna un 0 
    return 0

def obtener_color_de_jugador(jugador):
    """
    aqui recibe un jugador y me dice su color 
    parametros: 
    jugador 
    retorno:
    color
    """
    #creamos variable y guardamos el color 
    color=COLOR_1 
    #condicional para que el color se guarde 
    if jugador == JUGADOR_2: 
        color= COLOR_2 
    #retorna el color 
    return color 

def comprobar_ganador(jugador, tablero):
    """
    comprueba si el jugador en ese tablero es el ganador 
    parametros: jugador, tablero 
    retorna: true, false 
    """
    #guardamos en una variable de colorres no jugadores 
    color=obtener_color_de_jugador(jugador) 
    #recorremos por todo el tabero 
    for f, fila in enumerate(tablero):
        #recorremos por la fila 
        for c, celda in enumerate(fila):
            #contamos para el color, cuento en todas las direcciones 
            conteo= obtener_conteo(f, c, color, tablero)
            #si el conteo superal al que necesita ganar retorna un verdadero, comprobando que el jugador 
            if conteo >= CONECTA:
                #retorna un true si conecto las 4 fichas 
                return True 
    #retorna un falso si no conecto las 4 fichas
    return False 

def elegir_jugador_al_azar():
    """
    aqui escoge un jugador al azar pasa un arrecho con dos opciones elige unas de ellas dos y va a devolvermelo 
    parametro: 
    -----------
    retorna:
    una funcion random de dos opciones
    """
    return random.choice([JUGADOR_1, JUGADOR_2])


def imprimir_y_solicitar_turno(turno, tablero):
    """
    aqui nos dice que jugador es que caracter y nos dice el turno de cada quien 
    parametros:
    turno, tablero
    retorna: 
    solicitar_columna(tablero)
    """
    #nos define el color que va a tener cada jugador cuandola se jeugue contra la cpu 
    if not ESTA_JUGADOR_CPU:
        #imprimer el color que va ataner cada usuario al jugar 
        print(f"jugador 1: {COLOR_1} |  Jugador 2: {COLOR_2}")
    #caso contrario va a definir el color de usuario contra la cpu 
    else:
        #imprime el color de del usuario y de la cpu
        print(f"jugador 1: {COLOR_1} | CPU: {COLOR_2}")
    #define el turno del jugador 1 cuando sea su turno
    if turno == JUGADOR_1:
        #imprime el color y cuadno sea turno del jugador 1 
        print(f"turno del jugador 1 ({COLOR_1})") 
    #caso contrario si no es la cpu y es el jugador 2 imprimira su turno y el color correspondido 
    else: 
        #cuando no esta la CPU
        if not ESTA_JUGADOR_CPU:
            #imprime el turno del jugador 2 y el color 
            print (f"turno del jugador 2 ({COLOR_2})") 
        #caso controario si no hya jugador 2 sera turno de la computadora 
        else:
            #imprimer el turno de CPU
            print("turno de la cpu")
    #retorna la solicitud de la columan 
    return solicitar_columna(tablero)

def felicitar_jugador(jugador_actual):
    """
    en esta funcion solo se felicita  a los ganadores ya sea el jugador 1 o 2 o inclusive la CPU
    parametros: jugador_actual
    retorna: 
    ---------
    """
    # cuando no este jugando la computadora vamos a felicitar a jugador 1 y jugadoar 2 
    if not ESTA_JUGANDO_CPU:
        #si gana el jugador uno imprimira un mensaje 
        if jugador_actual==JUGADOR_1:
            #imprime las felicitadciones al jugdaor 1 
            print("felicidades jugador 1. has ganado")
        #caso contrario felicitara la jugdaor 2 
        else:
            #imprimimos las felicitaciones al jugador 2 
            print("felicidades jugador 2. has ganado")
    # caso contrario cuandoe l jugador este contra la computadora se realiza las siguientes felicitaciones 
    else:
        #si gana jugador 1 se realiza la sugiinet imprecion de mensaje
        if jugador_actual == JUGADOR_1:
            #imprimimos el mensaje de felicitacion 
            print ("felicidades jugador 1. has ganado")
        #en caso de que no gane el jugador 1
        else:
            #imprimimos que ha ganado el CPU
            print("ha ganado el cpu")


def es_empate(tablero):
    """
    se raaliza la operacion en caso de que sea empate entre los jugadores 
    parametros:
    tablero
    retorna:
    verdadero o falso
    """
    #recorre por las columnas del tablero para ver si hay un empate en verdad
    for columna in range(len(tablero[0])):
        #llamamos a funcion para comprobar en caso de que si hay y este nos vote un falso 
        if obtener_fila_valida_en_columna(columna, tablero)!= -1:
            #retorna un falso
            return False
    #retorna un verdadero
    return True


def indicar_empate():
    #indica una funcion de empate en donde solo nos imprime un mensaje de empate
    #parametros:------
    #retorno:------
    print("empate")


def obtener_tiradas_faltantes_en_columnas(columna,tablero):
    """
    esta nos avisa cuantas tiradas nos faltan a los jugadores se cuenta y se va restando 
    parametros: columnas, tablero
    retorna: tiradas
    """
    #guardamos en una variable y restando el numero de tiradas que faltan
    indice = len(tablero)-1 
    #inicializacion de numero de tiradas
    tiradas=0
    #ciclo condicional para que realice el proceso
    while indice >= 0:
        # validacion para que si hay un espacio basio se agregue un tiro
        if tablero[indice][columna]==ESPACIO_VACIO:
            #aumento de tiradas
            tiradas +=1
        #disminucion del indice de tiradas
        indice -=1
    #retorna las tiradas
    return tiradas 

def obtener_tiradas_faltantes(tablero):
    """
    en esta funcion se realixa el numero de tiradas faltantes en las columnas 
    parametros: tablero
    retorna: tiradas
    """
    #inicia en las tiradas en 0 
    tiradas=0
    #recorre el tablero por cada columna contando las tira faltantes y las va aumentando 
    for columna in range(len(tablero[0])):
        #recorrido por el pablero y aumento de las tiras 
        tiradas += obtener_tiradas_faltantes_en_columnas(columna, tablero)
    #retorno de la tiras
    return tiradas 

def imprimir_tiradas_faltantes(tablero):
    """
    en esta funcion imprime las tiradas flatantes del tablero 
    parametros: tablero
    retorna:-------
    """
    #imprime las tiradas faltantes que estan en el tablero
    print("tiradas flatntes: "+ str(obtener_tiradas_faltantes(tablero)))


def jugador_vs_jugador(tablero):
    """
    en esta funcion se raliza la operacion del juego entre dos usiaros, donde van colocando las figuras que se
    les asignan y demas, para asi poder juga
    parametros:
    tablero
    retorna:
    ----------
    """
    #iniciamos el jugdor uno o el judaor dos esto sera al azar 
    jugador_actual= elegir_jugador_al_azar()
    #ciclo infinito 
    while True:
        #imprimimos el tablero 
        imprimir_tablero(tablero) 
        #imprimir las tiras faltantes 
        imprimir_tiradas_faltantes(tablero) 
        #aqui guardamos el parametro e imprimimos y solicitamos turnos el jugador actual 
        columna=imprimir_y_solicitar_turno(jugador_actual, tablero)
        #se pide la coluna y la trata de colecoar la peiza 
        pieza_colocada=colocar_pieza(columna, jugador_actual, tablero)
        #condicion de que si no se deja colcoar la pieza
        if not pieza_colocada:
            #omprecio de un mensaje 
            print("no se puede coloar en esa columna")
        #vomprovacacio si el jugador a ganado 
        ha_ganado=comprobar_ganador(jugador_actual, tablero)
        #esta accion puede que se repita algun rato asi que s pocede a realixar la felicitacion 
        if ha_ganado:
            #comprovamos si es verdaero o flaso la gnanacia e imprime el tablero 
            imprimir_tablero(tablero) 
            #procede a realixar la felicitacion 
            felicitar_jugador(jugador_actual)
            break
        #por si el tablero termina en empate 
        elif es_empate(tablero): 
            #imprimer el tablero 
            imprimir_tablero(tablero) 
            #seidnica el empate 
            indicar_empate()
            break
        #se tuena os turnos 
        else:
           #se hace un cambio en ,so turnos 
            if jugador_actual == JUGADOR_1:
                #si la cpndicion no se cumple procede a realizar el seundo jugador
                jugador_actual = JUGADOR_2
            else: 
                #si no es el primer jugador
                jugador_actual=JUGADOR_1


def obtener_columna_segun_cpu(jugador, tablero):
    """
    etsa funcion nos permite ver los mmovimientos de la cpu 
    parametros:
    jugador, tablero
    retorna:elegir_columnas_ideal(jugador, tablero)

    """
    return elegir_columnas_ideal(jugador, tablero) 


def obtener_jugador_contrario(jugador):
    """
    en esta funcion es una funcion que etsa repetid pero quei es cuestion de lso turnso que nada jugador va a llevar
    paremtros:
    jugador
    REtorna:
    jugador_1
    """
    #condicion de a que jugaor le va aa tocar 
    if jugador == JUGADOR_1:
        return JUGADOR_2
    return JUGADOR_1


def elegir_columnas_ideal(jugador, tableroOriginal):
    """
    aqui es donde la cpu piensa en donde va a poner su ficha cuando se juegue con ella 
    parametros: jugador, tableroOriginal
    Retorna:
    colomna disponible
    """
    #inicializa variable dejando que las clases definidad anterioermente se anulen la operaciones o el conjunto de componestes copiados
    tablero=deepcopy(tableroOriginal)
    #guarda la varibale
    columna_ganadora= obtener_columna_ganadora(jugador, tablero) 
    #condicion para el retirno 
    if columna_ganadora != -1:
        return columna_ganadora
    #gardamos variable 
    columna_perdedora=obtener_columna_ganadora(obtener_jugador_contrario(jugador), tablero) 
    #condicion para el retorno
    if columna_perdedora != 1:
        return columna_perdedora 

    #se guarda una especie de contador
    umbral_puntaje=1
    #obetenmos lo puntajes de las as
    puntaje_ganador, columna_mia=obtener_columna_con_mayor_puntaje(jugador, tablero) 
    #oebtenemos el puntaje 
    puntaje_ganador_adversario, columna_adversario=obtener_columna_con_mayor_puntaje(obtener_jugador_contrario(jugador), tablero) 
    #condicion 
    if puntaje_ganador > umbral_puntaje and puntaje_ganador_adversario > umbral_puntaje:
        #condicion para que el retorno opere 
        if puntaje_ganador_adversario > puntaje_ganador:
            return columna_adversario 
        #retorno de la columna mia
        else:
            return columna_mia 
    #guardar variabel donde se ponga
    central=obtener_columna_central(jugador, tablero) 
    #condicion con -1 por lo que en programacion siempore se resta 1 por la posicion
    if central != -1:
        return central
    #disponibilida de las columnas
    columna_disponible=obtener_primera_columna_vacia(jugador, tablero) 
    if columna_disponible != -1:
        return columna_disponible
    #imprecion de error 
    print ("error. no se deberia llegar hasta aqui")

def obtener_primera_columna_vacia(jugador,tableroOriginal):
    """
    esta nos indica que columna esta vacia y de igual forama es solo un ayuda
    parametros: jugador, tableroOriginal
    Retrona: indice
    """
    tablero=deepcopy(tableroOriginal) 
    #ciclo de repeticon para poder ir vinedo donde esta la columna vacia 
    for indice in range(len(tablero[0])):
        #se busca donde se puede colocar la pieza
        if colocar_pieza(indice, jugador, tablero):
            #retorna el indice
            return indice

def obtener_columna_central(jugador, tableroOriginal):
    """
    Esta funcion es propia del cpu para que busqye en donde poder poner las fichas 
    Parametros: jugador, tableroOroginal
    REtorna: mitad
    """
    #guarda variable 
    tablero=deepcopy(tableroOriginal)
    #guarda la osocion del tablero 
    mitad=int((len(tablero[0])-1)/2)
    #concion para que ponga la ficha 
    if colocar_pieza(mitad, jugador, tablero):
        #retorna la mitad
        return mitad 
    return -1


def obtener_primera_fila_no_vacia(columna, tablero):
    """
    proceso que realiza la comutadora 
    parametros: columnas y tablero
    Retorna indice_final
    """
    #ciclo de repeio para ir por las filas del tablero
    for indice_fila, fila in enumerate(tablero):
        #verifica si tenemos un espacio 
        if fila[columna]!=ESPACIO_VACIO:
            #retorna el indice
            return indice_fila
    return -1


def obtener_columna_con_mayor_puntaje(jugador, tableroOriginal):
    """
    es propia del cpu busac en que colmna tendria mayor puntaje con tres piezas y demas 
    parametros: jugador, tableroOriginal
    Retorna:conteo_mayor, indice_columna_mayor
    """
    #inicio del contador mayor 
    conteo_mayor=0
    #inicializa en en -1 
    indice_columna_mayor=-1
    #ciclo de repeticiom del indice de la columna en una rango es una lista inmutable de numeros enteros en sucesion
    #aritmetica 
    for indiceColumna in range(len(tableroOriginal)):
        #dejamos que las clases definidas que tenemos en la parte de arriba anule a operacion de copia o el conjunto de componentes copiados
        tablero=deepcopy(tableroOriginal)
        #definimos el color de la pieza en el tablero
        pieza_colocada=colocar_pieza(indiceColumna, jugador, tablero) 
        #cunado se ponga la pieza se hara lo sguiente 
        if pieza_colocada:
            #verfica la fila qeu este vacia o no lo este 
            fila= obtener_primera_fila_no_vacia(indiceColumna, tablero) 
            #continuara e ira revisando cada una de las filas 
            if fila != -1:
                #obtenermos el conteo de las filas
                conteo=obtener_conteo(fila, indiceColumna, obtener_color_de_jugador(jugador), tablero) 
                #verificamos que este completo
                if conteo > conteo_mayor:
                    #guardamos la variable 
                    conteo_mayor=conteo 
                    #guardamos las colunas 
                    indice_columna_mayor= indiceColumna
    #retorno de la variables 
    return conteo_mayor, indice_columna_mayor

def obtener_columna_ganadora(jugador, tableroOriginal):
    """
    en esta funcion tenemos la columna ganadora, pasara revisando por toda la tabal para poder encontrar la columna ganadora 
    paramtros: jugador, tableroOriginal
    Retorna:indiceColumna 
    """
    for indiceColumna in range(len(tableroOriginal)):
        #dejamos que las clases definidas que tenemos en la parte de arriba anule a operacion de copia o el conjunto de componentes copiados
        tablero=deepcopy(tableroOriginal) 
        #verificamos las piezas que esten demas, y vea que sea correcto la ganacia  
        pieza_colocada=colocar_pieza(indiceColumna, jugador, tablero) 
        #condicoon para realizar las demas operaciones
        if pieza_colocada:
            #comprobamos que sea la columna ganadora
            gana=comprobar_ganador(jugador, tablero)
            #si es la columna ganadora retorna el indiceColumna
            if gana:
                return indiceColumna
    #caso contrario no lo hara 
    return -1

def jugador_vs_computador(tablero):
    """
    es la misma dinamica de jugador contra jugado ahora solo con computadora, pero en ves de solicutar el 
    turno la computadora lo juega
    parametros:tablero
    Retorno:
    --------
    """
    #llamamos a nuestra funcion 
    global ESTA_JUGADOR_CPU
    #activamos la varibale 
    ESTA_JUGADOR_CPU=True
    #el jugador que comenzara primero ya cea el usuario la cpu
    jugador_actual=elegir_jugador_al_azar()
    #inicio del juego mediante un bucle infinito hasta que deje de cumplir 
    while True:
        #imprecion del tablero 
        imprimir_tablero(tablero)
        #imprecion de los tiros que faltan
        imprimir_tiradas_faltantes(tablero)
        #condicon de jugador 1 para que inice jugando 
        if jugador_actual==JUGADOR_1:
            #da paso al jugador uno
            columna=imprimir_y_solicitar_turno(jugador_actual, tablero) 
        else: 
            #aqui no solicita el turno si no que solo li imprime hast que el computador lo ponga en la columna 
            print("cpu pensado...")
            #el cpu pone la ficha y ya no el usuario
            columna=obtener_columna_segun_cpu(jugador_actual, tablero) 
        #pieza esta colocada
        pieza_colocada=colocar_pieza(columna, jugador_actual, tablero) 
        #validacion de la pieza de si no esta colocada
        if not pieza_colocada: 
            #imprime la si no se puede realizar la validacion
            print("no se puede colocar en esa columna")
        #funcion de si gano o el computador
        ha_ganado=comprobar_ganador(jugador_actual, tablero) 
        #si ha ganado realiza las siguientes operaciones
        if ha_ganado:
            #imprime el tablero
            imprimir_tablero(tablero) 
            #felicta el jugador ganador
            felicitar_jugador(jugador_actual) 
            break 
        #en caso de que se empate
        elif es_empate(tablero):
            #imprime el tablero del empate
            imprimir_tablero(tablero) 
            #indica el empate 
            indicar_empate()
            break 
        #caso cotrario define el judaor 
        else: 
            #defiene el jugador
            if jugador_actual==JUGADOR_1: 
                #define el jugador 2
                jugador_actual=JUGADOR_2
            else: 
                #define el jugdaor 1
                jugador_actual=JUGADOR_1
    #termina el uso de la cpu 
    ESTA_JUGADOR_CPU=False 

def volver_a_jugar():
    """
    En esta funcion se pregunata a lso jugadores o el jugador desea jugar de nuevo 
    prametros:
    ----------
    Retorno:
    true o false
    """
    #ciclo repetitivo de si va a repetir el juego
    while True:
        #eleccion de la pregunta
        eleccion=input("volver a jugar? [s/n]").lower()
        #si toma la eleccion de si nos dara un verdero
        if eleccion=="s":
            return True
        #si la decision es no entonces sera falso
        elif eleccion =="n":
            return False

def main():
    """
    va a ser la cabecilla de todo para que inicie el juego mediante unmenu 
    parametros:
    ------------
    retorno:
    -----------
    """
    #inidel ciclo inifonito hasta que escoja una de las opciones 
    while True:
        #menu de ociones 
        eleccion=input("1-jugador vs jugador"
                       "\n"                  
                       "2- jugador vs maquina"
                       "\n"
                       "3- salir"
                       "\n"
                       "elegie: ")
        #si escoje el 3 sale del menu y del progrma 
        if eleccion=="3":
            break 
        #en caso de que haya sido uno llamaos a las siguientes funciones para que inicie el juego 
        if eleccion =="1":
            #creamos el tablero con las filas 
            filas,columnas= solicitar_filas(), solicitar_columnas()
            #crea tablero y llama a la funcion de juagr 1 contra uno 
            while True:
                #tablero creado
                tablero=crear_tablero(filas, columnas) 
                #funcion de juego 
                jugador_vs_jugador(tablero) 
                #en caso de ya no jugar 
                if not volver_a_jugar(): 
                    break
        # si escoger la opcion dos sera lo mismo pero contra el cpu
        if eleccion=="2":
            #llama las filas columnas y tablero 
            filas,columnas=solicitar_filas(), solicitar_columnas()
            #ciclo infinito para el tablero y juego hasta que termine y devuelva un false
            while True:
                #crea el tablero 
                tablero=crear_tablero(filas,columnas) 
                #juego contra la cmputadora 
                jugador_vs_computador(tablero)
                #para ya no volver a jugar 
                if not volver_a_jugar(): 
                    #rompe todo el ciclo
                    break 
        
#invoca el main 
main()