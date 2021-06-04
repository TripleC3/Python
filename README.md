# Proyectos de Python 3

### The Binding of Isaac bot
>/Isaac Bot/bot.py

Un bot para el videojuego The Binding of Isaac, con el código en Español, que se centra en la búsqueda de imágenes en pantalla, escalable a cualquier resolución, y el control del teclado.

### Buscador en maps 
>buscador_mapa.py

Se introduce una dirección y el script abre un mapa en el navegador con un marcador en la dirección.

### Crackeador de hashes por fuerza bruta
>hash_pass_cracker.py

Al introducir una clave y una encriptación, el programa encriptará la clave con un hash, entonces almacenará ese hash y tratará de forzarlo probando todas las combinaciones de letras, números y símbolos posibles, empezando por una letra (a, b... y, z) y sumando una letra cuando termina de probar todas las combinaciones (aa... zz, aaa... zzz). Útil para cuando se tiene que forzar un hash y se conoce la encriptación, al ser de python es mucho más lento que cualquiera en C++.

### New processes detector
>new_process_detector.pyw

Programa [con interfaz](https://imgur.com/a/ipjYBc6) que escanea los procesos de tu ordenador con el primer click, los vuelve a escanear con el segundo click y enseña en la consola los nuevos procesos que se han abierto, puede detectar todos los procesos que abre un programa de Windows incluso si son varios.

### Identificador de teclas en PyGame
>pygame_key_translator.py

Abre una pequeña ventana de PyGame encima de la consola, al dar click en la ventana y pulsar cualquier tecla, la consola enseñará el código de identificación de la tecla que se necesita para escribir código en pygame.

### Comprobador de RAM
>ram_checker.py

Muestra la RAM total, la que se está consumiendo y la restante en MB.

### Escáner de puertos TCP
>tcp_port_checker.py

Se introduce un dominio o una IP, después se introducen los puertos a testear y se comprueba si los puertos están abiertos o cerrados.
>tcp_port_checker_console.py

Versión para la consola con dos opciones, `-t` para el dominio o ip objetivo y `-p` para los puertos a testear. También se puede usar `-h` o `--help` para ver una lista descriptiva.

### Extractor de contraseñas de wifi almacenadas en Windows
>wifi_pass_extractor.py

Se ejecuta el script y se extraen todos los nombres y contraseñas de las redes que se hayan guardado en el ordenador.
