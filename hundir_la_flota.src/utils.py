import numpy as np
import random

#Creo la clase tablero, con sus atributos (tablero y barcos) y métodos de colocación de barcos

class Tablero:    

    def __init__(self, tablero, eslora_barcos = {"4A" : 4, "3A" : 3, "3B" : 3, "2A" : 2, \
        "2B"  : 2, "2C" : 2, "1A" : 1, "1B" : 1, "1C" : 1, "1D" : 1}):
        '''
        Los objetos tablero tienen un atributo de clase tablero y otro que es un diccionario con los
barcos a colocar (común para todos los tableros)
        '''
        self.tablero = tablero
        self.eslora_barcos = eslora_barcos


    def colocar_barcos_aleatorio(self):
        '''
        Este método sirve para colocar los barcos en el tablero, de manera aleatoria
        '''
        indice = 0

        while indice < len(self.eslora_barcos): 
            #Con un bucle while hago que siga iterando y avanzando por las posiciones de la lista de barcos
            eslora = list(self.eslora_barcos.values())[indice]

            semilla = np.random.randint(0, 10000)
            
            # Posicion inicial del barco (definimos la fila y la columna)
            np.random.seed(semilla)
            posicion_inicial = np.random.randint(10, size = 2)
            fila = posicion_inicial[0]
            columna = posicion_inicial[1]

            # 'N' - 'S' - 'E' - 'O'
            orientacion = random.choice(['N', 'S', 'E', 'O'])

            # Recogemos las 4 posiciones colindantes a la posición inicial
            coors_posiN = self.tablero[fila:fila - eslora:-1, columna]
            coors_posiE = self.tablero[fila, columna: columna + eslora]
            coors_posiS = self.tablero[fila:fila + eslora, columna]
            coors_posiO = self.tablero[fila, columna: columna - eslora:-1]

            # Comprobamos si esas posiciones son válidas. Si lo son, colocamos el barco e imprimimos de nuevo el tablero
            # Orientacion Norte
            if orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                self.tablero[fila:fila - eslora:-1, columna] = 'O'
                indice += 1

            # Orientacion Este
            elif orientacion == 'E' and 0 <= columna + eslora < 10 and 'O' not in coors_posiE:
                self.tablero[fila, columna: columna + eslora] = 'O'
                indice += 1

            # Orientacion Sur
            elif orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                self.tablero[fila:fila + eslora, columna] = 'O'
                indice += 1

            # Orientacion Oeste
            elif orientacion == 'O' and 0 <= columna - eslora < 10 and 'O' not in coors_posiO:
                self.tablero[fila, columna: columna - eslora:-1] = 'O'
                indice += 1

            # Si no cumple con las dimensiones del tablero, o la posición ya está ocupada por otro barco
            # Probamos con otra coordenada
            else:
                continue

        return self.tablero


    def colocar_barcos_manual(self):
        '''
        Este método sirve para colocar los barcos en el tablero, según las coordenadas que especifique el jugador
        '''

        indice = 0

        while indice < len(self.eslora_barcos): 
            #Con un bucle while hago que siga iterando y avanzando por las posiciones de la lista de barcos
            eslora = list(self.eslora_barcos.values())[indice]

            # Se le pide que seleccione la coordenada inicial donde quiere colocar el barco

            coordenada_inicial = input(f'\nTu barco mide {eslora}. Indica las coordenadas donde deseas \
posicionar tu barco (p.ej. 3.5) ')
            coordenada_inicial = coordenada_inicial.split(".")
            fila = int(coordenada_inicial[0])
            columna = int(coordenada_inicial[1])

            #Se le pide que elija una orientación para el barco: 'N' - 'S' - 'E' - 'O'
            orientacion = input("Selecciona la orientación de tu barco ('N', 'S', 'E', 'O') ")
            orientacion = orientacion.upper()

            # Recogemos las 4 posiciones colindantes a la posición inicial
            coors_posiN = self.tablero[fila:fila - eslora:-1, columna]
            coors_posiE = self.tablero[fila, columna: columna + eslora]
            coors_posiS = self.tablero[fila:fila + eslora, columna]
            coors_posiO = self.tablero[fila, columna: columna - eslora:-1]

            # Comprobamos si esas posiciones son válidas. Si lo son, colocamos el barco e imprimimos de nuevo el tablero
            # Orientacion Norte
            if orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                self.tablero[fila:fila - eslora:-1, columna] = 'O'
                print(f'\n Ya está colocado tu barco. Así queda tu tablero:\n {self.tablero}')
                indice += 1

            # Orientacion Este
            elif orientacion == 'E' and 0 <= columna + eslora < 10 and 'O' not in coors_posiE:
                self.tablero[fila, columna: columna + eslora] = 'O'
                print(f'\n Ya está colocado tu barco. Así queda tu tablero:\n {self.tablero}')
                indice += 1

            # Orientacion Sur
            elif orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                self.tablero[fila:fila + eslora, columna] = 'O'
                print(f'\n Ya está colocado tu barco. Así queda tu tablero:\n {self.tablero}')
                indice += 1

            # Orientacion Oeste
            elif orientacion == 'O' and 0 <= columna - eslora < 10 and 'O' not in coors_posiO:
                self.tablero[fila, columna: columna - eslora:-1] = 'O'
                print(f'\n Ya está colocado tu barco. Así queda tu tablero:\n {self.tablero}')
                indice += 1

            # Si no cumple con las dimensiones del tablero, o la posición ya está ocupada por otro barco
            # Probamos con otra coordenada
            else:
                print(f'\nLa coordenada {coordenada_inicial} con orientación {orientacion} no es válida. \
Introduce otra coordenada u otra orientación\n')
                continue

        return self.tablero
    

    def modo_colocacion(self):
        '''
        Este método sirve para preguntarle al jugador cómo desea colocar sus barcos en el tablero, 
de forma aleatoria o manual, y redirige al método de clase oportuno
        '''

        mensaje = f"""A continuación, decide la forma en la que quieres colocar los barcos.
    Introduce 1 si deseas colocar los barcos de forma ALEATORIA
    Introduce 2 si deseas colocar los barcos de forma MANUAL
    """
    
        eleccion = (input(mensaje))

        if not eleccion.isnumeric():
            error = f'{eleccion} no es un número válido'
            print(error)
            return self.modo_colocacion()

        if int(eleccion) == 1:
            print(f'\n Has elegido colocar tus barcos de forma aleatoria. Así queda tu tablero de barcos: \n')
            return self.colocar_barcos_aleatorio()

        elif int(eleccion) == 2:
            print(f"""\nHas elegido colocar tus barcos de forma manual. 
    A continuación vamos a colocar cada uno de ellos:""") 
            return self.colocar_barcos_manual()
        
        else:
            error = f'{eleccion} no es un número válido'
            print(error)
            return self.modo_colocacion()












        
        
    