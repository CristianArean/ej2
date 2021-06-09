import gamelib

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

def hay_valor_en_coordenada(juego, x, y):
    
     for i in range(filas):
        for j in range(columnas):
            if juego[i][j] !=0:
                return True
            return False


def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    '''
    def turnos():
    While True:
        if turno == jugador_x:
            valor == 'X'
            print('turno de jugador x')
        elif turno == jugador_o:
            valor == 'o'
            print('turno de jugador y')
        False
    return valor
    valor = turnos()
    '''
    if hay_valor_en_coordenada(juego, x, y) == False:
        new_juego = []
        for i in range (filas):
            row = []
            for j in range (columnas):
                row.append(juego[i][j])
            new_juego.append(row) 
        new_juego[i][j] == 1 #el 'x' o el 'o'
        return new_juego 
    return juego



def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)
    gamelib.draw_rectangle(ANCHO_VENTANA - 260, ALTO_VENTANA - 260, ANCHO_VENTANA - 40, ALTO_VENTANA - 40, outline='white', width=2, fill=None)
    for i in range(40, 280, 22):
        gamelib.draw_line(ANCHO_VENTANA - 260, i, ANCHO_VENTANA - 42, i, fill='white', width=1)
        for j in range(40, 280, 22):
            gamelib.draw_line(j, ALTO_VENTANA - 260, j, ALTO_VENTANA - 42)
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
