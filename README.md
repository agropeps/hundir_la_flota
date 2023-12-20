## Hundir la flota de Thide y Pepe

### Autores
>José Ripoll Pina

>Thide E. Llorente Llorente


### Librerías empleadas
>numpy

>random


### Recursos utilizados
>Apuntes proporcionados por el profesor Alberto Romero

>Resolución de dudas por parte del profesor Alberto Romero y del TA Antonio Macorra

>ChatGPT y Stack Overflow para resolución de dudas


### Descripción del proyecto
El proyecto ha consistido en desarrollar un juego de hundir la flota, donde un jugador se enfrenta a una máquina (la consola de Python) para ver quién es el primero que consigue hundir los barcos del adversario.

Para ello, el jugador se comunica con Python por medio de una serie de inputs para posicionar sus barcos en su tablero y/o atacar al tablero de la máquina.

Para nuestro juego, hemos creado varios scripts:

- **main.py**: desde donde se corre la función que contiene el juego (``constantes.hundir_la_flota()``). Esta función se encuentra definida dentro del script *constantes* y por lo tanto es necesario importarlo antes de ejecutarla.

- **utils.py**: en este script primero se importa numpy y random, y se recoge la definición de la clase *Tablero*, con sus atributos de clase *tablero* y *eslora_barcos*. Este último es un diccionario que recoge todos los barcos que se deben colocar. En el script utils.py también se definen varios métodos de la clase Tablero:

    - ``colocar_barcos_aleatorio()``: este método sirve para colocar todos los barcos en el tablero, de manera aleatoria. Para ello, fijamos una semilla y le pedimos que vaya buscando coordenadas de forma aleatoria, implementándolas solo en el caso de ser válidas. Hacemos uso de bucles while, slicing, control de flujo y de las librerías numpy y random

    - ``colocar_barcos_manual()``: este método sirve para colocar los barcos en el tablero, según las coordenadas que especifique el jugador. Para ello, le pedimos que indique las *coordenadas* en formato número.número y elija la *orientación* (norte, sur, este u oeste). Luego se comprueba si dicha colación es válida, y se implementa solo si es afirmativo. Hacemos uso de inputs, bucles while, slicing, control de flujo y de la librería numpy

    - ``modo_colocacion()``: este método sirve para preguntarle al jugador cómo desea colocar sus barcos en el tablero, de forma aleatoria o manual, y redirige al método de clase oportuno (a *colocar_barcos_aleatorio()* o a *colocar_barcos_manual()*, respectivamente). Hacemos uso de inputs, control de flujo y de funciones

- **constantes.py**: en este script primero se importa la librería numpy y los scripts *utils* y *dificultad_facil*, desde los que se tomarán funciones. A su vez, este script recoge varias funciones:

    - ``hundir_la_flota()``: esta función es la principal del juego, la que lo inicia, y llama a su vez a dos funciones recogidas en constantes.py:
        
        - ``inicio()``: esta función da la bienvenida al jugador, le presenta las instrucciones, crea los cuatro tableros de juegos necesarios, le pregunta al jugador cómo quiere colocar los barcos (aleatoria o manualmente) y los coloca. Hacemos uso de la clase Tablero y de la librería numpy para crear el array que será el tablero, llamamos a métodos de la clase, modificamos el scope de algunas variables que utilizaremos fuera de la función e imprimimos los tableros por pantalla.

        - ``dificultad()``: esta función pregunta al jugador el nivel de dificultad con el que desea jugar (fácil, medio o difícil), y le redirige a la *función disparar_jugador()* correspondiente, ``que estarán recogidas en otros scripts``. Hacemos uso de control de flujo y funciones.

        - ``terminar_juego()``: esta función es llamada una vez se acaben de ejecutar los turnos del jugador y de la máquina. Lo que hace es verificar quién de los dos ha ganado e imprimirlo por pantalla, y luego llama a la función *jugar_de_nuevo()*. Hacemos uso de control de flujo y funciones.

        - ``jugar_de_nuevo()``: esta función le pregunta al jugador si quiere jugar de nuevo y, en ese caso, vuelve a iniciar el juego, con el respectivo mensaje de bienvenida y demás. Hacemos uso de control de flujo, inputs y funciones.

- **dificultad_facil.py**: este script se ejecuta cuando la persona señala que quiere jugar en modo fácil. En primer lugar se importa la librería numpy y el script de constantes. Consta de dos funciones:

    - ``disparar_jugador()``: esta función controla el turno de juego del jugador. Primero verifica que siguen quedando barcos en los tableros, ya que si se hundieran todos los barcos de uno de ellos, el juego habría terminado y se llamaría a *terminar_juego()*. Después se le pide a la persona que introduzca las coordenadas donde desea disparar; se le informa además de que puede salir del juego si introduce el caracter *E*. Si la persona introduce un carater no válido, se le piden de nuevo las coordenadas. Después se imprime en los tableros si la persona ha acertado sobre un barco (aparecerá una X en el tablero) o si ha tocado agua (aparecerá $). Si acierta, vuelve a ser su turno; pero si falla, el turno pasa a la máquina, llamando a la función *disparar_maquina_facil()*. Hemos hecho uso de bucles, inputs, try/except, break/continue, scope, control de flujo, accessing y funciones.

    - ``disparar_maquina_facil()``: esta función controla el turno de juego de la máquina. De forma similar al anterior, verifica que queden barcos en los tableros, pero en este caso las coordenadas son aleatorias, proporcionadas por la librería numpy. Se comprueba si ha acertado o fallado: en caso de haber acertado, se repite su turno; pero si ha fallado (i.e. agua), el turno pasa al jugador, llamando a la función *disparar_jugador()*. Hemos hecho uso de bucles, de la librería numpy, control de flujo, accessing y funciones.
    
    El juego continua hasta que uno de los dos tableros pierda todos sus barcos.

- **dificultad_media.py**: este script se ejecuta cuando la persona señala que quiere jugar en modo medio. Es similar al script de *dificultad_facil.py*, solo que en este caso en disparar_maquina_medio(), la máquina hace dos disparos al mismo tiempo y se verifica si alguno de ellos es verdadero. La máquina tiene más probabilidades de acertar.

- **dificultad_dificil.py**: este script se ejecuta cuando la persona señala que quiere jugar en modo dificil. Es similar al script de *dificultad_facil.py*, solo que en este caso en disparar_maquina_dificil(), la máquina hace tres disparos al mismo tiempo y se verifica si alguno de ellos es verdadero. La máquina tiene aún más probabilidades de acertar.