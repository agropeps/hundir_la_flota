import numpy as np
import utils
import dificultad_facil
import dificultad_media
import dificultad_dificil



#La función principal primero corre la función de inicio (para dar la bienvenida, crear tableros y situar barcos)
#y una vez terminada, entra en los bucles de juego
def hundir_la_flota():
    inicio()
    dificultad()


instrucciones = """
Bienvenide al juego Hundir la flota de Pepe y Thide.
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
    
    #Y se le pregunta cómo desea colocar sus barcos: aleatoria o manualmente. 
    #Según su respuesta, se llama al método de clase oportuno y se colocan los barcos en su tablero de barcos
    print(jugador_tablero_barcos.modo_colocacion())
    #En dicho tablero se van a ir reflejando los disparos que le haga la máquina

    #Se crea el tablero de juego del jugador, donde se van recogiendo los disparos que hace a la máquina: 
    #sus aciertos y fallos. Es el tablero en el que el jugador se ha de basar para tomar decisiones
    global jugador_tablero_juego
    jugador_tablero_juego = utils.Tablero((np.full((10,10), "_")))
    #print(f'\nEste va a ser el tablero donde se reflejarán tus aciertos y fallos: \n {jugador_tablero_juego.tablero}\n')
    #Este print lo teníamos como ayuda en la programación. Ahora lo dejamos comentado para que no se muestre por pantalla

    #Creamos el tablero de barcos de la máquina y situamos sus barcos aleatoriamente. En dicho tablero se van a ir
    #reflejando los disparos que el jugador le haga. Una vez terminada la programación, este tablero 
    #debe permanecer oculto
    global maquina_tablero_barcos
    maquina_tablero_barcos = utils.Tablero((np.full((10,10), "_")))
    maquina_tablero_barcos.colocar_barcos_aleatorio()
    #print(f'Este es el tablero donde la máquina coloca los barcos: \n {maquina_tablero_barcos.tablero}\n')

    #Creamos el tablero de juego de la máquina, donde se van recogiendo los disparos que hace al jugador. 
    #Es el tablero en el que Python se basa para no repetir coordenadas. Una vez terminada la programación, 
    #este tablero debe permanecer oculto
    global maquina_tablero_juego
    maquina_tablero_juego = utils.Tablero((np.full((10,10), "_")))
    #print(f'Este es el tablero donde se reflejan aciertos y fallos de la máquina: \n {maquina_tablero_juego.tablero}\n')




def dificultad():

    mensaje = """\n Ahora debes elegir el nivel de dificultad del juego:
Introduce 1 para nivel FÁCIL
Introduce 2 para nivel MEDIO
Introduce 3 para nivel DIFÍCIL
 """
    num_dificultad = input(mensaje)
    
    if int(num_dificultad) == 1:
        return dificultad_facil.disparar_jugador()   
                       
    elif int(num_dificultad) == 2:
        return dificultad_media.disparar_jugador()  
    
    elif int(num_dificultad) == 3:
        return dificultad_dificil.disparar_jugador()  
    
    else:
        error = f'{num_dificultad} no es un número válido'
        print(error)
        return dificultad()



#Esta función imprime quién ha ganado una vez que se ha terminado el juego
def terminar_juego():

    if "O" not in jugador_tablero_barcos.tablero:
        print("La máquina ha ganado")
        return jugar_de_nuevo()
    
    elif "O" not in maquina_tablero_barcos.tablero:
        return f'Has ganado {jugar_de_nuevo()}'
    


#Esta función pregunta al jugador si quiere jugar de nuevo (tras haber perdido, ganado o abandonado la partida)
def jugar_de_nuevo(): 
       
    otra_vez = input("¿Quieres jugar de nuevo? Toca S para Sí o N para No ")

    if otra_vez != "S" and otra_vez != "N":
        otra_vez = input("¿Quieres jugar de nuevo? Toca S para sí o N para No ")

    if otra_vez == "S":
        return hundir_la_flota()
    
    elif otra_vez == "N":
        print("Gracias por jugar")
        