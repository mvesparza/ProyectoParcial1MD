"""
JUEGO DE LA SERPIENTE

El juego de la serpiente consiste en controlar una serpiente animada mediante las flechas de dirección de nuestro teclado
e ir comiendo las frutas o comida que aparece en nuestra pantalla.

Autores: Alexander Mejía, Marco Esparza, Mateo Barriga

Version 1.0

Haremos uso de variables en español para el mejor manejo del código con la excepción de la sintaxis en python donde 
oligatoriamente usamos el ingles como lenguaje de ensamblamiento.
"""
import pygame, sys, time, random
"""
Importamos la librería pygame y varias herramientas que incluyen en su paquetería, además importaremos la librería random
ya que estás dos librerías no incluyen en el paquete de instalación por defecto, para estilizar nuestro cuadro de juego y 
las funciones que debe ir adoptando el entorno y el objeto controlar.
"""
pygame.init()

#pantalla del juego de 500 por 500
cuadro_juego = pygame.display.set_mode((500, 500))
"""
Esteblecemos la variable cuadro_juego y mediante la librería pygame su modulo display y la funcion set_mode generamos una
vetana en donde se ejecutará el juego de la serpiente estableciedno los valores del cuadro en 500 pixeles de ancho por 500 
pixeles de alto.
"""
#varible que establece y estiliza la fuente del puntaje
fuente = pygame.font.Font(None,30)
"""
Nuestra variable fuente es la que se encarga de dar cuerpo al texto que saldrá en nuestro cuadro de juego, haciendo uso de
la librería pygame, su modulo font y su función Font con un tmaño de 30 pixeles.
"""
#pixeles o fotogramas por segundo
fps = pygame.time.Clock()
"""
Con nuestra variable fps obtendremos un control en la velocidad de movimiento de nuestra serpiente y en este caso la usaremos
para aumentar los niveles en nuestro juego, aumentado de igual manera la dificultad del mismo.
"""
def comida():
    pos_aleatoria = random.randint(0,49)*10
    #                  x                y
    pos_comida = [pos_aleatoria, pos_aleatoria]
    return pos_comida
