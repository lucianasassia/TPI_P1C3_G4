import random

# Función para crear un tablero vacío
def crear_tablero(tamano):
    tablero = {}
    for i in range(tamano):
        for j in range(tamano):
            tablero[(i, j)] = '~'  # El agua es '~'
    return tablero

# Función para mostrar el tablero
def mostrar_tablero(tablero, tamano, es_computadora=False):
    for i in range(tamano):
        fila = ''
        for j in range(tamano):
            casilla = tablero[(i, j)]
            if es_computadora and casilla == 'B':  # Los barcos no se deben mostrar
                fila += '~ '  # Si es la computadora, no mostrar los barcos
            else:
                fila += casilla + ' '
        print(fila)
    print()

# Función para colocar un barco de tamaño 'tamaño_barco' de forma aleatoria
def colocar_barco(tablero, tamano, tamaño_barco):
    colocado = False
    while not colocado:
        orientacion = random.choice(['horizontal', 'vertical'])
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)

        if orientacion == 'horizontal':
            if columna + tamaño_barco <= tamano and all(tablero[(fila, columna + i)] == '~' for i in range(tamaño_barco)):
                for i in range(tamaño_barco):
                    tablero[(fila, columna + i)] = 'B'
                colocado = True
        else:
            if fila + tamaño_barco <= tamano and all(tablero[(fila + i, columna)] == '~' for i in range(tamaño_barco)):
                for i in range(tamaño_barco):
                    tablero[(fila + i, columna)] = 'B'
                colocado = True

# Función para disparar a una casilla
def disparar(tablero, fila, columna):
    if tablero[(fila, columna)] == 'B':
        tablero[(fila, columna)] = 'X'  # Barco hundido
        return 'tocado'  # En lugar de True, usamos 'tocado'
    elif tablero[(fila, columna)] == '~':
        tablero[(fila, columna)] = 'O'  # Agua
        return 'agua'  # En lugar de False, usamos 'agua'
    else:
        return 'ya_disparado'  # Ya disparaste ahí

# Función para que la computadora dispare
def disparar_computadora(tablero, tamano):
    fila, columna = random.randint(0, tamano - 1), random.randint(0, tamano - 1)
    while tablero[(fila, columna)] in ['X', 'O']:  # Asegurarse de no disparar al mismo lugar
        fila, columna = random.randint(0, tamano - 1), random.randint(0, tamano - 1)
    return disparar(tablero, fila, columna), fila, columna

# Función principal del juego
def jugar(tamano=5, barcos=3, tamaño_barco=2):
    tablero_jugador = crear_tablero(tamano)
    tablero_computadora = crear_tablero(tamano)

    # Colocar los barcos de la computadora
    for _ in range(barcos):
        colocar_barco(tablero_computadora, tamano, tamaño_barco)

    # Colocar los barcos del jugador
    for _ in range(barcos):
        while True:
            try:
                print("\nColoca tu barco.")
                fila = int(input(f"Introduce la fila (0-{tamano - 1}): "))
                columna = int(input(f"Introduce la columna (0-{tamano - 1}): "))
                if fila < 0 or fila >= tamano or columna < 0 or columna >= tamano:
                    print("Coordenadas fuera de rango. Intenta de nuevo.")
                    continue
                if tablero_jugador[(fila, columna)] == 'B':
                    print("Ya hay un barco en esta posición. Intenta otra casilla.")
                    continue
                colocar_barco(tablero_jugador, tamano, tamaño_barco)
                break
            except ValueError:
                print("Por favor, introduce números válidos.")

    # Juego
    while True:
        # Mostrar los tableros
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador, tamano)
        print("Tablero de la computadora:")
        mostrar_tablero(tablero_computadora, tamano, es_computadora=True)

        # Disparo del jugador
        try:
            fila = int(input(f"Introduce la fila (0-{tamano - 1}): "))
            columna = int(input(f"Introduce la columna (0-{tamano - 1}): "))
        except ValueError:
            print("Por favor, introduce números válidos.")
            continue

        if not (0 <= fila < tamano and 0 <= columna < tamano):
            print("Coordenadas fuera de rango. Intenta de nuevo.")
            continue

        resultado = disparar(tablero_computadora, fila, columna)

        if resultado == 'tocado':
            print("¡Tocado!")
            tablero_jugador[(fila, columna)] = 'X'  # Marcar el disparo en el tablero del jugador
        elif resultado == 'agua':
            print("Agua.")
            tablero_jugador[(fila, columna)] = 'O'  # Marcar el disparo en el tablero del jugador
        elif resultado == 'ya_disparado':
            print("Ya has disparado aquí antes.")

        # Comprobar si el jugador ha ganado
        if all(tablero_computadora[(i, j)] != 'B' for i in range(tamano) for j in range(tamano)):
            print("¡Has hundido todos los barcos de la computadora! ¡Ganaste!")
            break

        # Disparo de la computadora
        print("\nLa computadora está disparando...")
        resultado, fila, columna = disparar_computadora(tablero_jugador, tamano)
        if resultado == 'tocado':
            print(f"La computadora ha tocado un barco en ({fila}, {columna})")
        else:
            print(f"La computadora disparó al agua en ({fila}, {columna})")

        # Comprobar si la computadora ha ganado
        if all(tablero_jugador[(i, j)] != 'B' for i in range(tamano) for j in range(tamano)):
            print("¡La computadora ha hundido todos tus barcos! ¡Perdiste!")
            break

# Ejecutar el juego
jugar()

