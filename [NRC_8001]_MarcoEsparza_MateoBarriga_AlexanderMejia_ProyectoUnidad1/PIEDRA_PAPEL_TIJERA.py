"""
JUEGO DE PIEDRA - PAPEL O TIJERA

Se juega de dos en dos, para este caso el usuario vs la maquina. Los jugadores deben
elejir: piedra, papel o tijera, justo al acabar la eleccion en la pantalla veran quien
gana. Si los dos jugadores sacan lo mismo hay empate.

Autores: Marco Esparza, Mateo Barriga, Alexander Mejia.

Version: VR.1.1
"""
# para ejecutar el programa necesitamos la librería random
import random

def JuegoPiedraPapelTijera():
    """
    Proceso que compara lo que ingresa el usuario con lo que elije 
    aleatoriamente la maquina.
    ----------------------
    Parametros:
         1. Piedra : int
         2. Papel : int
         3. Tijera : int
            Valores que ingresa el usuario
    ----------------------
    Retorna:
         Si retorna valor elejido por la maquina, empate, si gana o pierde
    """

    # el usuario elije e ingresa una entrada
    usuario = input("A jugar! ** '1' Piedra - '2' Papel - '3' Tijera **\n")
    print("Tu elejiste: ", usuario)
    # la maquina elije una opcion aleatoriamente
    maquina = random.choice(['1', '2', '3'])
    print("La maquina elijio: ", maquina)
    # comparamos la eleccion del usuario y de la maquina
    if usuario == maquina:
        # si son iguales los valores retorna un empate
        return 'EMPATE!!'
    # preguntamos si gana el usuario o la maquina
    if ganador(usuario, maquina):
        # gana usuario retorna ganas
        return 'TU GANAS!!'
    # gana maquina retorna pierdes    
    return 'TU PIERDES!!'

def ganador(jugador, oponente):
    """
    Proceso en el que establecemos al usuario como jugador y a la maquina
    como oponente para conocer al ganador.
    ----------------------
    Parametros:
         jugador : int
         oponente : int
            Valores que ingresa el usuario
    ----------------------
    Retorna:
         Si retorna al ganador
    """
    # Determinamos las siguientes reglas para conocer al ganador 1 > 3, 3 > 2, 2 > 1
    if (jugador == '1' and oponente == '3') or (jugador == '3' and oponente == '2') \
        or (jugador == '2' and oponente == '1'):
        # retorna cuando el jugador gana
        return True

if __name__ == '__main__':
    # inicializamos del juego
    print("*****************************************************")
    print("************** PIEDRA - PAPEL O TIJERA **************") 
    print("                 Usuario vs Maquina                  ")
    print("                   Buena Suerte !!                   ") 
    print("*****************************************************")
    print("Nombre del usuario:")
    # solicitamos el nombre del usuario
    nombre = input('')
    print("Buena suerte ", nombre, "!")
# el usuario podra jugar las veces que quiera
while(True):
    # llamamos al proceso
    print(JuegoPiedraPapelTijera())
    # preguntamos si el usuario quiere volver a jugar
    print("Deseas jugar otra vez ", nombre, "?")
    jugarOtravez = input(" (si/no): ")
    if jugarOtravez.lower() != "si":
        print("El juego ha terminado")
        # detenemos el bucle por completo
        break