def PasaPalabra():
    def tableroFinal():
        for i in range(26):
            print(abecedario[i],end=" ")
        print()
        print("ACIERTOS: ",aciertos,"\n","ERRORES: ",errores,"\n","PASAPALABRAS: ",sinRespuesta)
    
    abecedario=["A ","B ","C ","D ","E ","F ","G ","H ","I ","J ","K ","L ","M ","N ","O ","P ","Q ","R ","S ","T ","U ","V ","W ","X ","Y ","Z "]
    j=0
    aciertos=0
    errores=0
    sinRespuesta=26

    eligeRosco=input("Elige tu rosco: 1 o 2\n")
    
    for j in range(3):
        if (eligeRosco=="1"):
            rosco=open("D:\\Users\\Usuario\\Documents\\GitHub\\TPI_P1C3_G4\\Rosco1.txt")
        elif(eligeRosco=="2"):
            rosco=open("D:\\Users\\Usuario\\Documents\\GitHub\\TPI_P1C3_G4\\Rosco2.txt")
        linea=rosco.readline()
        #rosco1=open("D:\\Users\\Usuario\\Documents\\prueba\\Definiciones1.txt")
        #linea=rosco1.readline()
        for j in range (26): 
            campos=linea.strip().split(":")
            if (abecedario[j]!="🟩" and abecedario[j]!="🟥"):
                for i in range(26):
                    print(abecedario[i],end=" ")
                i=0
                print()
                print(campos[0])
                print(campos[1])
                respuesta=input("Respuesta:")
                respuesta=respuesta.upper()
                if(respuesta==campos[2]):
                    abecedario[j]="🟩"
                    aciertos=aciertos+1
                    sinRespuesta=sinRespuesta-1
                elif(respuesta=="PASAPALABRA"):
                    print()
                else:
                    abecedario[j]="🟥"
                    errores=errores+1
                    sinRespuesta=sinRespuesta-1
                linea=rosco.readline()
            else:
                linea = rosco.readline()
            j+=1
        j=0
    j=0
    i=0
    tableroFinal()
    rosco.close()
    