"""
Esta funcion con el nombre comida() encapsula la accion de lanzar una posicion aleatoria en toda el area de juego establecida
en la variable cuadro_juego mediante la libreria random
"""
"""
Nuestra funcion main albergará todo el código que hará funcionar nuestro juego
"""
def main():
    #estructura de la serpiente
    cabeza_serpiente = [100, 50]
    cuerpo_serpiente = [[100,50],[90,50],[80,50]]
    """
    Está parte de codigo estable el cuerpo de nuestra serpiente con cuadros pintaados en eje X y eje Y.

    La cabeza_serpiente establece la posición de nuestra serpiente y el cuerpo_serpiente es la cola de nuestra serpiente.
    """

    cambio = "Derecha"
    valor = True
    pos_comida = comida()
    puntuacion = 0
    perdiste = "HAS PERDIDO"

    """
    Establecemos variable primitivas para acudir a las mismas en diferentes casos: 

    -   cambio es una variable que determina la dirección de la serpiente
    -   valor es una variable tipo booleano la cual servirá para establecer el estado del juego en caso de perder o de querer salir
        por ejemplo en el caso de apretar x o salir en nuestro cuadro de juego nuestra variable valor cambia a False y automaticamente salimos
    -   pos_comida es una variable que alberga la función comida() y nos da la posición random de la comida
    -   puntuación es una variable inicializazda en cero que tiene el objetivo de contabiizar los puntos que hace cuando la serpiente
        come la comida
    -   perdiste es una varible que tiene como valor un texto que dice "HAS PERDIDO"
    """

    #mientras nuestro valor sea verdadero ejecutaremos las lineas de código que se hallan dentro del ciclo while
    while valor:
        #para nuestra variable event de nuestra modificación pygame.event.get()
        for event in pygame.event.get():
            # si event.type es igual a la acción de salida nuestro variable valor cambiará a False y automaticamente cerrará los procesos.
            if event.type == pygame.QUIT:
                valor = False
            # si event.type es igual a la acción determinada por nuestra librería pygame de control de dirección
            if event.type == pygame.KEYDOWN:
                # si event.key (que es dado por la accion de la tecla() es igual a derecha nuestra variable cambio tendrá el valor "Derecha"
                if event.key == pygame.K_RIGHT:
                    cambio = "Derecha"
                # si event.key (que es dado por la accion de la tecla() es igual a izquierda nuestra variable cambio tendrá el valor "Izquierda"
                if event.key == pygame.K_LEFT:
                    cambio = "Izquierda"
                # si event.key (que es dado por la accion de la tecla() es igual a arriba nuestra variable cambio tendrá el valor "Arriba"
                if event.key == pygame.K_UP:
                    cambio = "Arriba"
                # si event.key (que es dado por la accion de la tecla() es igual a abajo nuestra variable cambio tendrá el valor "Abajo"
                if event.key == pygame.K_DOWN:
                    cambio = "Abajo"
        # si cambio es igual a "Derecha" la variable cabeza_serpiente cambia sus valores mediante una suma lo que hace un efecto visaul de movimiento
        if cambio == "Derecha":
            cabeza_serpiente[0] += 10
        # si cambio es igual a "Izquierda" la variable cabeza_serpiente cambia sus valores mediante una resta lo que hace un efecto visaul de movimiento
        if cambio == "Izquierda":
            cabeza_serpiente[0] -= 10
        # si cambio es igual a "Arriba" la variable cabeza_serpiente cambia sus valores mediante una resta lo que hace un efecto visaul de movimiento
        if cambio == "Arriba":
            cabeza_serpiente[1] -= 10
        # si cambio es igual a "Abajo" la variable cabeza_serpiente cambia sus valores mediante una suma lo que hace un efecto visaul de movimiento
        if cambio == "Abajo":
            cabeza_serpiente[1] += 10

        #acciones de la serpiente
        cuerpo_serpiente.insert(0,list(cabeza_serpiente))
        """
        Aquí generaremos la simulación de cuando la serpiente come la comida establecida en el cuadro de juego, coincidiendo la posicion de la variable
        cabeza_serpiente con la variable pos_comida, diciendo que en el caso de que las posiciones sean iguales se aumenta 1 a la variabe posición, y
        automaticamente la posicion de la comida en la variable pos_comida cambiara de manera aleatoria ya que se llama a la funcion comida().
        """
        # si posicion de la variable cabeza_serpiente es igual a la posicion de variable pos_comida
        if cabeza_serpiente == pos_comida:
            pos_comida = comida()
            puntuacion += 1
            print(puntuacion)
        # caso contrario cuerpo serpiente revienta un cubo de su cuerpo_serpiente
        else:
            cuerpo_serpiente.pop() #pop elimina las  ultima posicion de un array

        cuadro_juego.fill((0,0,0))
        #dibujo de la serpiente
        for pos in cuerpo_serpiente:
            pygame.draw.rect(cuadro_juego,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(cuadro_juego,[169,6,6], pygame.Rect(pos_comida[0],pos_comida[1],10,10))
        # la variable texto adopta la condicion de la variable fuente ya establecida y mediante metodos y funciones se establece su color
        texto = fuente.render(str(puntuacion),0,(255,255,255))
        """
        En este metodo establecemos la posicion de la variable texto dentro del cuadro_juego
        """
        cuadro_juego.blit(texto,(450,470))

        """
        En esta parte del código aplicamos condicionales para determinar la dificultad de los niveles mediante un incremento de rapidez en la variable fps:
        """
        # si variable puntuacion es menor a 10 la variable fps con el metodo tick lo establecemos en 10
        if puntuacion < 10:
            fps.tick(10)
        # si variable puntuacion es mayor o igual  a 10 la variable fps con el metodo tick lo establecemos en 20 y aumenta la velocidad de la serpiente
        if puntuacion >= 10:
            fps.tick(20)
        
        """
        En esta parte de código delimitamos el espacio hasta donde nuestra serpiente tiene permitido recorrer, ya que en el caso de que la serpiente 
        toque los bordes del cuadro de juego automaticamente la variable valor cambia a False e imprime en pantalla el mensaje "Perdiste" y automaticamente
        salimos del juego
        """
        if cabeza_serpiente[0] <= 0 or cabeza_serpiente[0] >= 500:
            valor = False
            print("Perdiste")
        if cabeza_serpiente[1] <= 0 or cabeza_serpiente[1] >= 500:
            valor = False
            print("Perdiste")
        
        pygame.display.flip()
        fps.tick(10)
#llamamos la función main() para que se nos ejecute el código
main()
# con nuestra librería pygame y el metodo quit hacemos que los procesos se cierren
pygame.quit

