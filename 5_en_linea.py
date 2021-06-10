import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300

ALTO_TABLERO = 10
ANCHO_TABLERO = 10


VACIO = ''
def juego_crear():
    """Inicializar el estado del juego"""
    juego = {}
    M = []
    for line in range(ALTO_TABLERO):
        ROW = []
        for char in range(ANCHO_TABLERO):
            ROW.append(VACIO)
        M.append(ROW)
    juego['tablero'] = M
    juego['turno'] = 'O'
    return juego
    

def hay_valor_en_coordenada(juego, x, y):
    return juego['tablero'][x][y] != VACIO
        


def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    if x > 40 and x < 260 and y > 40 and y < 260:
        fila = int((x - 40) / 22)
        columna = int((y - 40) / 22)
        if not hay_valor_en_coordenada(juego, fila, columna):
            juego['tablero'][fila][columna] = juego['turno']
            if juego['turno'] == 'O':
                juego['turno'] = 'X'
            elif juego['turno'] == 'X':
                juego['turno'] = 'O'
    return juego



def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)
    gamelib.draw_rectangle(ANCHO_VENTANA - ALTO_VENTANA * 0.86, ALTO_VENTANA - ALTO_VENTANA * 0.86, ANCHO_VENTANA - ALTO_VENTANA * 0.1333, ALTO_VENTANA - ALTO_VENTANA * 0.1333, outline='white', width=2, fill=None)
    for i in range(40, 280, 22):
        gamelib.draw_line(ANCHO_VENTANA - ALTO_VENTANA * 0.86, i, ANCHO_VENTANA - ANCHO_VENTANA * 0.14, i, fill='white')
        for j in range(40, 280, 22):
            gamelib.draw_line(j, ALTO_VENTANA - ALTO_VENTANA * 0.86, j, ALTO_VENTANA - ANCHO_VENTANA * 0.14)
    for i in range(ALTO_TABLERO):
        for j in range(ANCHO_TABLERO):
            gamelib.draw_text(juego['tablero'][i][j], 40 + (i * 22)+ 11, 40 + (j *22) + 11)
    gamelib.draw_text('es el turno de ' + juego['turno'], 150, 280 )

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
