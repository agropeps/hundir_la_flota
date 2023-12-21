import constantes
import numpy as np

#Esta función representa el turno del jugador. 
def disparar_jugador():

    while "O" in constantes.jugador_tablero_barcos.tablero and "O" in constantes.maquina_tablero_barcos.tablero:
    #Lo primero que hace es comprobar que siguen quedando barcos en pie en cualquiera de los dos 
    #tableros; si no, mira quién ha ganado y lo saca por pantalla
        print(f'\nAsí llevas tu tablero de juego \n{constantes.jugador_tablero_juego.tablero}')
        coordenada_disparo = input(f'\nIndica las coordenadas donde deseas disparar (p.ej. 3.5). Si deseas salir \
del juego, introduce E ')
        #Se le piden las coordenadas al jugador mediante un input

        #Ofrecemos al jugador la posibilidad de salir del juego cuando quiera, intriduciendo E (de Exit)
        if coordenada_disparo == "E":
            print('Has abandonado la partida')
            return constantes.jugar_de_nuevo()

        #Si quedan barcos en juego, verifica si el jugador quiere salir. Si no quiere salir, transforma el
        #input en coordenadas y verifica si en ellas hay agua, barco o si ya ha golpeado antes
        
        try:
            coordenada_disparo = coordenada_disparo.split(".")
            fila = int(coordenada_disparo[0])
            columna = int(coordenada_disparo[1])

        except:
            print("Caracter no válido")
            continue

        #Primero verificamos si la persona dispara a un sitio donde ya ha disparado: si es así,
        #pasa el turno a la máquina; si no, pasa a verificar si hay agua o barco
        if constantes.jugador_tablero_juego.tablero[fila, columna] != "_":
            print(f'\nYa has disparado en esta posición')
            #print(f'\nTu tablero de juego queda \n{constantes.jugador_tablero_juego.tablero}')
            print(f'\nY tu tablero de barcos queda \n{constantes.jugador_tablero_barcos.tablero}')
            #print(f'\nmaquina_tablero_barcos \n{constantes.maquina_tablero_barcos.tablero}')
            #Esto nos sirvió para la programación. Ahora debe queda oculto
            return disparar_maquina_facil()
        #No marcamos nada sobre el tablero y pasa el turno a la máquina

        else: 
            if constantes.maquina_tablero_barcos.tablero[fila, columna] == "_":
                print(f'\n¡Agua! Más suerte la proxima vez')
                constantes.jugador_tablero_juego.tablero[fila, columna] = "$"
                print(f'\nTu tablero de juego queda \n{constantes.jugador_tablero_juego.tablero}')
                print(f'\nY tu tablero de barcos queda \n{constantes.jugador_tablero_barcos.tablero}')
                #print(f'\nmaquina_tablero_barcos \n{constantes.maquina_tablero_barcos.tablero}')
                return disparar_maquina_facil()
            # Marcamos el disparo fallido y pasa el turno a la máquina

            
            elif constantes.maquina_tablero_barcos.tablero[fila, columna] == "O":
                print(f'\nHas alcanzado un barco, sigue así')
                constantes.jugador_tablero_juego.tablero[fila, columna] = "X"
                constantes.maquina_tablero_barcos.tablero[fila, columna] = "X"
                print(f'\nTu tablero de juego queda \n{constantes.jugador_tablero_juego.tablero}')
                print(f'\nY tu tablero de barcos queda \n{constantes.jugador_tablero_barcos.tablero}')
                #print(f'\nmaquina_tablero_barcos \n{constantes.maquina_tablero_barcos.tablero}')
                return disparar_jugador()
            # Marcamos el impacto sobre el barco de la máquina y vuelve a ser el turno del jugador
    else:
        return constantes.terminar_juego()


#Esta función representa el turno de la máquina. 
def disparar_maquina_facil():

    while "O" in constantes.jugador_tablero_barcos.tablero and "O" in constantes.maquina_tablero_barcos.tablero:
    #Lo primero que hace es comprobar que siguen quedando barcos en pie en cualquiera de los dos 
    #tableros; si no, mira quién ha ganado y lo saca por pantalla

        fila = np.random.randint(10)
        columna = np.random.randint(10)
        #Se sacan las coordenadas de disparo de la máquina de forma aleatoria

        if constantes.maquina_tablero_juego.tablero[fila, columna] == "_":  
        #Controlamos para que no dispare a un sitio donde ya ha disparado; si no, se ejecuta de nuevo la función

            if constantes.jugador_tablero_barcos.tablero[fila, columna] == "_":
                print(f'\nLa máquina ha golpeado en el agua. Te toca de nuevo')
                constantes.maquina_tablero_juego.tablero[fila, columna] = "$"
                #print(f'\nmaquina_tablero_juego\n{constantes.maquina_tablero_juego.tablero}')
                #print(f'\njugador_tablero_barcos\n{constantes.jugador_tablero_barcos.tablero}')
                return disparar_jugador()
            # Marcamos el disparo fallido y pasa el turno al jugador

            elif constantes.jugador_tablero_barcos.tablero[fila, columna] == "O":
                print(f'\nLa máquina te ha golpeado en un barco. Le toca de nuevo a la máquina')
                constantes.maquina_tablero_juego.tablero[fila, columna] = "X"
                constantes.jugador_tablero_barcos.tablero[fila, columna] = "X"
                print(f'\nTu tablero de barcos queda \n{constantes.jugador_tablero_barcos.tablero}')
                #print(f'\nmaquina_tablero_juego\n{constantes.maquina_tablero_juego.tablero}')
                return disparar_maquina_facil()
            # Marcamos el impacto sobre el barco del jugador y vuelve a ser el turno de la máquina
            
        else:
            return disparar_maquina_facil()
    else:
        return constantes.terminar_juego()

