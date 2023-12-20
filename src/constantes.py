import numpy as np
import utils



#La función principal primero corre la función de inicio (para dar la bienvenida, crear tableros y situar barcos)
#y una vez terminada, entra en los bucles de juego
def hundir_la_flota():
    inicio()
    turno_de_juego()
    terminar_juego()
    jugar_de_nuevo()


instrucciones = """
Bienvenide al juego Hundir la flota.
El juego consiste en hundir la flota del contrincante (en este caso, la máquina). 
Para ello, deberás ir introduciendo una serie de números que representarán
las coordenadas donde atacarás al contrincante (p.ej. 5.3 significa fila 5, columna 3).
Si aciertas, seguirás jugando. Pero, si fallas, el turno pasará a la máquina y será ella quien te ataque a ti.
¡Que gane le mejor!
""" 



# La función inicio sirve para dar la bienvenida, crear tableros y situar barcos
def inicio():

    #Cuando se abre el programa, se le da la bienvenida al jugador y se le cuentan las instrucciones del juego
    print(instrucciones) 

    #Después se le presenta el tablero 10x10 que utilizará
    global jugador_tablero_barcos
    jugador_tablero_barcos = utils.Tablero((np.full((10,10), "_")))
    print(f'Este va a ser el tablero donde debes colocar tus barcos: \n {jugador_tablero_barcos.tablero}\n')
# AQUÍ SE HA DE IMPRIMIR CADA VEZ QUE LA MÁQUINA ATACA AL JUGADOR
    
    #Y se le pregunta cómo desea colocar sus barcos: aleatoria o manualmente. 
    #Según su respuesta, se llama al método de clase oportuno y se colocan los barcos en su tablero de barcos
    print(jugador_tablero_barcos.modo_colocacion())
    #En dicho tablero se van a ir reflejando los disparos que le haga la máquina

    #Se crea el tablero de juego del jugador, donde se van recogiendo los disparos que hace a la máquina: 
    #sus aciertos y fallos. Es el tablero en el que el jugador se ha de basar para tomar decisiones
    global jugador_tablero_juego
    jugador_tablero_juego = utils.Tablero((np.full((10,10), "_")))
    print(f'\nEste va a ser el tablero donde se reflejarán tus aciertos y fallos: \n {jugador_tablero_juego.tablero}\n')
# AQUÍ SE HA DE IMPRIMIR CADA VEZ QUE EL JUGADOR ATACA A LA MÁQUINA

    #Creamos el tablero de barcos de la máquina y situamos sus barcos aleatoriamente. En dicho tablero se van a ir
    #reflejando los disparos que el jugador le haga. Una vez terminada la programación, este tablero 
    #debe permanecer oculto
    global maquina_tablero_barcos
    maquina_tablero_barcos = utils.Tablero((np.full((10,10), "_")))
    maquina_tablero_barcos.colocar_barcos_aleatorio()
    print(f'Este es el tablero donde la máquina coloca los barcos: \n {maquina_tablero_barcos.tablero}\n')
# AQUÍ SE HA DE IMPRIMIR CADA VEZ QUE EL JUGADOR ATACA A LA MÁQUINA

    #Creamos el tablero de juego de la máquina, donde se van recogiendo los disparos que hace al jugador. 
    #Es el tablero en el que Python se basa para no repetir coordenadas. Una vez terminada la programación, 
    #este tablero debe permanecer oculto
    global maquina_tablero_juego
    maquina_tablero_juego = utils.Tablero((np.full((10,10), "_")))
    print(f'Este es el tablero donde se reflejan aciertos y fallos de la máquina: \n {maquina_tablero_juego.tablero}\n')
# AQUÍ SE HA DE IMPRIMIR CADA VEZ QUE LA MÁQUINA ATACA AL JUGADOR






# def dificultad():

#     mensaje = """\n Ahora debes elegir el nivel de dificultad del juego:
# Introduce 1 para nivel FÁCIL
# Introduce 2 para nivel MEDIO
# Introduce 3 para nivel DIFÍCIL
# """
#     num_dificultad = int(input(mensaje))
#     if num_dificultad == 1:
#         return f'Necesario cambiar'   
#                        #ESTO COMBINARLO CON LO DE PEPE
#     elif num_dificultad == 2:
#         return f'Necesario cambiar'  
    
#     elif num_dificultad == 3:
#         return f'Necesario cambiar'    
    
#     else:
#         print(f'{num_dificultad} no es un número válido. Inserta otro número')
#         return dificultad()


