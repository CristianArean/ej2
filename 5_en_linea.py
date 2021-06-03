#import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300

ALTO_TABLERO = 10
ANCHO_TABLERO = 10

filas = 10
columnas = 10
vacio = 0
def juego_crear():
    """Inicializar el estado del juego"""
    M = []
    for line in range(filas):
        ROW = []
        for char in range(columnas):
            ROW.append(vacio)
        M.append(ROW)
    return M


def juego_actualizar(juego, x, y)
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    if x in range(filas) 
        and y in range(columnas)
        and x, y == vacio:
        new_juego = []
        for i in range (filas):
            row = []
            for j in range (columnas):
                row.append(juego[i][j])
            new_juego.append(row) 
        new_juego[x][y] = #el 'x' o el 'o'
        return new_juego 
    return juego



def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)
    gamelib.draw_rectangle(1, 10)
def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)