def batallaNaval ():
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
def asesinoVirtual():
    import random 
    try:
        def planoDCasa():
            print("--------------------------")
            print("|      1.Habitación      |")
            print("|                        |")
            print("-----------  -------------")
            print("|                        |")
            print("|       2.Comedor        |")
            print("|                        |")
            print("-----------  -------------")
            print("| 3.Baño   | | 4.Living  |")
            print("|                         ")
            print("|          | |           |")
            print("----------- --------------")
            print("|                        |")
            print("|      5.Cochera         |")
            print("|                        |")
            print("--------------------------")
            
        def elegir_habitacion():
            print("Elige una habitación por su numero:")
            print (" ")
            print("1: Habitacion")
            print("2: Comedor")
            print("3: Baño")
            print("4: Living")
            print("5: Cochera")
            
            
        print("    █                            ██                      ▀██▀  ▀█▀  ██            ▄                    ▀██  ")
        print("   ███     ▄▄▄▄    ▄▄▄▄   ▄▄▄▄  ▄▄▄  ▄▄ ▄▄▄     ▄▄▄       ▀█▄  ▄▀  ▄▄▄  ▄▄▄ ▄▄  ▄██▄  ▄▄▄ ▄▄▄   ▄▄▄▄    ██  ")
        print("  █  ██   ██▄ ▀  ▄█▄▄▄██ ██▄ ▀   ██   ██  ██  ▄█  ▀█▄      ██  █    ██   ██▀ ▀▀  ██    ██  ██  ▀▀ ▄██   ██  ")
        print(" ▄▀▀▀▀█▄  ▄ ▀█▄▄ ██      ▄ ▀█▄▄  ██   ██  ██  ██   ██       ███     ██   ██      ██    ██  ██  ▄█▀ ██   ██  ")
        print("▄█▄  ▄██▄ █▀▄▄█▀  ▀█▄▄▄▀ █▀▄▄█▀ ▄██▄ ▄██▄ ██▄  ▀█▄▄█▀        █     ▄██▄ ▄██▄     ▀█▄▀  ▀█▄▄▀█▄ ▀█▄▄▀█▀ ▄██▄ ")
        print(" ")
        print(" ")                             
        jugar_de_nuevo = input("¿Quieres jugar al escondite? (s/n): ")
            
        while jugar_de_nuevo == "s":
                    planoDCasa()
                    elegir_habitacion()
                    eleccion = int(input("Elegi una habitacion para salvarte: "))
                    if 1 <= eleccion <= 5:
                        habitacionPerdida = random.randint(1, 5)  
                        print(" ")
                        print(f"El asesino fue a la habitación {habitacionPerdida}")
                        if eleccion == habitacionPerdida:
                            print("El asesino te encontró. Fuiste ASESINADO")
                            print("▀██▀▀▀▀█           ██           ▄              ▀██▀▀▀▀█                                      ▄                       ▀██          ")
                            print(" ██  ▄   ▄▄▄ ▄▄▄  ▄▄▄   ▄▄▄▄  ▄██▄    ▄▄▄▄      ██  ▄    ▄▄ ▄▄▄     ▄▄▄▄    ▄▄▄   ▄▄ ▄▄▄   ▄██▄  ▄▄▄ ▄▄   ▄▄▄▄     ▄▄ ██    ▄▄▄   ")
                            print(" ██▀▀█    ██  ██   ██  ██▄ ▀   ██   ▄█▄▄▄██     ██▀▀█     ██  ██  ▄█   ▀▀ ▄█  ▀█▄  ██  ██   ██    ██▀ ▀▀ ▀▀ ▄██  ▄▀  ▀██  ▄█  ▀█▄ ")
                            print(" ██       ██  ██   ██  ▄ ▀█▄▄  ██   ██          ██        ██  ██  ██      ██   ██  ██  ██   ██    ██     ▄█▀ ██  █▄   ██  ██   ██ ")
                            print("▄██▄      ▀█▄▄▀█▄ ▄██▄ █▀▄▄█▀  ▀█▄▀  ▀█▄▄▄▀    ▄██▄▄▄▄▄█ ▄██▄ ██▄  ▀█▄▄▄▀  ▀█▄▄█▀ ▄██▄ ██▄  ▀█▄▀ ▄██▄    ▀█▄▄▀█▀ ▀█▄▄▀██▄  ▀█▄▄█▀ ")
                                                                                                                                    
                                                                                                                                    

                            print("""
⣿⣿⣿⡿⣿⣿⣿⢿⣕⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⢀⣴⡿⡿⢿⣺⡿⡟⡟⢺
⣿⣿⡿⣿⣿⣿⡻⠿⣿⣿⣿⣿⠟⣻⠯⢛⣛⣯⣿⣿⣯⣽⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣛⠻⢟⣿⣿⣿⣿⣗⡙⠿⣿⣿⣵⡿
⢻⣿⣿⣟⣛⡛⣶⣻⣿⡿⣹⢧⣋⡗⠛⣋⣭⣭⣭⣭⣙⣛⡿⠿⣶⣭⡽⢿⣿⣿⢿⣿⡷⣼⣾⣟⣿⣿⢷⣤⠩⣗⠠⡑⢌⢻⡿⣿⣿⣿⣎⠛⣿⣿⡁
⠀⠙⢿⣿⣿⣿⣿⣿⣿⢴⣽⢻⣧⣮⣿⣿⣿⣿⣿⣷⣿⣿⣿⣽⣛⣿⣯⣮⠵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣚⢿⠌⣿⣿⢿⣿⣷⡏⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⢧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣼⢿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⣠⣿⣿⣟⣯⢾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣟⣿⣿⣿⣿⣿⣿⣿⣥⣿⣸⣿⣿⣄⠀⠀
⠀⠀⠀⣰⣿⣿⣷⣟⢳⣟⢻⣿⣿⣿⣿⣿⣿⣿⣷⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣵⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⡄⠀
⠀⣠⣾⣿⢟⡽⢋⡋⣻⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣯⣹⣿⢿⣿⡀
⢰⣿⣷⣷⣿⣳⣿⣶⣬⣭⢋⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢻⢿⣇⠀⠈⠂⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠓⣉⣉⣭⣉⠑⠘⢝⢷⣽⡇
⠈⢻⣿⣿⡿⣟⣽⣿⣿⣿⣶⣿⣦⣑⠫⡿⡿⠿⣿⣿⣿⢿⠏⣤⡀⠏⠀⠀⠀⠀⠙⡋⣀⣈⠻⡿⣿⣿⡿⠿⠛⣁⣤⣾⣯⣾⣿⣿⣿⣿⡶⢪⠃⣿⠃
⠀⠈⠻⣿⣵⣿⣿⣿⣿⣿⡿⣿⣿⣿⣷⣦⣝⣟⣩⣟⣿⣯⣗⠾⣿⣦⣀⠀⠀⠀⠀⣿⣿⣟⣩⣭⣿⣷⣶⣿⣿⡿⣿⣿⣿⡿⡿⣿⣿⠟⣡⢏⣼⠃⠀
⠀⠀⠀⠈⠻⣿⣿⣿⡿⣛⠷⣯⣏⣹⢫⢏⠏⢻⡟⢿⣿⣿⣿⣿⣿⣿⢶⣭⣄⣢⡿⢿⣿⣿⣿⠟⣿⠙⠙⡍⡍⢳⣻⣼⣿⣷⣽⠟⣡⣾⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣙⠺⣗⣮⣿⣗⣿⣾⣄⡎⠀⢡⠃⠆⢿⠟⠓⠈⠃⠙⡿⠏⠁⠀⠹⢇⠁⠀⠀⡇⠀⣇⣿⣾⡷⢟⢯⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⡙⣿⣿⣿⣯⠻⣿⣷⣄⢈⠀⠀⢸⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⢸⠀⠀⠀⡇⢀⣿⠟⢛⡡⢪⣾⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣝⡌⢿⣮⣿⣇⠙⣿⣽⡿⢶⣤⣼⣤⣤⠤⣤⣤⣼⣴⣶⣶⡶⢾⠶⠓⡞⡟⡿⢁⠶⠃⡰⢟⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣿⣿⣦⡙⢿⡟⡆⠸⣷⣷⡔⣧⠀⡇⠀⠀⠀⢸⠀⠀⠀⢸⠀⢸⠀⣰⣳⡟⡁⢁⣴⠋⣴⣿⣿⡿⣿⣯⣓⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⡿⣿⡇⢿⣿⣿⡝⢧⠙⢿⡄⠹⣿⣿⣿⡀⣿⡀⠀⢀⣿⢂⠀⣀⢸⣠⣿⣷⣿⡟⡘⢀⡿⢋⣾⣿⣿⠟⠁⠙⢿⣿⣿⣬⣦⠀⠀⠀
⠀⠀⣀⣴⣿⣿⣿⣿⢛⠭⠀⠿⣿⣿⡀⢃⢨⣻⠀⠸⣿⣿⣷⣿⣷⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡏⣸⢣⡟⢁⣿⣾⣿⡏⠀⠀⠀⠀⠈⠻⣶⣟⣿⣧⣤
⣴⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⢸⣷⣕⢳⠹⣷⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣰⣻⠏⢠⣾⣻⣿⠟⠀⠀⣸⣿⣴⣦⠀⠀⠙⢯⣿⣯
⣿⣷⣿⣟⠁⠀⠀⣰⣰⣿⣣⡀⠀⠀⢈⢿⣄⠄⢛⣟⢶⡈⠙⠿⢿⣿⣿⣿⣿⣿⣿⠿⠟⢋⡾⣽⡏⢰⡿⣱⣿⠇⠀⠀⣔⣏⣿⣯⡓⣽⣆⠀⠀⠀⠈
⣯⠏⠁⠀⠀⢬⡽⣛⣿⣿⣿⡟⣦⠀⠀⠘⢿⣷⡄⠩⢢⠙⠦⣄⣀⣀⣀⣀⣀⣤⡤⠤⠖⢋⣼⠟⢠⡿⣹⣿⣟⠀⠀⢘⣼⣿⣷⡍⡟⣗⡞⣿⣵⡄⠀
⠀⠀⣠⣽⣿⣏⣿⣏⣗⣏⡿⡭⣿⣧⠀⠀⠈⢻⣿⡆⠀⠁⢰⣶⣶⣦⣤⣶⣶⣶⣶⣶⡞⠁⠀⠀⣯⣴⣿⡏⠀⠀⢀⣽⠯⢌⢻⣯⡏⣽⣿⡿⣻⣿⠆
⠀⣖⣟⣯⣯⣫⡿⣛⡿⡧⢏⡽⣋⡳⡗⡀⠀⠀⠻⣷⡄⠀⠐⠺⠿⠿⣿⣿⠿⠿⠟⠋⠀⠀⠀⣼⣿⣿⠟⠀⠀⣠⣯⣝⡯⣃⣷⢞⢝⢯⣿⢯⡽⡬⢏
⣼⢏⡟⣟⣋⡟⣯⣿⠓⢱⡇⢻⡥⣏⢡⡋⢄⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⠀⢀⢝⣿⣗⡽⣣⡋⡕⡗⡓⡯⡦⣿⣯⣹⠘
⢤⡟⠧⣿⣷⣿⣗⡪⣳⡏⣍⣭⠉⡕⢉⢋⣽⠅⠀⠀⠀⠝⡷⣤⣀⣀⠀⠀⠀⠀⢀⣠⣴⡿⢿⠋⠀⢰⣤⢿⡿⡣⣷⡷⡋⢲⣎⢉⡞⡇⢿⠿⣿⣮⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""""")
                            jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ") 
                        else:
                            print("Te has salvado, por ahora...")
                            jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        else:
            print(" ")     
            print("  ______                             __                                                           _____                                     ")
            print(" /      \                           |  \                                                         |     \                                    ")
            print("|  ▓▓▓▓▓▓\ ______   ______   _______ \▓▓ ______   _______       ______   ______   ______          \▓▓▓▓▓__    __  ______   ______   ______  ")
            print("| ▓▓ __\▓▓/      \ |      \ /       \  \|      \ /       \     /      \ /      \ /      \           | ▓▓  \  |  \/      \ |      \ /      \ ")
            print("| ▓▓|    \  ▓▓▓▓▓▓\ \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓    |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\     __   | ▓▓ ▓▓  | ▓▓  ▓▓▓▓▓▓\ \▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ")
            print("| ▓▓ \▓▓▓▓ ▓▓   \▓▓/      ▓▓ ▓▓     | ▓▓/      ▓▓\▓▓    \     | ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓   \▓▓    |  \  | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓/      ▓▓ ▓▓   \▓▓")
            print("| ▓▓__| ▓▓ ▓▓     |  ▓▓▓▓▓▓▓ ▓▓_____| ▓▓  ▓▓▓▓▓▓▓_\▓▓▓▓▓▓\    | ▓▓__/ ▓▓ ▓▓__/ ▓▓ ▓▓          | ▓▓__| ▓▓ ▓▓__/ ▓▓ ▓▓__| ▓▓  ▓▓▓▓▓▓▓ ▓▓      ")
            print(" \▓▓    ▓▓ ▓▓      \▓▓    ▓▓\▓▓     \ ▓▓\▓▓    ▓▓       ▓▓    | ▓▓    ▓▓\▓▓    ▓▓ ▓▓           \▓▓    ▓▓\▓▓    ▓▓\▓▓    ▓▓\▓▓    ▓▓ ▓▓      ")
            print("  \▓▓▓▓▓▓ \▓▓       \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓ \▓▓▓▓▓▓▓\▓▓▓▓▓▓▓     | ▓▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓            \▓▓▓▓▓▓  \▓▓▓▓▓▓ _\▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓      ")
            print("                                                              | ▓▓                                              |  \__| ▓▓                  ")
            print("                                                              | ▓▓                                               \▓▓    ▓▓                  ")
            print("                                                               \▓▓                                                \▓▓▓▓▓▓                   ")
            
    except ValueError:
        print("Por favor, ingresa un número válido.")
        
