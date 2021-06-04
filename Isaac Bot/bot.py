import pyautogui as pg
import time
import keyboard
import winsound


# Presionar tecla

def tecla(tecla_str):
    pg.keyDown(tecla_str)
    time.sleep(0.1)
    pg.keyUp(tecla_str)
    time.sleep(0.1)


# Busca el spawn en el mapa, la sala más blanca

def buscar_spawn():
    posibles_spawns = pg.locateAllOnScreen("spawn.png", region=region_mapa, confidence=0.9)
    for posible_spawn in posibles_spawns:
        captura = pg.screenshot(region=posible_spawn)
        for x in range(0, posible_spawn.width, 10):
            for y in range(0, posible_spawn.height, 10):
                for n in captura.getpixel((x, y)):
                    if n > 100:
                        del posibles_spawns
                        return posible_spawn


# Configuración inicial

def configuracion():
    print("-" * 40 + "\nConfiguración\n" + "-" * 40)

    # Tamaño pantalla
    print("Tamaño de la pantalla:")
    print(f"Ancho: {ancho} | Alto: {alto}\n")

    # Mapa
    print("Buscando mapa...")
    while True:
        for i in range(2):
            coordenadas = buscar_spawn()
            # Coordenadas: (left: x, top: y, width: ancho, height: alto)

            if coordenadas:
                print("Mapa encontrado.\n" + "-" * 40)
                return coordenadas
            else:
                print("Tabulando...")
                tecla("tab")
        reinicio()


# Calcula la dirección de la habitación del tesoro

def calculo(tesoro_punto, coordenadas):
    if tesoro_punto.x < coordenadas.left:
        return "izquierda"
    elif tesoro_punto.y < coordenadas.top:
        return "arriba"
    elif tesoro_punto.x > coordenadas.left + coordenadas.width:
        return "derecha"
    elif tesoro_punto.y > coordenadas.top + coordenadas.height:
        return "abajo"
    else:
        print("Error calculando dirección")
        quit()


# Reiniciar partida

def reinicio():
    print("Reiniciando...\n" + "-" * 40)
    pg.keyDown("r")
    time.sleep(2)
    pg.keyUp("r")
    time.sleep(1)


# Escanea el mapa constantemente en busca de una habitación amarilla mientras reinicia

def buscar_puertas(coordenadas_tuple):
    region_tesoro = (coordenadas_tuple.left - coordenadas_tuple.width,
                     coordenadas_tuple.top - coordenadas_tuple.height,
                     coordenadas_tuple.width * 3,
                     coordenadas_tuple.height * 3)
    time.sleep(0.5)
    print("Buscando habitación amarilla...")
    pg.keyDown("r")
    while True:
        tesoro = pg.locateCenterOnScreen("tesoro.png", region=region_tesoro, confidence=0.95)

        if tesoro:
            pg.keyUp("r")
            print(f"Habitación amarilla encontrada.\n" + "-" * 40)
            direccion = calculo(tesoro, coordenadas_tuple)
            for i in range(4):
                winsound.Beep(400 + i * 150, 75)
            return direccion


# Presiona teclas para moverse y detecta el movimiento

def movimiento(direccion):
    if direccion == "izquierda":
        pg.keyDown("a")
        captura = pg.screenshot(region=(int(region_isaac[0] - ancho * 0.34), region_isaac[1],
                                        region_isaac[2], region_isaac[3]))
        while pg.locateOnScreen(captura, region=(int(region_isaac[0] - ancho * 0.34), region_isaac[1],
                                                 region_isaac[2], region_isaac[3]), confidence=0.8) is not None:
            pass
        pg.keyDown("w")
        time.sleep(1)
        pg.keyUp("w")
        pg.keyUp("a")

    elif direccion == "derecha":
        pg.keyDown("d")
        captura = pg.screenshot(region=(int(region_isaac[0] + ancho * 0.34), region_isaac[1],
                                        region_isaac[2], region_isaac[3]))
        while pg.locateOnScreen(captura, region=(int(region_isaac[0] + ancho * 0.34), region_isaac[1],
                                                 region_isaac[2], region_isaac[3]), confidence=0.8) is not None:
            pass
        pg.keyDown("w")
        time.sleep(1)
        pg.keyUp("w")
        pg.keyUp("d")

    elif direccion == "arriba":
        pg.keyDown("w")
        captura = pg.screenshot(region=(int(ancho * 0.44), 0, int(ancho * 0.12), int(alto * 0.12)))
        while pg.locateOnScreen(captura, region=(int(ancho * 0.44), 0, int(ancho * 0.12), int(alto * 0.12)),
                                confidence=0.8) is not None:
            pass
        pg.keyUp("w")

    elif direccion == "abajo":
        pg.keyDown("s")
        captura = pg.screenshot(region=(int(ancho * 0.44), int(alto * 0.88), int(ancho * 0.12), int(alto * 0.12)))
        while pg.locateOnScreen(captura, region=(int(ancho * 0.44), int(alto * 0.88),
                                                 int(ancho * 0.12), int(alto * 0.12)), confidence=0.8) is not None:
            pass
        pg.keyUp("s")


# Pregunta

def confirmar():
    print("Esperando confirmación")
    while True:
        respuesta = keyboard.read_key()
        if respuesta.lower() == "r":
            print("Objeto rechazado.\n" + "-" * 40)
            time.sleep(0.01)
            break
        if respuesta.lower() == "enter":
            print("Objeto aceptado\n" + "-" * 40)
            quit()


# Start

print("Iniciando...")
time.sleep(1)
ancho, alto = pg.size()
region_mapa = (int(ancho * 0.8), 0, int(ancho * 0.2), int(alto * 0.2))
region_isaac = (int(ancho * 0.47), int(alto * 0.62), int(ancho * 0.06), int(alto * 0.14))
print("----------INSTRUCCIONES DE USO----------\n"
      "IMPORTANTE: Entrar en opciones y fijar 'gamma' en 150\n"
      "Solo funciona con 60 FPS\n"
      "Dentro de la habitación del tesoro:\n"
      "'R' para reiniciar, 'Enter' para cerrar el programa")

coordenadas_spawn = configuracion()

while not keyboard.is_pressed("esc"):
    puerta = buscar_puertas(coordenadas_spawn)
    movimiento(puerta)
    confirmar()