#Esta función representa el turno del jugador. 
def disparar_jugador():

    while "O" in jugador_tablero_barcos.tablero and "O" in maquina_tablero_barcos.tablero:
    #Lo primero que hace es comprobar que siguen quedando barcos en pie en cualquiera de los dos 
    #tableros; si no, mira quién ha ganado y lo saca por pantalla
    
        coordenada_disparo = input(f'\nIndica las coordenadas donde deseas disparar (p.ej. 3.5). Si deseas salir \
del juego, introduce un caracter no numérico ')
        #Se le piden las coordenadas al jugador mediante un input

        if coordenada_disparo == "E":
            break

        #Si quedan barcos en juego, verifica si el jugador quiere salir. Si no quiere salir, transforma el
        #input en coordenadas y verifica si en ellas hay agua, barco o si ya ha golpeado antes
        
        try:
            coordenada_disparo = coordenada_disparo.split(".")
            global fila
            fila = int(coordenada_disparo[0])
            columna = int(coordenada_disparo[1])

        except:
            print("Caracter no válido")
            continue

        #Primero verificamos si la persona dispara a un sitio donde ya ha disparado: si es así,
        #pasa el turno a la máquina; si no, pasa a verificar si hay agua o barco
        if jugador_tablero_juego.tablero[fila, columna] != "_":
            print(f'\nYa has disparado en esta posición')
            print(f'\njugador_tablero_juego \n{jugador_tablero_juego.tablero}')
            print(f'\nmaquina_tablero_barcos \n{maquina_tablero_barcos.tablero}')
            return (disparar_maquina_facil())
        #No marcamos nada sobre el tablero y pasa el turno a la máquina

        else: 
            if maquina_tablero_barcos.tablero[fila, columna] == "_":
                print(f'\n¡Agua! mas suerte la proxima vez')
                jugador_tablero_juego.tablero[fila, columna] = "$"
                print(f'\njugador_tablero_juego \n{jugador_tablero_juego.tablero}')
                print(f'\nmaquina_tablero_barcos \n{maquina_tablero_barcos.tablero}')
                return (disparar_maquina_facil())
            # Marcamos el disparo fallido y pasa el turno a la máquina

            
            elif maquina_tablero_barcos.tablero[fila, columna] == "O":
                print(f'\nHas alcanzado un barco, sigue así')
                jugador_tablero_juego.tablero[fila, columna] = "X"
                maquina_tablero_barcos.tablero[fila, columna] = "X"
                print(f'\njugador_tablero_juego \n{jugador_tablero_juego.tablero}')
                print(f'\nmaquina_tablero_barcos \n{maquina_tablero_barcos.tablero}')
                return disparar_jugador()
            # Marcamos el impacto sobre el barco de la máquina y vuelve a ser el turno del jugador



#Esta función representa el turno del jugador. 
def disparar_maquina_facil():

    while "O" in jugador_tablero_barcos.tablero and "O" in maquina_tablero_barcos.tablero:
    #Lo primero que hace es comprobar que siguen quedando barcos en pie en cualquiera de los dos 
    #tableros; si no, mira quién ha ganado y lo saca por pantalla

        fila = np.random.randint(10)
        columna = np.random.randint(10)
        #Se sacan las coordenadas de disparo de la máquina de forma aleatoria

        if maquina_tablero_juego.tablero[fila, columna] == "_":  
        #Controlamos para que no dispare a un sitio donde ya ha disparado; si no, se ejecuta de nuevo la función

            if jugador_tablero_barcos.tablero[fila, columna] == "_":
                print(f'\nLa máquina ha golpeado en el agua. Te toca de nuevo')
                maquina_tablero_juego.tablero[fila, columna] = "$"
                print(f'\nmaquina_tablero_juego\n{maquina_tablero_juego.tablero}')
                print(f'\njugador_tablero_barcos\n{jugador_tablero_barcos.tablero}')
                return (disparar_jugador())
            # Marcamos el disparo fallido y pasa el turno al jugador

            elif jugador_tablero_barcos.tablero[fila, columna] == "O":
                print(f'\nLa máquina te ha golpeado en un barco. Le toca de nuevo a la máquina')
                maquina_tablero_juego.tablero[fila, columna] = "X"
                jugador_tablero_barcos.tablero[fila, columna] = "X"
                print(f'\nmaquina_tablero_juego\n{maquina_tablero_juego.tablero}')
                print(f'\njugador_tablero_barcos\n{jugador_tablero_barcos.tablero}')
                return (disparar_maquina_facil())
            # Marcamos el impacto sobre el barco del jugador y vuelve a ser el turno de la máquina
            
            elif jugador_tablero_barcos.tablero[fila, columna] in ["$", "X"]:
                print(f'\nYa has disparado en esta posición')
                print(f'\nmaquina_tablero_juego\n{maquina_tablero_juego.tablero}')
                print(f'\njugador_tablero_barcos\n{jugador_tablero_barcos.tablero}')
                return (disparar_jugador())
            #En este caso no marcamos nada sobre el tablero y pasa el turno al jugador
            
        else:
            disparar_maquina_facil()
    else:
        return terminar_juego()



#Esta función controla el turno de juego y llama al jugador para que haga el primer ataque
def turno_de_juego():

    disparar_jugador()

#Esta 
def terminar_juego():

    if "O" not in jugador_tablero_barcos.tablero:
        print("La máquina ha ganado")
    
    elif "O" not in maquina_tablero_barcos.tablero:
        print("Has ganado")


def jugar_de_nuevo(): 
       
    otra_vez = input("¿Quieres jugar de nuevo? Toca S para Sí o N para No ")

    while otra_vez != "S" and otra_vez != "N":
        otra_vez = input("¿Quieres jugar de nuevo? Toca S para sí o N para No ")

    if otra_vez == "S":
        return hundir_la_flota()
        
    elif otra_vez == "N":
        print("Gracias por jugar")


    #Primero llama al turno del jugador, que a su vez irá llamando al turno de la máquina, según corresponda

    #Cuando se finalice el juego, bien porque gane la máquina o el jugador, bien porque el jugador decida salir,
    #se le preguntará si quiere volver a jugar de nuevo       