def piedraPapelTijera ():
    import random
    opciones = ["piedra", "papel", "tijera"]
    eleccion = input("Elegí piedra, papel o tijera: ").lower()
    if eleccion not in opciones:
        print("Opción no válida, elegí entre piedra, papel o tijera.")
    else:
        computadoraEleccion = random.choice(opciones)
        print("Elegiste:", eleccion)
        print("La computadora eligió:", computadoraEleccion)
        if eleccion == computadoraEleccion:
            print("¡Es un empate!")
        elif (eleccion == "piedra" and computadoraEleccion == "tijera") or \
            (eleccion == "papel" and computadoraEleccion == "piedra") or \
            (eleccion == "tijera" and computadoraEleccion == "papel"):
            print("¡Ganaste!")
        else:
            print("La computadora ganó.")
try:            
    print("""""
    ╔═══╗             ╔═══╗                 
    ║╔═╗║             ║╔═╗║                 
    ║╚═╝║╔═╗╔══╗╔══╗  ║║ ╚╝╔══╗ ╔╗╔╗╔══╗╔══╗
    ║╔══╝║╔╝║╔╗║║╔╗║  ║║╔═╗╚ ╗║ ║╚╝║║╔╗║║══╣
    ║║   ║║ ║╚╝║║╚╝║╔╗║╚╩═║║╚╝╚╗║║║║║║═╣╠══║
    ╚╝   ╚╝ ╚══╝╚═╗║╚╝╚═══╝╚═══╝╚╩╩╝╚══╝╚══╝
                ╔═╝║                        
                ╚══╝                                    
    """)
    print("         Que Deseas Jugar?")      
    print(" ") 
    print("         1-Pasa Palabra.")  
    print(" ")         
    print("         2-Batalla Naval.")    
    print(" ")      
    print("         3-Asesino Virtual.")
    print(" ")
    print("         4-Piedra Papel o Tijera.")       
    print(" ")
    print("         5-Salir")  
    
    juego = int(input())   
    if juego == 1:
        PasaPalabra()
    if juego == 2:
       batallaNaval () 
    if juego == 3:
       asesinoVirtual() 
    if juego == 4:
        piedraPapelTijera ()
    if juego == 5:
        print (""""
                                                                                                                                   
  ▄▄█▀▀▀█▄█                         ██                                                      ▀████▀                                    
▄██▀     ▀█                                                                                   ██                                      
██▀       ▀▀███▄███ ▄█▀██▄  ▄██▀██▀███  ▄█▀██▄  ▄██▀███   ▀████████▄  ▄██▀██▄▀███▄███         ██ ▀███  ▀███  ▄█▀█████▄█▀██▄ ▀███▄███  
██           ██▀ ▀▀██   ██ ██▀  ██  ██ ██   ██  ██   ▀▀     ██   ▀██ ██▀   ▀██ ██▀ ▀▀         ██   ██    ██ ▄██  ██ ██   ██   ██▀ ▀▀  
██▄    ▀████ ██     ▄█████ ██       ██  ▄█████  ▀█████▄     ██    ██ ██     ██ ██             ██   ██    ██ ▀█████▀  ▄█████   ██      
▀██▄     ██  ██    ██   ██ ██▄    ▄ ██ ██   ██  █▄   ██     ██   ▄██ ██▄   ▄██ ██        ███  ██   ██    ██ ██      ██   ██   ██    ▄▄
  ▀▀███████▄████▄  ▀████▀██▄█████▀▄████▄████▀██▄██████▀     ██████▀   ▀█████▀▄████▄       █████    ▀████▀███▄███████▀████▀██▄████▄  ██
                                                            ██                                              █▀     ██                 
                                                          ▄████▄                                            ██████▀                   

               
               """)
    
    else:
        print("Porfavor ingrese un Numero Valido. ;)")
except ValueError:
        print("Por favor, ingresa un número válido.")
