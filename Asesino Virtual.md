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
⢤⡟⠧⣿⣷⣿⣗⡪⣳⡏⣍⣭⠉⡕⢉⢋⣽⠅⠀⠀⠀⠝⡷⣤⣀⣀⠀⠀⠀⠀⢀⣠⣴⡿⢿⠋⠀⢰⣤⢿⡿⡣⣷⡷⡋⢲⣎⢉⡞⡇⢿⠿⣿⣮⠿
⢨⣶⣿⣿⣯⢇⢏⣳⡽⣙⡅⠄⡏⠃⠭⣷⠓⣯⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⡽⣿⡿⠧⡺⢞⡛⡒⣛⠟⣏⠿⢻⣭⣛⣻⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
        
asesinoVirtual()
